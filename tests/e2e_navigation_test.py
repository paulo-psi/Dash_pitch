import http.server
import os
import re
import socketserver
import sys
import threading
import urllib.parse
import urllib.request

PORT = 8924
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def log_message(self, format, *args):
        pass

def run_e2e_tests():
    server = socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    print(f"[INFO] Servidor HTTP de teste rodando em http://127.0.0.1:{PORT}")

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
        except Exception as e:
            errors.append(f"Erro ao acessar {full_url} (referrer: {referrer}): {e}")

    # 1. Carrega Master Hub (index.html na raiz)
    try:
        with urllib.request.urlopen(f"{base_url}/index.html", timeout=5) as resp:
            master_html = resp.read().decode("utf-8")
            print(f"[OK] Master Hub carregado com sucesso ({len(master_html)} bytes)")
    except Exception as e:
        print(f"[FAIL] Não foi possível carregar Master Hub: {e}")
        server.shutdown()
        sys.exit(1)

    # 2. Carrega Portal PIBEP 2026 (pibep-2026/index.html)
    pibep_url = f"{base_url}/pibep-2026/index.html"
    try:
        with urllib.request.urlopen(pibep_url, timeout=5) as resp:
            pibep_html = resp.read().decode("utf-8")
            print(f"[OK] PIBEP Hub carregado com sucesso ({len(pibep_html)} bytes)")
    except Exception as e:
        print(f"[FAIL] Não foi possível carregar PIBEP Hub: {e}")
        server.shutdown()
        sys.exit(1)

    # 3. Extrai e testa todos os links de pibep-2026
    dash_links = re.findall(r'href=["\'](\./dashboards/dashboard_[^"\']+\.html)["\']', pibep_html)
    pdf_links = re.findall(r'href=["\'](\./assets/pdfs/[^"\']+\.pdf)["\']', pibep_html)

    print(f"[INFO] No PIBEP Hub: {len(dash_links)} dashboards e {len(pdf_links)} PDFs.")
    if len(dash_links) != 8:
        errors.append(f"Esperado 8 links de dashboards, encontrados {len(dash_links)}")
    if len(pdf_links) != 8:
        errors.append(f"Esperado 8 links de PDFs, encontrados {len(pdf_links)}")

    for link in dash_links:
        full_d = urllib.parse.urljoin(f"{base_url}/pibep-2026/", link)
        check_url(full_d, "pibep-2026/index.html")

    for link in pdf_links:
        full_p = urllib.parse.urljoin(f"{base_url}/pibep-2026/", link)
        check_url(full_p, "pibep-2026/index.html")

    # 4. Navega em cada dashboard e testa links internos
    for d_link in dash_links:
        full_d = urllib.parse.urljoin(f"{base_url}/pibep-2026/", d_link)
        try:
            with urllib.request.urlopen(full_d, timeout=5) as resp:
                d_html = resp.read().decode("utf-8")
        except Exception as e:
            errors.append(f"Falha ao carregar dashboard {full_d}: {e}")
            continue

        # Link de retorno ao hub do evento
        if "../index.html" not in d_html:
            errors.append(f"{d_link} sem link '../index.html'")
        else:
            check_url(urllib.parse.urljoin(full_d, "../index.html"), d_link)

        # Link do PDF local
        local_pdfs = re.findall(r'href=["\'](\.\./assets/pdfs/[^"\']+\.pdf)["\']', d_html)
        if not local_pdfs:
            errors.append(f"{d_link} sem link de PDF local")
        else:
            for p in local_pdfs:
                check_url(urllib.parse.urljoin(full_d, p), d_link)

        # Seletor de equipes
        selector_opts = re.findall(r'<option\s+value=["\'](dashboard_[^"\']+\.html)["\']', d_html)
        if len(selector_opts) != 8:
            errors.append(f"{d_link} seletor com {len(selector_opts)} opções (esperado 8)")
        for opt in selector_opts:
            check_url(urllib.parse.urljoin(full_d, opt), d_link)

    server.shutdown()

    if errors:
        print(f"\n[FAIL] Erros na verificação E2E:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"\n[PASS] Bateria E2E multi-demanda concluída com 100% de sucesso! ({len(checked_urls)} URLs verificadas, zero 404s)")

if __name__ == "__main__":
    run_e2e_tests()
