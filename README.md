# Portal Executivo Demoday PIBEP 2026 (PUCPR & SEBRAE/PR)

> **Portal web unificado e dashboards interativos com a devolutiva oficial da banca avaliadora, transcrição auditada dos pitches e materiais de apoio das 8 startups do PIBEP 16.**

🌐 **Site no Ar (GitHub Pages):** [https://paulo-psi.github.io/Dash_pitch/](https://paulo-psi.github.io/Dash_pitch/)

---

## 🎯 Links de Acesso Direto para as Equipes

- **Hub Geral (Visão Completa da Banca e Startups):**
  [https://paulo-psi.github.io/Dash_pitch/](https://paulo-psi.github.io/Dash_pitch/)

- **Painéis Individuais de Devolutiva (Com Sigilo e Foco por Equipe):**
  1. **Anchor:** [dashboard_01_anchor.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_01_anchor.html)
  2. **IntegreMente:** [dashboard_02_integremente.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_02_integremente.html)
  3. **Norman:** [dashboard_03_norman.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_03_norman.html)
  4. **Nock:** [dashboard_04_nock.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_04_nock.html)
  5. **Manka:** [dashboard_05_manka.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_05_manka.html)
  6. **Kaden:** [dashboard_06_kaden.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_06_kaden.html)
  7. **PlantonIQ:** [dashboard_07_plantoniq.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_07_plantoniq.html)
  8. **Recoup IA:** [dashboard_08_recoup.html](https://paulo-psi.github.io/Dash_pitch/dashboards/dashboard_08_recoup.html)

---

## 📁 Estrutura do Repositório

```text
Dash_pitch/
├── index.html                   # Hub Executivo Central (Panorama da banca, regras e os 8 cards)
├── dashboards/                  # 8 Páginas dedicadas por equipe com navegação global
│   ├── dashboard_01_anchor.html
│   ├── dashboard_02_integremente.html
│   ├── dashboard_03_norman.html
│   ├── dashboard_04_nock.html
│   ├── dashboard_05_manka.html
│   ├── dashboard_06_kaden.html
│   ├── dashboard_07_plantoniq.html
│   └── dashboard_08_recoup.html
├── assets/
│   └── pdfs/                    # Os 8 One-Pagers em PDF (download local instantâneo)
│       ├── Anchor.pdf
│       ├── IntegreMente.pdf
│       ├── Norman.pdf
│       ├── Nock.pdf
│       ├── MANKA.pdf
│       ├── Kaden.pdf
│       ├── PlantonIQ.pdf
│       └── RECOUP.pdf
└── tests/                       # Bateria de testes de integridade e E2E
    ├── verify_assets.py
    ├── verify_dashboards.py
    ├── verify_hub.py
    └── e2e_navigation_test.py
```

---

## 🧪 Auditoria de Qualidade e Testes

- **Auditoria Profunda via Playwright:** Inspecionado em 3 viewports (`1440x900`, `1366x768`, `375x812`).
- **IDs Órfãos:** 0.
- **Links Quebrados:** 0.
- **Overflows de Layout:** 0 (responsividade mobile-first validada).
- **Testes E2E Locais:** `python tests/e2e_navigation_test.py` (17 URLs testadas com status 200).
- **Publicação:** GitHub Pages nativo a partir da branch `main` (`/`).
