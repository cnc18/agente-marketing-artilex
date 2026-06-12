# Agente de Marketing

Agente autónomo y recursivo para campañas de perfumería de lujo. Diseña, ejecuta
y aprende de cada campaña.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env          # y rellena tus claves
```

## Cómo usar

El agente trabaja con un flujo de 7 pasos descrito en `CLAUDE.md`. Cada paso
combina **conocimiento** (`skills/`) y **acciones** (`tools/`), y deja rastro en
`memoria/`.

| Comando            | Qué hace                                        |
|--------------------|-------------------------------------------------|
| `/recon <prod>`    | Inteligencia de mercado y producto              |
| `/campaña <prod>`  | Ejecuta el flujo completo de 7 pasos            |
| `/metricas <camp>` | Lee métricas de las redes y las guarda          |
| `/memoria <q>`     | Consulta patrones, estrategias y métricas       |

## Árbol de carpetas

```
agente-marketing/
├── CLAUDE.md              # metodología, reglas, flujo de 7 pasos
├── skills/                # conocimiento modular (cómo hacer cada cosa)
├── tools/                 # scripts ejecutables (crm, imagenes, redes, memoria, web)
├── memoria/               # memoria recursiva (patrones, métricas, estrategias, campañas)
├── datos/                 # archivos que subes tú (no va a git)
├── .env                   # claves (no va a git)
└── requirements.txt
```

## Memoria recursiva

- `memoria/patrones/patrones.json` — lo que funcionó en TUS campañas (acumulativo).
- `memoria/metricas/historico_metricas.json` — métricas por campaña (acumulativo).
- `memoria/estrategias/` — conocimiento externo de la industria, ya procesado.
- `memoria/campanas/<año>/<mes>/<campaña>/` — archivo histórico de cada campaña.
