"""Genera una imagen base con Flux Pro o DALL-E.

Uso:
    python tools/imagenes/generar_imagen.py --prompt "frasco Invictus, luz cálida" \
        --modelo flux --salida memoria/campanas/.../imagenes/base.png
"""
import argparse
import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda *a, **k: None  # noqa: E731


def generar(prompt, modelo="flux", salida="base.png"):
    """Llama al proveedor de imágenes y guarda el resultado en `salida`."""
    if modelo == "flux" and not os.getenv("FLUX_API_KEY"):
        raise SystemExit("Falta FLUX_API_KEY en .env")
    if modelo == "dalle" and not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Falta OPENAI_API_KEY en .env")
    # TODO: implementar la llamada real al proveedor.
    print(f"[stub] generar imagen modelo={modelo} -> {salida}\n  prompt: {prompt}")
    return salida


def main():
    load_dotenv()
    p = argparse.ArgumentParser(description="Generar imagen")
    p.add_argument("--prompt", required=True)
    p.add_argument("--modelo", choices=["flux", "dalle"], default="flux")
    p.add_argument("--salida", default="base.png")
    args = p.parse_args()
    generar(args.prompt, args.modelo, args.salida)


if __name__ == "__main__":
    sys.exit(main())
