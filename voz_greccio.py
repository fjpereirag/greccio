# Genera la voz de Álvaro (edge-tts, es-ES-AlvaroNeural) para «Greccio: un Belén para ti».
# Uso, desde esta carpeta:   pip install edge-tts   y después   python voz_greccio.py
# Crea los mp3 en audio/. Si cambias una frase en app.js, cámbiala también aquí y vuelve a ejecutarlo.
import asyncio, os, edge_tts
VOZ, VELOCIDAD = 'es-ES-AlvaroNeural', '-8%'
FRASES = {
    '00': 'Greccio. Un Belén para ti.',
    '01': 'Era la Navidad de 1223. Francisco quiso celebrarla en Greccio, un pueblo en las montañas del valle de Rieti.',
    '02': '«Quiero celebrar la memoria del Niño que nació en Belén.»',
    '03': 'Preparó un pesebre con heno, junto a un buey y un asno. Aquella noche Greccio se convirtió en un nuevo Belén.',
    '04': 'Francisco lo había dejado todo para seguir a Jesús pobre.',
    '05': '«Siendo rico, quiso escoger la pobreza.»',
    '06': 'Por eso en Navidad pedía que nadie pasara hambre: ni los pobres, ni siquiera los animales.',
    '07': 'El mismo Jesús que nació en Belén le había hablado desde la cruz de San Damián.',
    '08': 'Y Francisco salió a anunciarlo a todos, hasta a los pájaros del camino.',
    '09': '«El Señor te dé la paz.»',
    '10': 'Esta Navidad, haz en tu casa un pequeño Greccio: deja que el Niño de Belén encuentre sitio en ella.',
    '12': 'Feliz Navidad. Te esperamos en la parroquia del Cristo de la Paz.',
    '13': '«Donde hay pobreza con alegría, no hay codicia ni avaricia.»',
    '14': 'El Hijo de Dios se hizo pequeño y pobre para que nadie tenga miedo de acercarse.',
}
async def main():
    os.makedirs('audio', exist_ok=True)
    for k, t in FRASES.items():
        t = t.replace('«', '').replace('»', '')
        await edge_tts.Communicate(t, VOZ, rate=VELOCIDAD).save(f'audio/greccio_{k}.mp3'); print('audio/greccio_' + k + '.mp3')
asyncio.run(main())
