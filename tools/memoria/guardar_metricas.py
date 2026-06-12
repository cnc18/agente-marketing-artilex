"""Agrega las métricas de una campaña al histórico acumulativo.

Uso:
    python tools/memoria/guardar_metricas.py --campana invictus_finde \
        --json '{"alcance": 12000, "ventas": 34}'
"""
import argparse
import json
import os
import sys

HISTORICO = os.path.join("memoria", "metricas", "historico_metricas.json")


def cargar(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def guardar(campana, metricas):
    """Añade las métricas al histórico sin sobrescribir."""
    datos = cargar(HISTORICO)
    datos.append({"campana": campana, **metricas})
    os.makedirs(os.path.dirname(HISTORICO), exist_ok=True)
    with open(HISTORICO, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"[ok] métricas guardadas para {campana} ({len(datos)} registros)")
    return datos[-1]


def main():
    p = argparse.ArgumentParser(description="Guardar métricas")
    p.add_argument("--campana", required=True)
    p.add_argument("--json", required=True, help="métricas en formato JSON")
    args = p.parse_args()
    guardar(args.campana, json.loads(args.json))


if __name__ == "__main__":
    sys.exit(main())
