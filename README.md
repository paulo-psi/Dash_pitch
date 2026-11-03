# Portal Executivo Demoday PIBEP 2026 (PUCPR & SEBRAE/PR)

> **Portal web unificado e dashboards interativos com a devolutiva oficial da banca avaliadora, transcrição auditada dos pitches e materiais de apoio das 8 startups do PIBEP 16.**

---

## 🎯 Visão Geral da Arquitetura (Opção A)

O projeto foi construído para ser hospedado no **GitHub Pages** (GitHub Pro) em um link único e compartilhável para a coordenação, avaliadores e equipes:

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
├── tests/                       # Bateria de testes de integridade e E2E
│   ├── verify_assets.py
│   ├── verify_dashboards.py
│   ├── verify_hub.py
│   └── e2e_navigation_test.py
└── .github/workflows/
    └── deploy.yml               # Workflow oficial de deploy contínuo no GitHub Pages
```

---

## 🚀 Como Publicar no GitHub Pages (GitHub Pro)

### 1. Criar o Repositório no GitHub
Você pode criar via terminal com o GitHub CLI (`gh`) ou direto pelo navegador:

```powershell
# Via GitHub CLI (se autenticado):
gh repo create Dash_pitch --public --source=. --remote=origin --push

# OU se criar manualmente pelo site (https://github.com/new):
git remote add origin https://github.com/<seu-usuario-github>/Dash_pitch.git
git branch -M main
git push -u origin main
```

### 2. Ativar o GitHub Pages no Repositório
1. No seu repositório no GitHub, clique em **Settings** > **Pages** (no menu lateral esquerdo).
2. Em **Build and deployment > Source**, selecione:
   - **GitHub Actions** (Recomendado — o workflow `.github/workflows/deploy.yml` será executado automaticamente a cada push).
3. Aguarde cerca de 1 a 2 minutos até o workflow finalizar.
4. Seu portal estará no ar em:
   ```text
   https://<seu-usuario-github>.github.io/Dash_pitch/
   ```

---

## 🔗 Compartilhamento com as Equipes

- **Link Geral (Hub Central):**
  `https://<seu-usuario-github>.github.io/Dash_pitch/`
- **Links Diretos por Equipe (Sigilo e Foco na Devolutiva):**
  - Anchor: `.../Dash_pitch/dashboards/dashboard_01_anchor.html`
  - IntegreMente: `.../Dash_pitch/dashboards/dashboard_02_integremente.html`
  - Norman: `.../Dash_pitch/dashboards/dashboard_03_norman.html`
  - Nock: `.../Dash_pitch/dashboards/dashboard_04_nock.html`
  - Manka: `.../Dash_pitch/dashboards/dashboard_05_manka.html`
  - Kaden: `.../Dash_pitch/dashboards/dashboard_06_kaden.html`
  - PlantonIQ: `.../Dash_pitch/dashboards/dashboard_07_plantoniq.html`
  - Recoup: `.../Dash_pitch/dashboards/dashboard_08_recoup.html`

---

## 🧪 Verificação e Testes Locais

Para rodar a bateria de testes e simular o servidor HTTP antes do deploy:

```powershell
# Teste de integridade dos PDFs
python tests/verify_assets.py

# Teste de integridade dos 8 dashboards e navegação
python tests/verify_dashboards.py

# Teste da Landing Page Hub
python tests/verify_hub.py

# Bateria End-to-End completa (servidor HTTP local em porta 8923)
python tests/e2e_navigation_test.py
```
