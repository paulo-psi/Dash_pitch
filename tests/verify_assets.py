import os
import sys

REQUIRED_PDFS = [
    "Anchor.pdf",
    "IntegreMente.pdf",
    "Norman.pdf",
    "Nock.pdf",
    "MANKA.pdf",
    "Kaden.pdf",
    "PlantonIQ.pdf",
    "RECOUP.pdf"
]

TARGET_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "pdfs")

def test_assets():
    if not os.path.isdir(TARGET_DIR):
        print(f"[FAIL] Diretório {TARGET_DIR} não existe.")
        sys.exit(1)

    missing = []
    too_small = []
    for pdf in REQUIRED_PDFS:
        path = os.path.join(TARGET_DIR, pdf)
        if not os.path.isfile(path):
            missing.append(pdf)
        else:
            size_kb = os.path.getsize(path) / 1024
            if size_kb < 50:
                too_small.append(f"{pdf} ({size_kb:.1f} KB)")

    if missing:
        print(f"[FAIL] PDFs ausentes: {missing}")
        sys.exit(1)
    if too_small:
        print(f"[FAIL] PDFs muito pequenos / corrompidos: {too_small}")
        sys.exit(1)

    print(f"[PASS] Todos os {len(REQUIRED_PDFS)} PDFs estão presentes e válidos em {TARGET_DIR}!")
    for pdf in REQUIRED_PDFS:
        size_kb = os.path.getsize(os.path.join(TARGET_DIR, pdf)) / 1024
        print(f"  - {pdf}: {size_kb:.1f} KB")

if __name__ == "__main__":
    test_assets()
