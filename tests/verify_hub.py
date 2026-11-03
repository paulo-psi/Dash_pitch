import os
import sys

MASTER_HUB = os.path.join(os.path.dirname(__file__), "..", "index.html")
PIBEP_HUB = os.path.join(os.path.dirname(__file__), "..", "pibep-2026", "index.html")

def test_hubs():
    for name, path in [("Master Hub", MASTER_HUB), ("PIBEP Hub", PIBEP_HUB)]:
        if not os.path.isfile(path):
            print(f"[FAIL] {name} ({path}) não existe.")
            sys.exit(1)

    # Verifica Master Hub
    with open(MASTER_HUB, encoding="utf-8") as fp:
        master_content = fp.read()
    if "./pibep-2026/index.html" not in master_content and "pibep-2026" not in master_content:
        print("[FAIL] Master Hub não conecta ao PIBEP 2026.")
        sys.exit(1)

    # Verifica PIBEP Hub
    with open(PIBEP_HUB, encoding="utf-8") as fp:
        pibep_content = fp.read()
    if "Demoday PIBEP 2026" not in pibep_content:
        print("[FAIL] PIBEP Hub não contém título do evento.")
        sys.exit(1)

    print("[PASS] Ambos os portais (Master Hub e PIBEP Hub) validados com sucesso!")

if __name__ == "__main__":
    test_hubs()
