import os
import sys

INDEX_PATH = os.path.join(os.path.dirname(__file__), "..", "index.html")

REQUIRED_DASHBOARDS = [
    "./dashboards/dashboard_01_anchor.html",
    "./dashboards/dashboard_02_integremente.html",
    "./dashboards/dashboard_03_norman.html",
    "./dashboards/dashboard_04_nock.html",
    "./dashboards/dashboard_05_manka.html",
    "./dashboards/dashboard_06_kaden.html",
    "./dashboards/dashboard_07_plantoniq.html",
    "./dashboards/dashboard_08_recoup.html"
]

REQUIRED_JURORS = [
    "Daucio",
    "Liliane",
    "Gustavo Russi",
    "Bruno"
]

REQUIRED_TERMS = [
    "Demoday PIBEP 2026",
    "PUCPR",
    "SEBRAE",
    "Banca Avaliadora",
    "8 Startups"
]

def test_hub():
    if not os.path.isfile(INDEX_PATH):
        print(f"[FAIL] Arquivo {INDEX_PATH} não existe.")
        sys.exit(1)

    with open(INDEX_PATH, encoding="utf-8") as fp:
        content = fp.read()

    errors = []
    # Check required terms
    for term in REQUIRED_TERMS:
        if term.lower() not in content.lower():
            errors.append(f"Termo essencial não encontrado: '{term}'")

    # Check required jurors
    for juror in REQUIRED_JURORS:
        if juror.lower() not in content.lower():
            errors.append(f"Jurado da banca não encontrado: '{juror}'")

    # Check dashboard links
    for d in REQUIRED_DASHBOARDS:
        if d not in content and d.replace('./', '') not in content:
            errors.append(f"Link para dashboard não encontrado: '{d}'")

    if errors:
        print("[FAIL] Erros encontrados no Hub Central (index.html):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print(f"[PASS] Hub Central (index.html) validado com sucesso! Contém todos os {len(REQUIRED_DASHBOARDS)} cards e os 4 jurados.")

if __name__ == "__main__":
    test_hub()
