"""Búsqueda web de tendencias actualizadas.

Uso:
    python tools/web/buscar_tendencias.py --q "perfumes hombre verano 2026"
"""
import argparse
import sys


def buscar(q, limite=5):
    """Devuelve tendencias recientes para la consulta dada."""
    # TODO: integrar un proveedor de búsqueda web real.
    print(f"[stub] buscar tendencias q={q!r} limite={limite}")
    return []


def main():
    p = argparse.ArgumentParser(description="Buscar tendencias")
    p.add_argument("--q", required=True)
    p.add_argument("--limite", type=int, default=5)
    args = p.parse_args()
    buscar(args.q, args.limite)


if __name__ == "__main__":
    sys.exit(main())
