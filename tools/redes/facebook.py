"""Facebook: sube un borrador y lee métricas (Meta Graph API).

Uso:
    python tools/redes/facebook.py publicar --imagen img.png --copy "..."
    python tools/redes/facebook.py metricas --post-id 123
"""
import argparse
import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda *a, **k: None  # noqa: E731


def publicar(imagen, copy):
    if not os.getenv("META_ACCESS_TOKEN"):
        raise SystemExit("Falta META_ACCESS_TOKEN en .env")
    # TODO: publicar en la página como borrador.
    print(f"[stub] FB publicar imagen={imagen} copy={copy[:40]!r}...")
    return {"status": "borrador"}


def metricas(post_id):
    # TODO: GET insights del post.
    print(f"[stub] FB métricas post_id={post_id}")
    return {}


def main():
    load_dotenv()
    p = argparse.ArgumentParser(description="Facebook")
    sub = p.add_subparsers(dest="cmd", required=True)
    pub = sub.add_parser("publicar")
    pub.add_argument("--imagen", required=True)
    pub.add_argument("--copy", required=True)
    met = sub.add_parser("metricas")
    met.add_argument("--post-id", required=True)
    args = p.parse_args()
    if args.cmd == "publicar":
        publicar(args.imagen, args.copy)
    else:
        metricas(args.post_id)


if __name__ == "__main__":
    sys.exit(main())
