# Greccio: un Belén para ti · Navidad 2026

Felicitación de Navidad interactiva de la **Parroquia de Santa Casilda** (Carabanchel, Madrid), hermana de «Una buena noticia para ti». Esta vez la carta sale de **Greccio**, donde San Francisco de Asís hizo el primer Belén en la Nochebuena de 1223, y llega a Santa Casilda.

Web: https://fjpereirag.github.io/greccio/

## Cómo funciona

1. Se comparte el enlace. La portada, con el botón «Recibir la carta», pone en marcha la música.
2. La carta sale de Greccio sobre el mapa 3D de Umbría y el valle de Rieti, da el salto y llega en 3D a Madrid, a Carabanchel (botón «Saltar» para ir directo).
3. Se rompe el lacre y se abre el carrusel con los frescos de Giotto. Cada frase aparece palabra a palabra.
4. Al final, «Feliz Navidad · Te esperamos» y el botón **Reenviar por WhatsApp**.

El texto de la carta está en `app.js`, en la lista `CARTA_BELEN`. No lleva voz grabada: las palabras aparecen a su ritmo. Si más adelante se graban voces, basta con poner la ruta del mp3 en el campo `v` de cada frase.

## Imágenes que faltan (frescos de Giotto, Basílica superior de Asís, dominio público)

Sustituye estos archivos de `img/` por los frescos, con el mismo nombre:

| Archivo | Fresco |
|---|---|
| `giotto-greccio.jpg` | El pesebre de Greccio (Institución del Belén) |
| `giotto-renuncia.jpg` | La renuncia a los bienes |
| `giotto-manto.jpg` | San Francisco da su manto a un caballero pobre |
| `giotto-sandamian.jpg` | San Francisco ora ante el crucifijo de San Damián |
| `giotto-pajaros.jpg` | La predicación a los pájaros |

Mejor en vertical o con el motivo centrado (la tarjeta recorta a 9:16). En `app.js`, el campo `b` de cada frase marca dónde cae el brillo (porcentajes x, y).

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
| `assets/terreno-greccio.jpg`, `assets/altura-greccio.js` | Relieve ilustrado de Umbría y el valle de Rieti (Asís, Spoleto, Greccio, Rieti, Roma) |
| `assets/terreno-madrid.jpg`, `assets/altura-madrid.js` | Relieve de Madrid, donde llega la carta |
| `img/` | Frescos de Giotto y foto de la parroquia |
| `audio/musica.mp3` | «Noche de paz» (dominio público), en bucle |
| `og.jpg` | Vista previa al compartir |
