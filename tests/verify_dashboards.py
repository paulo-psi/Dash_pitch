import os
import sys
import re

REQUIRED_DASHBOARDS = [
    "dashboard_01_anchor.html",
    "dashboard_02_integremente.html",
    "dashboard_03_norman.html",
    "dashboard_04_nock.html",
    "dashboard_05_manka.html",
    "dashboard_06_kaden.html",
    "dashboard_07_plantoniq.html",
    "dashboard_08_recoup.html"
]

DASHBOARDS_DIR = os.path.join(os.path.dirname(__file__), "..", "pibep-2026", "dashboards")

def test_dashboards():
    if not os.path.isdir(DASHBOARDS_DIR):
        print(f"[FAIL] Diretório {DASHBOARDS_DIR} não existe.")
        sys.exit(1)

    errors = []
    for d in REQUIRED_DASHBOARDS:
        path = os.path.join(DASHBOARDS_DIR, d)
        if not os.path.isfile(path):
            errors.append(f"Arquivo ausente: {d}")
            continue

        with open(path, encoding="utf-8") as fp:
            content = fp.read()

        # Check return to hub link
        if '../index.html' not in content:
            errors.append(f"{d}: Falta link de retorno para '../index.html'")

        # Check team selector
        if 'id="teamSelector"' not in content and 'team-select' not in content:
            errors.append(f"{d}: Falta seletor de equipes (teamSelector)")

        # Check all 8 options in team selector
        for opt in REQUIRED_DASHBOARDS:
            if opt not in content:
                errors.append(f"{d}: Falta opção '{opt}' no seletor de equipes")

        # Check local PDF link
        if '../assets/pdfs/' not in content:
            errors.append(f"{d}: Falta link relativo '../assets/pdfs/' para o PDF local")

        # Check 4 tabs
        tabs = re.findall(r'data-tab=["\'](.*?)["\']', content)
        if len(tabs) < 4:
            errors.append(f"{d}: Encontradas apenas {len(tabs)} abas (esperado >= 4)")

    if errors:
        print("[FAIL] Erros encontrados nos dashboards:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"[PASS] Todos os {len(REQUIRED_DASHBOARDS)} dashboards validados com sucesso em {DASHBOARDS_DIR}!")

if __name__ == "__main__":
    test_dashboards()
