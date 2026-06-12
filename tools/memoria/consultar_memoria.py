"""Busca en patrones + estrategias + métricas.

Uso:
    python tools/memoria/consultar_memoria.py --q "invictus"
    python tools/memoria/consultar_memoria.py --q "descuento" --fuente estrategias
"""
import argparse
import glob
import json
import os
import sys

PATRONES = os.path.join("memoria", "patrones", "patrones.json")
METRICAS = os.path.join("memoria", "metricas", "historico_metricas.json")
ESTRATEGIAS = os.path.join("memoria", "estrategias", "*.md")


def _buscar_json(path, q):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        datos = json.load(f)
    q = q.lower()
    return [d for d in datos if q in json.dumps(d, ensure_ascii=False).lower()]


def _buscar_md(q):
    q = q.lower()
    hits = []
    for path in glob.glob(ESTRATEGIAS):
        with open(path, encoding="utf-8") as f:
            texto = f.read()
        if q in texto.lower():
            hits.append(os.path.basename(path))
    return hits


def consultar(q, fuente="todo"):
    res = {}
    if fuente in ("todo", "patrones"):
        res["patrones"] = _buscar_json(PATRONES, q)
    if fuente in ("todo", "metricas"):
        res["metricas"] = _buscar_json(METRICAS, q)
    if fuente in ("todo", "estrategias"):
        res["estrategias"] = _buscar_md(q)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return res


def main():
    p = argparse.ArgumentParser(description="Consultar memoria")
    p.add_argument("--q", required=True)
    p.add_argument("--fuente", default="todo",
                   choices=["todo", "patrones", "metricas", "estrategias"])
    args = p.parse_args()
    consultar(args.q, args.fuente)


if __name__ == "__main__":
    sys.exit(main())
