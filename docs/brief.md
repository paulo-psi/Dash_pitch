# Brief do Projeto: Dash_pitch

- **Data:** 2026-11-03
- **Arquétipo:** `software-app`
- **Stack:** HTML5, Tailwind CSS (v3.4 CDN), JavaScript Vanilla, GitHub Pages

## 1. Objetivo Central
Portal unificado e interativo dos Dashboards de Feedback dos Pitches PIBEP 2026 para publicação no GitHub Pages em link único e navegável para as equipes e avaliadores.

## 2. Escopo Concluído (MVP)
- [x] Download e validação dos 8 One-Pagers em PDF (`assets/pdfs/`).
- [x] Padronização dos 8 Dashboards interativos em `dashboards/` com barra de navegação global (Link para Hub + Seletor de Equipes) e caminhos relativos.
- [x] Desenvolvimento da Landing Page Hub (`index.html`) com contexto do Demoday, painel da banca avaliadora (4 jurados) e 8 cards de startups.
- [x] Bateria de testes automatizados (assets, dashboards, hub e navegação E2E com zero links 404).
- [x] Configuração de CI/CD para GitHub Pages (`.github/workflows/deploy.yml`) e manual de deploy no `README.md`.

## 3. Fora de Escopo (Non-Goals)
- Backend dinâmico, bancos de dados relacionais e alteração dos textos literais das avaliações da banca já consolidadas.

## 4. Critérios de Sucesso
- [x] Servidor estático local executando todos os fluxos com 100% de sucesso.
- [x] Navegação bidirecional fluida entre o Hub e todos os dashboards.
- [x] Repositório Git com commits atômicos por tarefa e preparado para push no GitHub Pro.
