"""Redimensiona/recorta una imagen para cada red usando Pillow.

Formatos: instagram (4:5, 9:16), tiktok (9:16), facebook (1:1, 4:5).

Uso:
    python tools/imagenes/adaptar_formato.py --entrada base.png --red instagram
"""
import argparse
import sys

try:
    from PIL import Image
except ImportError:
    Image = None

RATIOS = {
    "instagram": (4, 5),
    "instagram_story": (9, 16),
    "tiktok": (9, 16),
    "facebook": (1, 1),
}


def adaptar(entrada, red, salida=None):
    """Recorta la imagen al ratio de la red indicada."""
    if red not in RATIOS:
        raise SystemExit(f"Red no soportada: {red}. Opciones: {list(RATIOS)}")
    salida = salida or entrada.replace(".", f"_{red}.")
    if Image is None:
        print(f"[stub] (Pillow no instalado) {entrada} -> {salida} ratio={RATIOS[red]}")
        return salida
    # TODO: recorte centrado real al ratio objetivo.
    print(f"[stub] adaptar {entrada} -> {salida} ratio={RATIOS[red]}")
    return salida


def main():
    p = argparse.ArgumentParser(description="Adaptar formato por red")
    p.add_argument("--entrada", required=True)
    p.add_argument("--red", required=True, choices=list(RATIOS))
    p.add_argument("--salida")
    args = p.parse_args()
    adaptar(args.entrada, args.red, args.salida)


if __name__ == "__main__":
    sys.exit(main())
