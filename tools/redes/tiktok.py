"""TikTok: sube un borrador y lee métricas (TikTok API).

Uso:
    python tools/redes/tiktok.py publicar --video v.mp4 --copy "..."
    python tools/redes/tiktok.py metricas --post-id 123
"""
import argparse
import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = lambda *a, **k: None  # noqa: E731


def publicar(video, copy):
    if not os.getenv("TIKTOK_ACCESS_TOKEN"):
        raise SystemExit("Falta TIKTOK_ACCESS_TOKEN en .env")
    # TODO: subir vídeo como borrador.
    print(f"[stub] TikTok publicar video={video} copy={copy[:40]!r}...")
    return {"status": "borrador"}


def metricas(post_id):
    # TODO: GET métricas del vídeo.
    print(f"[stub] TikTok métricas post_id={post_id}")
    return {}


def main():
    load_dotenv()
    p = argparse.ArgumentParser(description="TikTok")
    sub = p.add_subparsers(dest="cmd", required=True)
    pub = sub.add_parser("publicar")
    pub.add_argument("--video", required=True)
    pub.add_argument("--copy", required=True)
    met = sub.add_parser("metricas")
    met.add_argument("--post-id", required=True)
    args = p.parse_args()
    if args.cmd == "publicar":
        publicar(args.video, args.copy)
    else:
        metricas(args.post_id)


if __name__ == "__main__":
    sys.exit(main())
