# Dash_pitch: Portal Hub & Dashboards Executivos Demoday PIBEP 2026 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir e publicar um portal web estático, integrado e responsivo no GitHub Pages contendo uma Landing Page Hub central (`index.html`), os 8 dashboards interativos individuais com navegação unificada e os One-Pagers em PDF para acesso das equipes e avaliadores.

**Architecture:** Abordagem multi-página estática (Opção A): Uma Landing Page Hub na raiz (`index.html`) apresenta o panorama geral do Demoday PIBEP 2026 e os 8 cards das startups; cada card conecta à sua página dedicada em `dashboards/` contendo o dashboard interativo completo (4 abas) e um cabeçalho global integrado com botão de retorno e seletor rápido entre equipes. Os 8 PDFs de apoio ficam hospedados localmente em `assets/pdfs/` para download direto sem dependência de permissões do Google Drive.

**Tech Stack:** HTML5 semântico, Tailwind CSS (v3.4 CDN), Google Fonts (Inter), JavaScript Vanilla (Tabs, Selector e Impressão), GitHub Pages (deploy via GitHub Actions).

**Spec:** Baseado na auditoria das fontes primárias documentadas em `raw_drive/00_Plano_Diretor_Auditoria_e_Dashboards_PIBEP_2026.md` e `raw_drive/00_Relatorio_Geral_Execucao_Como_Foi_Feito_PIBEP_2026.md`.

---

## Global Constraints

- **Padrão de Links Relativos:** Todos os links internos e referências de assets DEVEM ser relativos (`./`, `../`) para garantir funcionamento perfeito em subdiretórios do GitHub Pages (`https://<username>.github.io/<repo>/`).
- **Codificação UTF-8:** Todos os arquivos HTML e scripts gerados devem ter encoding UTF-8 estrito sem BOM, prevenindo mojibake.
- **Zero Build Tooling:** Aplicação estática pura (HTML + JS Vanilla + Tailwind CDN), dispensando Node.js, Webpack ou Vite para facilitar manutenção e deploy instantâneo.
- **Trava de Sigilo e Autonomia:** Cada dashboard individual deve funcionar perfeitamente isolado caso a coordenação deseje enviar apenas o link direto da equipe (`/dashboards/dashboard_01_anchor.html`).
- **Trava Absoluta de Planos:** Nenhuma tarefa deste plano pode ser executada antes da aprovação explícita do Paulo no chat.

---

## Review Focus

1. **Quebra de caminhos no GitHub Pages em subcaminho:** Links com barra inicial absoluta (`/assets/...`) falham no GitHub Pages quando hospedados em repositório de projeto (`/Dash_pitch/`). *Prevenção: Usar estritamente caminhos relativos `./assets/` e `../assets/`.*
2. **Navegação mobile colapsada:** Dropdown de alternância de equipes ou abas horizontais estourarem a largura em smartphones (< 375px). *Prevenção: Menus responsivos com flex-wrap/scroll lateral e botões touch-friendly (mínimo 44px de altura).*
3. **Estado de aba inválida ou ausente:** Se o usuário clicar em link ou recarregar, a aba primária (Devolutiva da Banca) deve sempre abrir visível por padrão, com as demais abas em `hidden`.
4. **Fallback de links do Google Drive:** Caso algum PDF local não seja baixado ou o usuário queira abrir no Google Drive, preservar o link do Drive original como alternativa secundária.
5. **Erros de console silenciosos:** Scripts de troca de abas e seletor rápido devem ter verificações defensivas (`if (elem)`) para não lançar exceções não tratadas no console do navegador.

---

## Task Structure

### Task 1: Download e Organização dos One-Pagers em PDF (`assets/pdfs/`)
- [x] **Step 1: Escrever teste de verificação de integridade dos PDFs** (`tests/verify_assets.py`)
- [x] **Step 2: Executar teste para verificar falha inicial** (FAIL confirmado)
- [x] **Step 3: Baixar os 8 arquivos PDF via CLI `gdrive readonly download`**
- [x] **Step 4: Executar teste de verificação de integridade** (PASS - 8 PDFs validados)
- [x] **Step 5: Commit Git** (`5bb46db`)

### Task 2: Padronização e Enriquecimento dos 8 Dashboards com Navegação Global (`dashboards/`)
- [x] **Step 1: Escrever teste de validação dos dashboards** (`tests/verify_dashboards.py`)
- [x] **Step 2: Executar teste para verificar falha inicial** (FAIL confirmado)
- [x] **Step 3: Copiar e injetar a barra de navegação global nos 8 dashboards**
- [x] **Step 4: Executar teste de validação dos dashboards** (PASS - 8 dashboards validados)
- [x] **Step 5: Commit Git** (`28e087a`)

### Task 3: Construção da Landing Page Hub Central (`index.html`)
- [x] **Step 1: Escrever teste para o Hub Central** (`tests/verify_hub.py`)
- [x] **Step 2: Executar teste para verificar falha inicial** (FAIL confirmado)
- [x] **Step 3: Implementar `index.html`** (Hero, KPIs, 4 Jurados, 8 Cards responsivos)
- [x] **Step 4: Executar teste para validar `index.html`** (PASS)
- [x] **Step 5: Commit Git** (`a9b365f`)

### Task 4: Bateria de Testes E2E e Verificação Visual Integrada
- [x] **Step 1: Implementar script de teste E2E com servidor local HTTP** (`tests/e2e_navigation_test.py`)
- [x] **Step 2: Executar bateria de testes E2E** (PASS - 17 URLs verificadas, zero links 404)
- [x] **Step 3: Registrar resultados no log do projeto** (`docs/log.md`)
- [x] **Step 4: Commit Git** (`047ccb0`)

### Task 5: Configuração do GitHub Pages, Workflow de CI/CD e Manual de Publicação
- [x] **Step 1: Criar GitHub Action `.github/workflows/deploy.yml`**
- [x] **Step 2: Atualizar `README.md` com Guia Passo a Passo para o Paulo**
- [x] **Step 3: Atualizar `docs/brief.md` e `docs/log.md` com status final**
- [x] **Step 4: Commit Git final da fase de estruturação**
