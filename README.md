# Greccio: un Belén para ti · Navidad 2026

Felicitación de Navidad interactiva de la **Parroquia del Cristo de la Paz** (Franciscanos · C/ Portalegre, 8 · Carabanchel, Madrid), hermana de «Una buena noticia para ti». La carta sale de **Greccio**, donde San Francisco de Asís hizo el primer Belén en la Nochebuena de 1223, cruza el Mediterráneo y llega a la parroquia.

Web: https://fjpereirag.github.io/greccio/

## Cómo funciona

1. Se comparte el enlace. La portada, con el botón «Recibir la carta», pone en marcha la música.
2. La carta sale de Greccio sobre el mapa 3D de Italia, da el salto a España y llega a Madrid, a Carabanchel (botón «Saltar» para ir directo).
3. Se rompe el lacre (la Tau franciscana) y se abre el carrusel con los frescos de Giotto. Cada frase aparece palabra a palabra mientras la lee la voz de Álvaro.
4. Al final, «Feliz Navidad · Te esperamos» y el botón **Reenviar por WhatsApp**.

El texto de la carta está en `app.js`, en la lista `CARTA_BELEN`.

## La voz de Álvaro

Las voces se generan con `voz_greccio.py` (edge-tts, voz es-ES-AlvaroNeural) y se guardan en `audio/greccio_00.mp3` … `greccio_14.mp3`. Para crearlas: `pip install edge-tts` y `python voz_greccio.py` desde esta carpeta. Ya están incluidas. Si falta alguna, la web funciona igual: las palabras aparecen a su ritmo, sin voz.

## Imágenes

| Archivo | Imagen |
|---|---|
| `img/giotto-greccio.jpg` | Giotto, El pesebre de Greccio |
| `img/giotto-renuncia.jpg` | Giotto, La renuncia a los bienes |
| `img/giotto-manto.jpg` | Giotto, San Francisco da su manto a un caballero pobre |
| `img/giotto-sandamian.jpg` | Giotto, San Francisco ora ante el crucifijo de San Damián |
| `img/giotto-pajaros.jpg` | Giotto, La predicación a los pájaros |
| `img/parroquia.jpg` | Foto de la Parroquia del Cristo de la Paz (pantalla final) |
| `img/felicitacion-2026.jpg` | Felicitación «¡Feliz Navidad 2026!», última tarjeta de la carta |

Los frescos están recortados a 9:16 para las tarjetas y llevan un pie con su título («Giotto · … · Asís»), definido en `app.js` (lista `PIE`).

## Cómo publicarla

1. En GitHub, crea un repositorio público llamado **greccio**.
2. Sube todo el contenido de esta carpeta («Add file → Upload files»).
3. En *Settings → Pages*: *Deploy from a branch*, rama `main`, carpeta `/ (root)`.
4. Estará en `https://fjpereirag.github.io/greccio/`.

Si usas otro nombre de repositorio, cambia `og:image` y `og:url` en `index.html`.

## Enlace de cada carta

`…/greccio/?para=Carmen&de=Fj&m=1&e=1&n=Me%20acuerdo%20de%20ti` · para escribir una: `…/greccio/?escribir`

| Parámetro | Qué es |
|---|---|
| `para`, `de` | Nombres (máx. 30 caracteres) |
| `m` | Palabras: 1 un pequeño Greccio · 2 el Señor te dé la paz · 3 pobreza con alegría · 4 se hizo pequeño |
| `e` | Fresco: 1 Greccio · 2 el manto · 3 San Damián · 4 los pájaros |
| `n` | Nota personal (opcional, máx. 140) |

## Fuentes de las frases

- Tomás de Celano, *Vida primera*, 84-86 (Greccio) y *Vida segunda*, 199-200 (la Navidad de Francisco).
- San Francisco, *Carta a todos los fieles* («siendo rico, quiso escoger la pobreza»), *Testamento* («El Señor te dé la paz») y *Admoniciones*, 27.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html`, `estilo.css`, `app.js` | La web |
| `vendor/three.min.js` | Three.js (licencia MIT) |
| `assets/terreno-italia.jpg`, `assets/altura-italia.js` | Relieve ilustrado de Italia (Asís, Greccio, Roma…), donde sale la carta |
| `assets/terreno-espana.jpg`, `assets/altura-espana.js` | Relieve ilustrado de la península ibérica, donde llega la carta a Madrid |
| `voz_greccio.py` | Genera la voz de Álvaro |
| `img/` | Frescos de Giotto y foto de la parroquia |
| Costas y fronteras | Natural Earth (dominio público) |
| `audio/musica.mp3` | «Noche de paz» (dominio público), en bucle |
| `og.jpg` | Vista previa al compartir |
