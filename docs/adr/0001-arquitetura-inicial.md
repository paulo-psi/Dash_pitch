# ADR 0001: Estrutura e Arquitetura Inicial do Projeto

- **Data:** 2026-11-03
- **Status:** Aceito

## Contexto
O projeto **Dash_pitch** foi iniciado com o objetivo: *Portal unificado e interativo dos Dashboards de Feedback dos Pitches PIBEP 2026 para publicação no GitHub Pages*.

## Decisão
Adotar o arquétipo `software-app` dentro do padrão Governança V4.5 do Antigravity 2.0, utilizando a stack `HTML5, CSS3, JavaScript, Chart.js, GitHub Pages`.

## Consequências
- Memória persistente concentrada em `./docs/log.md` (seção Handoff Rápido).
- Snapshots locais isolados em `./_backup/` (fora do controle de versão Git).
