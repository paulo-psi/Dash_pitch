import http.server
import os
import re
import socketserver
import sys
import threading
import urllib.parse
import urllib.request

PORT = 8923
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def log_message(self, format, *args):
        pass # Silêncio para manter o teste limpo

def run_e2e_tests():
    server = socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    print(f"[INFO] Servidor HTTP de teste rodando em http://127.0.0.1:{PORT} (root={ROOT_DIR})")

    base_url = f"http://127.0.0.1:{PORT}"
    errors = []
    checked_urls = set()

    def check_url(rel_url, referrer="root"):
        full_url = urllib.parse.urljoin(base_url + "/", rel_url.lstrip("/"))
        if full_url in checked_urls:
            return
        checked_urls.add(full_url)

        try:
            req = urllib.request.Request(full_url, method="HEAD")
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status != 200:
                    errors.append(f"HTTP {resp.status} em {full_url} (referrer: {referrer})")
                else:
                    pass
        except Exception as e:
            errors.append(f"Erro ao acessar {full_url} (referrer: {referrer}): {e}")

    # 1. Checa a raiz index.html
    try:
        with urllib.request.urlopen(f"{base_url}/index.html", timeout=5) as resp:
            content = resp.read().decode("utf-8")
            print(f"[OK] index.html carregado com sucesso ({len(content)} bytes)")
    except Exception as e:
        print(f"[FAIL] Não foi possível carregar index.html: {e}")
        server.shutdown()
        sys.exit(1)

    # 2. Extrai e testa todos os links de index.html
    dashboard_links = re.findall(r'href=["\'](\./dashboards/dashboard_[^"\']+\.html)["\']', content)
    pdf_links = re.findall(r'href=["\'](\./assets/pdfs/[^"\']+\.pdf)["\']', content)

    print(f"[INFO] Encontrados no Hub: {len(dashboard_links)} links de dashboards e {len(pdf_links)} links de PDFs.")

    if len(dashboard_links) != 8:
        errors.append(f"Esperado 8 links de dashboards no index.html, encontrados {len(dashboard_links)}")
    if len(pdf_links) != 8:
        errors.append(f"Esperado 8 links de PDFs no index.html, encontrados {len(pdf_links)}")

    for link in dashboard_links:
        check_url(link, "index.html")
    for link in pdf_links:
        check_url(link, "index.html")

    # 3. Navega em cada dashboard e testa seus links internos
    for d_link in dashboard_links:
        d_url = urllib.parse.urljoin(base_url + "/", d_link.lstrip("/"))
        try:
            with urllib.request.urlopen(d_url, timeout=5) as resp:
                d_html = resp.read().decode("utf-8")
        except Exception as e:
            errors.append(f"Falha ao carregar dashboard {d_url}: {e}")
            continue

        # Testa link para o hub
        hub_link = re.findall(r'href=["\'](\.\./index\.html)["\']', d_html)
        if not hub_link:
            errors.append(f"Dashboard {d_link} não contém link de retorno '../index.html'")
        else:
            check_url(urllib.parse.urljoin(d_url, hub_link[0]), d_link)

        # Testa link do PDF local
        local_pdf = re.findall(r'href=["\'](\.\./assets/pdfs/[^"\']+\.pdf)["\']', d_html)
        if not local_pdf:
            errors.append(f"Dashboard {d_link} não contém link de PDF local '../assets/pdfs/...'")
        else:
            for p in local_pdf:
                check_url(urllib.parse.urljoin(d_url, p), d_link)

        # Testa as opções do seletor de equipes
        selector_opts = re.findall(r'<option\s+value=["\'](dashboard_[^"\']+\.html)["\']', d_html)
        if len(selector_opts) != 8:
            errors.append(f"Dashboard {d_link} contém {len(selector_opts)} opções no seletor (esperado 8)")
        for opt in selector_opts:
            check_url(urllib.parse.urljoin(d_url, opt), d_link)

    server.shutdown()

    if errors:
        print(f"\n[FAIL] Foram encontrados {len(errors)} erros na verificação E2E:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"\n[PASS] Bateria E2E concluída com 100% de sucesso! ({len(checked_urls)} URLs verificadas, zero links 404)")

if __name__ == "__main__":
    run_e2e_tests()
