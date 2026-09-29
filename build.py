#!/usr/bin/env python3
"""Genera la demo autocontenida (funciona offline): incrusta los logos en base64."""
import base64, pathlib

root = pathlib.Path(__file__).parent
def data_uri(name, mime):
    return f"data:{mime};base64," + base64.b64encode((root / "assets" / name).read_bytes()).decode()

html = (root / "src" / "template.html").read_text(encoding="utf-8")
html = (html.replace("{{LOGO_BLANCO}}", data_uri("logo-vinte-blanco.webp", "image/webp"))
            .replace("{{ICONO}}", data_uri("icono-vinte.png", "image/png")))
out = root / "demo-vinte-taquillapp.html"
out.write_text(html, encoding="utf-8")
print(f"OK -> {out.name} ({out.stat().st_size // 1024} KB)")
