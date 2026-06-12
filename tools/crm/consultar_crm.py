"""GET de productos, stock, costos y estadísticas desde el CRM.

Uso:
    python tools/crm/consultar_crm.py --producto "Invictus"
    python tools/crm/consultar_crm.py --sku 12345 --stats
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


def consultar(producto=None, sku=None, stats=False):
    """Devuelve datos del producto: stock, costo, precio, ventas."""
    base = os.getenv("CRM_BASE_URL")
    key = os.getenv("CRM_API_KEY")
    if not base or not key:
        raise SystemExit("Falta CRM_BASE_URL o CRM_API_KEY en .env")
    # TODO: implementar la llamada real al CRM.
    params = {"producto": producto, "sku": sku, "stats": stats}
    print(f"[stub] GET {base}/productos params={params}")
    return {}


def main():
    load_dotenv()
    p = argparse.ArgumentParser(description="Consultar el CRM")
    p.add_argument("--producto")
    p.add_argument("--sku")
    p.add_argument("--stats", action="store_true")
    args = p.parse_args()
    consultar(args.producto, args.sku, args.stats)


if __name__ == "__main__":
    sys.exit(main())
