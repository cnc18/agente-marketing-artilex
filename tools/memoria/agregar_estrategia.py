"""Procesa y guarda una estrategia externa en memoria/estrategias/.

Uso:
    python tools/memoria/agregar_estrategia.py --titulo "lanzamientos" \
        --archivo estrategias_destino.md --texto "..."
"""
import argparse
import os
import sys

DESTINO = os.path.join("memoria", "estrategias")


def agregar(titulo, archivo, texto):
    """Añade una sección de conocimiento externo a un .md de estrategias."""
    os.makedirs(DESTINO, exist_ok=True)
    path = os.path.join(DESTINO, archivo)
    bloque = f"\n## {titulo}\n\n{texto.strip()}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(bloque)
    print(f"[ok] estrategia '{titulo}' agregada a {path}")
    return path


def main():
    p = argparse.ArgumentParser(description="Agregar estrategia externa")
    p.add_argument("--titulo", required=True)
    p.add_argument("--archivo", required=True, help="ej. tipos_oferta.md")
    p.add_argument("--texto", required=True)
    args = p.parse_args()
    agregar(args.titulo, args.archivo, args.texto)


if __name__ == "__main__":
    sys.exit(main())
