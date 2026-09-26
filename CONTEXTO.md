# Contexto del proyecto: Lili's (dulcería artesanal, Coquimbo)

Este archivo resume todo lo trabajado en sesiones anteriores para que cualquier sesión nueva pueda continuar sin perder contexto. Rama de trabajo: **`renato`**.

## La dueña y la marca
- La usuaria es la **dueña de Lili's** (Liliana Maier). Habla en español chileno, informal y directo. Responder en español, corto y concreto.
- **Lili's** = dulcería/chocolatería artesanal de la Región de Coquimbo, Chile. Nombres que aparecen: "Dulcería Lili's Artesanales", "Chocolatería Lili's By Maier Boutique", "Productos Artesanales Lili's" (Instagram @dulceria_lilis, ~6.300 seguidores, ~305 publicaciones).
- Sitio actual: https://lilis.cl (WordPress/WooCommerce con URLs `/categoria-producto/…`; también aparece una tienda Shopify "lilisecommerce" con `/products/…`, sin confirmar si es migración).
- Íconos de marca: **Faro Monumental de La Serena**, "La Región de las Estrellas", papaya y higos locales. Exportan a EE.UU. (Amazon).
- **Público objetivo: turistas** en Coquimbo / La Serena (chilenos y extranjeros).

### Datos reales (de buscadores, confirmar con la dueña)
- Tienda 1: Av. del Mar 3500, Local 116. Dom–Jue 10:00–20:00, Vie–Sáb 10:00–21:00.
- Tienda 2: Coquimbo, Av. Párroco Waldo Alcalde 401, Local 8. Lun–Sáb 10:30–20:30.
- Contacto: +56 9 6226 1712 · ventas@lilis.cl
- Productos: alfajores (papaya, higo, maicena, whisky, naranja, flow pack), cuchuflíes, galletas, golosinas (malvas de coco/chocolate, guagüitas, gomitas de fruta), frutas bañadas en chocolate (higos, papayitas), papayas confitadas, cajas de regalo y regalos corporativos.
- Menú que indicó la dueña: Inicio, Alfajores, Sweets (Dulces), Chocolates, Gift boxes (Cajas de regalo), Regalos corporativos.

## Estructura del repo
| Carpeta | Qué hay |
|---|---|
| `landing-page/` | Landing estática (`index.html` + `styles.css`). Estado actual abajo. |
| `disenos/empaque-alfajor-papaya/` | Rediseño de la cara frontal del empaque del Alfajor Blanco de Papaya (SVG a escala en mm, PNG, `generar.py`). |
| `info/`, `info/nutricion/`, `agentes/` | Carpetas vacías (solo README) para secciones futuras. |
| `.claude/skills/` + `.agents/skills/` | Skills de diseño instaladas (`Leonxlnx/taste-skill`): `design-taste-frontend`, `minimalist-ui`, `redesign-existing-projects`, `high-end-visual-design`, etc. |

Otras ramas: `landing-page`, `claude/epic-goldberg-nhuah1`, `info`, `info-nutricion`, `agentes` (históricas). **Seguir trabajando en `renato`.**

## Landing page (estado actual)
- Hecha con la skill `design-taste-frontend`: tipografía **Geist**, paleta neutra fría (#f4f4f2 / #161616) con **un solo acento frambuesa** (#b3325a; oscuro #e3739a), modo oscuro automático, radios: botones píldora y fotos 16px, sin em-dashes (—).
- Secciones: nav (Alfajores, Dulces, Chocolates, Cajas de regalo, Empresas, Tiendas + botón Comprar) → hero "Un recuerdo dulce de Coquimbo." → bento de productos (Alfajores grande, Dulces, Cuchuflíes, Chocolates, Galletas, Cajas de regalo ancho) → frase "Cada dulce lleva el sabor de una región de Chile." → Regalos corporativos (Cotizar) → Visítanos (2 tiendas + contacto) → cierre "Comprar" → footer.
- **Faltan fotos reales**: los cuadros `.ph` son placeholders con `<!-- TODO -->`. Hay que reemplazarlos por fotos (ver Magnific abajo).
- Pendiente: la dueña pidió que la marca sea **menos genérica** y que luzca más profesional; también se sugirió incluir el faro/estrellas en la web para coherencia con los empaques.
- Vista previa pública con marca de ejemplo (no se puede publicar con la marca real Lili's como artifact): https://claude.ai/artifact/A9z1UxMLsYtYJmUKaewrix — se genera desde `landing-page/` reemplazando la marca y los datos por ejemplos.

## Empaque Alfajor Blanco de Papaya
- Mantiene naranja, logo circular dorado, "Alfajor Premium", "La Región de las Estrellas", 65 g. Nuevo: Faro Monumental grande, constelaciones doradas, "RECUERDO DE COQUIMBO · CHILE", líneas en inglés.
- Sellos MINSAL (Ley 20.606): octágono negro, borde blanco, "ALTO EN …" + "Ministerio de Salud", 2,5 × 2,5 cm (cara 90 cm²). Azúcares + grasas saturadas; **confirmar si también lleva "calorías"**.
- Antes de imprimir: reemplazar el logo aproximado por el vector original; confirmar medidas del troquel.

## Generación de imágenes y video
### Magnific (conector principal, plan Premium, ~209.000 créditos al 26-09-2026)
- Proyecto en Magnific: **"Lili's - Papaya Confitadas"** (folderReference `67d3e1aa-caaf-4384-8860-0f1426a16d89`). Pasar siempre `folderReference` al generar.
- Costos de referencia: foto Nano Banana Pro 2K = 75; Seedream 5 Pro 2K = 100; quitar fondo = 3; logo a SVG = 150; upscale ×2 = 90–1.080; video Seedance 2.5 10 s 720p = 4.400, 1080p = 7.900 (8 s 1080p = 6.320); música 30 s = 150.
- Creaciones (identificadores para encadenar):
  - Foto original caja Papaya Confitadas: `jU2NGvZLD0`
  - 4 fotos pro 4:5: `XmkFrz8Bfo`, `5jNJimLKxe` (**Foto 2, la favorita**), `ksiyRvw16B`, `P3DWexY42C`
  - Toma vertical con **error** (texto de sistema incrustado arriba, no usar): `xSZ9zTmjfW` y su upscale `ksiy2aU16B`
  - Cuadro final fondo desenfocado + logo Lili's (salió bien): `fHUjOeVCDY`
  - Video 8 s 1080p 9:16 (mano toma la caja → fondo desenfocado → logo). **Empieza con el texto erróneo**: `WDCtFWRcXe`
  - Nuevas tomas verticales limpias para rehacer el video (esperando que la dueña elija A o B): A `LwA6C0BswO`, B `vQgrTyca47`
- **Siguiente paso pendiente**: la dueña elige A o B → regenerar el video Seedance 2.5 (start = A/B, end = `fHUjOeVCDY`, 9:16, cámara fija, sin música) en 1080p (6.320) o 720p (~3.500) para probar.
- Lección: **no usar `images_expand` (Ideogram)** para cambiar formato: incrustó texto de su prompt en la imagen. Usar Nano Banana Pro con referencias.

### Higgsfield (secundario, plan gratis, ~4,85 créditos)
- Solo sirve Z Image (0,15/imagen, baja calidad) y Wan 3.0 480p (≥4 créditos). La dueña **rechazó** la calidad de Z Image.
- Se generó un video Wan 3.0 de 5 s con la dueña sosteniendo el alfajor de papaya (ella dio consentimiento para usar su imagen).

## Limitaciones del entorno (importante)
- La red del entorno **bloquea**: lilis.cl, instagram.com, pikaso.cdnpk.net (archivos de Magnific), ak-data.magnific.com (subida directa a Magnific), d8j0ntlcm91z4.cloudfront.net y d2ol7oe51mr4n9.cloudfront.net (Higgsfield).
- Por eso **no se pueden ver ni descargar** las imágenes/videos generados; hay que pasar los links de Magnific (`webUrl`) y pedir capturas a la dueña.
- Truco para subir fotos locales a Magnific: subir a Higgsfield (`media_upload` → PUT a S3, que sí funciona) y luego `creations_upload_image` en Magnific con la URL pública de Higgsfield.
- La dueña quiere **ver todo dentro de Claude**. Solución pendiente: que agregue `pikaso.cdnpk.net` (y opcional `ak-data.magnific.com`) a Network access del entorno en claude.ai/code → entorno → Edit. Le costó encontrar el menú; ofrecer ayuda con capturas.

## Pendientes
1. Rehacer el video de Papaya Confitadas con la toma A o B.
2. Poner fotos reales en la landing (Foto 2 u otras) una vez que se puedan descargar.
3. Mejorar la landing: más profesional y con identidad propia (faro, estrellas), sin perder minimalismo.
4. Reverso del empaque del alfajor y versiones para otros sabores (higo, maicena, whisky, naranja).
5. Ideas de contenido para Instagram/Reels (ya se propusieron 10; favoritas: "lo que te tienes que llevar de Coquimbo", "así se hace un alfajor", ASMR del mordisco).
