# Plan automatización con IA

> Mi viaje de cero a experto en automatización con IA, con la certificación
> Claude Certified Architect Foundations (CCA-F) como meta tangible.
> **18 meses · 78 semanas · 5-7 horas por semana.**

## Sobre este repositorio

Aquí vivirán los proyectos de código que voy construyendo durante mi plan
personal de aprendizaje. Cada proyecto irá en su propia subcarpeta, con
su `README`, sus tests y sus instrucciones de uso.

**Punto de partida:** ingeniero de sistemas con base en C, C++ y Java (J2EE/J2ME),
sin programar profesionalmente desde hace más de 10 años. Hoy en roles operativos
y comerciales en consultoría.

**Meta a 18 meses:** especialista vendible en automatización con IA, con
casos demostrables y la certificación CCA-F en mano.

## Plan en bloques

| Fase | Foco | Semanas | Estado |
|---|---|---|---|
| Setup | Entorno, cuentas IA, mentalidad | 1-2 | En curso |
| Fase 1 | Python para automatización | 3-10 | Pendiente |
| Fase 2 | APIs, webhooks y datos | 11-16 | Pendiente |
| Fase 3 | Claude API + prompt engineering | 17-26 | Pendiente |
| Fase 4 | n8n / Make / Zapier + IA | 27-36 | Pendiente |
| Fase 5 | Tool use, MCP y Claude Code | 37-48 | Pendiente |
| Fase 6 | RAG y agentes para automatización | 49-58 | Pendiente |
| Fase 7 | Evals, observabilidad, despliegue | 59-66 | Pendiente |
| Fase 8 | Preparación CCA-F | 67-70 | Pendiente |
| Fase 9 | Capstone y posicionamiento | 71-78 | Pendiente |

## Estructura

(Se irá llenando con cada proyecto del plan a medida que avance.)

## Stack al que apunto

- **Lenguaje:** Python idiomático moderno (`uv`, `ruff`, type hints, `pytest`).
- **LLMs:** familia Claude (Opus / Sonnet / Haiku) como principal · GPT como secundario.
- **APIs LLM:** Anthropic SDK, structured output, streaming, tool use, prompt caching.
- **Frameworks IA:** Claude Agent SDK, MCP cliente y servidor.
- **Editor / agente local:** Cursor + Claude Code.
- **Automatización:** n8n (principal), Make, Zapier, Playwright para RPA.
- **RAG:** embeddings (Voyage), pgvector + Supabase, hybrid search + reranking.
- **Backend ligero:** FastAPI, sqlmodel, Postgres / SQLite.
- **UI mínima:** Streamlit / Gradio.
- **Despliegue:** Render, Railway, GitHub Actions.
- **Evals y observabilidad:** Promptfoo, Langfuse, Helicone.

## Setup local

A medida que añada proyectos cada uno tendrá sus instrucciones específicas.
El stack base que asume todo el repo es:

- macOS o Linux.
- Python 3.13+ instalado vía `uv`.
- Git con SSH configurado.
- Variable de entorno `ANTHROPIC_API_KEY` disponible.

## Sobre el plan

El plan completo (cronograma semanal, recursos por fase, proyectos, mapeo a
los dominios del CCA-F) lo tengo en una hoja Excel personal fuera de este
repositorio. Aquí solo vive el resultado tangible: código, proyectos
y artefactos compartibles.

---

Plan diseñado y ejecutado con Claude (Anthropic) como tutor.
