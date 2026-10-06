# Demo · Cine Vinte × TaquillApp

Demo de una sola página de **TaquillApp para Empresas** con la marca de **Grupo Vinte**: un beneficio corporativo con el que los colaboradores consiguen folios y códigos de cine (Cinépolis y Cinemex) con **hasta 60% de descuento**.

## Cómo abrirla (offline)

Abre **`demo-vinte-taquillapp.html`** con doble clic en cualquier navegador. Es un solo archivo: logos, estilos y scripts van incrustados, así que no necesita internet ni servidor. Se puede mandar por correo o USB.

## Qué incluye

- Hero con el mensaje de "hasta 60% de descuento en cine"
- Cómo funciona, en 4 pasos
- Catálogo filtrable (Cinépolis / Cinemex · Boletos / Premium / Dulcería)
- Compra simulada: carrito → datos del colaborador → pago → folios generados (copiar / imprimir o guardar como PDF)
- Instrucciones de canje por cadena, beneficios para Vinte (RR.HH.) y preguntas frecuentes

> Los precios y códigos son **ilustrativos**. Ajusta el catálogo en `src/template.html` (constante `PRODUCTS`).

## Editar y regenerar

```bash
python3 build.py   # src/template.html + assets/ -> demo-vinte-taquillapp.html
```

Colores de marca: azul `#172843` (fondos y texto oscuro) y naranja `#D9912E` (logo y acentos).
