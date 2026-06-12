"""Guarda un patrón estructurado tras una campaña (acumulativo).

Nunca reemplaza: añade al array de patrones.json.

Uso:
    python tools/memoria/guardar_patron.py --campana invictus_finde \
        --json '{"angulo": "perfume del finde", "resultado": "bueno"}'
"""
import argparse
import json
import os
import sys

PATRONES = os.path.join("memoria", "patrones", "patrones.json")


def cargar(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def guardar(campana, patron):
    """Añade un patrón al histórico sin sobrescribir lo anterior."""
    datos = cargar(PATRONES)
    entrada = {"campana": campana, **patron}
    datos.append(entrada)
    os.makedirs(os.path.dirname(PATRONES), exist_ok=True)
    with open(PATRONES, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"[ok] patrón guardado para {campana} ({len(datos)} en total)")
    return entrada


def main():
    p = argparse.ArgumentParser(description="Guardar patrón")
    p.add_argument("--campana", required=True)
    p.add_argument("--json", required=True, help="patrón en formato JSON")
    args = p.parse_args()
    guardar(args.campana, json.loads(args.json))


if __name__ == "__main__":
    sys.exit(main())
