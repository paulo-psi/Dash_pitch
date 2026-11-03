# Portal Multi-Demandas de Pitches & Demodays (Dash_pitch)

> **Plataforma web unificada no GitHub Pages para hospedagem de relatórios executivos, auditorias multimodais de pitches e dashboards de bancas avaliadoras de inovação e aceleração de startups.**

🌐 **Portal Geral no Ar:** [https://paulo-psi.github.io/Dash_pitch/](https://paulo-psi.github.io/Dash_pitch/)

---

## 🏛️ Arquitetura Multi-Demandas

O projeto foi estruturado para abrigar múltiplas demandas/edições independentes ao longo do tempo, mantendo o histórico de cada evento isolado em subpastas:

```text
Dash_pitch/
├── index.html                   # Master Hub (Catálogo de programas, edições e demandas)
│
├── pibep-2026/                  # [DEMANDA 1] Demoday PIBEP 2026 (PUCPR & SEBRAE/PR)
│   ├── index.html               # Hub do Demoday PIBEP 2026 (Banca, regras e os 8 cards)
│   ├── dashboards/              # 8 Dashboards interativos individuais c/ 4 abas completas
│   │   ├── dashboard_01_anchor.html
│   │   ├── dashboard_02_integremente.html
│   │   ├── dashboard_03_norman.html
│   │   ├── dashboard_04_nock.html
│   │   ├── dashboard_05_manka.html
│   │   ├── dashboard_06_kaden.html
│   │   ├── dashboard_07_plantoniq.html
│   │   └── dashboard_08_recoup.html
│   └── assets/
│       └── pdfs/                # Os 8 One-Pagers em PDF (download local imediato)
│           ├── Anchor.pdf
│           ├── IntegreMente.pdf
│           ├── Norman.pdf
│           ├── Nock.pdf
│           ├── MANKA.pdf
│           ├── Kaden.pdf
│           ├── PlantonIQ.pdf
│           └── RECOUP.pdf
│
├── <futura-demanda>/            # [DEMANDA 2+] Prontidão para novos programas e hackathons
│   └── ...
│
└── tests/                       # Bateria de testes de integridade e E2E automatizada
```

---

## 🔗 Links Oficiais — Demoday PIBEP 2026

- **Portal Central PIBEP 2026:**  
  [https://paulo-psi.github.io/Dash_pitch/pibep-2026/](https://paulo-psi.github.io/Dash_pitch/pibep-2026/)

- **Painéis Individuais das 8 Startups:**
  1. **Anchor:** [dashboard_01_anchor.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_01_anchor.html)
  2. **IntegreMente:** [dashboard_02_integremente.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_02_integremente.html)
  3. **Norman:** [dashboard_03_norman.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_03_norman.html)
  4. **Nock:** [dashboard_04_nock.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_04_nock.html)
  5. **Manka:** [dashboard_05_manka.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_05_manka.html)
  6. **Kaden:** [dashboard_06_kaden.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_06_kaden.html)
  7. **PlantonIQ:** [dashboard_07_plantoniq.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_07_plantoniq.html)
  8. **Recoup IA:** [dashboard_08_recoup.html](https://paulo-psi.github.io/Dash_pitch/pibep-2026/dashboards/dashboard_08_recoup.html)

---

## 🧪 Bateria de Testes Locais

```powershell
python tests/verify_assets.py
python tests/verify_dashboards.py
python tests/verify_hub.py
python tests/e2e_navigation_test.py
```
