"""POST de una oferta al CRM, con validación de margen.

REGLA DE ORO: si el margen cae por debajo del mínimo, la oferta se RECHAZA.

Uso:
    python tools/crm/crear_oferta.py --sku 12345 --precio 79.0 --margen-min 0.35
"""
import argparse
import os
import sys

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    requests = None
    load_dotenv = lambda *a, **k: None  # noqa: E731


def margen(precio_oferta, costo):
    return (precio_oferta - costo) / precio_oferta if precio_oferta else -1


def crear_oferta(sku, precio_oferta, costo, margen_min=0.35):
    """Valida el margen y, si pasa, registra la oferta en el CRM."""
    m = margen(precio_oferta, costo)
    if m < margen_min:
        raise SystemExit(
            f"RECHAZADA: margen {m:.1%} < mínimo {margen_min:.1%}. "
            "Sube el precio o cambia el tipo de oferta."
        )
    base = os.getenv("CRM_BASE_URL")
    # TODO: implementar el POST real al CRM.
    print(f"[stub] POST {base}/ofertas sku={sku} precio={precio_oferta} margen={m:.1%}")
    return {"sku": sku, "precio": precio_oferta, "margen": m}


def main():
    load_dotenv()
    p = argparse.ArgumentParser(description="Crear oferta en el CRM")
    p.add_argument("--sku", required=True)
    p.add_argument("--precio", type=float, required=True)
    p.add_argument("--costo", type=float, required=True)
    p.add_argument("--margen-min", type=float, default=0.35)
    args = p.parse_args()
    crear_oferta(args.sku, args.precio, args.costo, args.margen_min)


if __name__ == "__main__":
    sys.exit(main())
