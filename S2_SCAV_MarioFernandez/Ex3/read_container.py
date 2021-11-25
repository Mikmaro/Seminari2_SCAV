# Mario Fernández
# Exercise 3

"""
Para este ejercicio es necesario utilizar el vídeo generado en el ejercicio
anterior (package_BBB.mp4), por lo que una vez se ha ejecutado el ejercicio 2,
se debería añadir el .mp4 a esta carpeta.
Aún así, en el ejercicio 5 no hará falta pasar el archivo de un lado
a otro, ya que el vídeo creado estará en la misma carpeta de Ex5.
"""
import os
import subprocess
import wget


def read_container():
    url = 'https://drive.google.com/uc?export=download&id=1JNG_179igGs6Z-8Tw4SnM874c2tCEVlN'

    wget.download(url)  # Vídeo descargado --> package_BBB.mp4

    # La siguiente línea encontré que meustra los diferentes codecs que...
    # ... encajan para el input introducido, con a ffprobe
    cmd0 = ['ffprobe', '-show_entries', 'stream=codec_name', '-of', 'default=nokey=1:noprint_wrappers=1',
            'package_BBB.mp4']
    # Esto permite tener en una variable el output que se da en la terminal, útil para siguientes acciones
    output = subprocess.Popen(cmd0, stdout=subprocess.PIPE).communicate()[0]

    # El output lo convertiré en una lista mediante la comanda split
    list = output.split()

    # De esta manera, para buscar me ha parecido más cómo para encontrar elementos en la lista
    # Estas son las combinaciones que son posibles para los diferentes video y audio códecs
    for i in list:
        for j in list:
            if i == b'mpg':  # video
                if j == b'aac':  # audio
                    print("El broadcasting standard sería DTMB, DVB y/o ISDB (mpg-aac)")
                elif j == b'ac3':  # audio
                    print("El broadcasting standard sería DTMB, DVB y/o ATSC (mpg-aac3)")
                elif j == b'mp3':  # audio
                    print("El broadcasting standard sería DTMB y/o DVB (mpg-mp3)")
                elif j == b'mp2':  # audio
                    print("El broadcasting standard sería DTMB (mpg-mp2)")

            if i == b'h264':  # video
                if j == b'aac':  # audio
                    print("El broadcasting standard sería DTMB, DVB y/o ISDB (h264-aac)")
                elif j == b'mp3':  # audio
                    print("El broadcasting standard sería DTMB y/o DVB (h264-mp3)")
                elif j == b'mp2':  # audio
                    print("El broadcasting standard sería DTMB (h264-mp2)")

            if i == b'avs':  # video
                print("El broadcasting standard sería DTMB")

        # Probablemente no sea ni la mejor manera ni la más eficiente... pero es la que
        # se me ha ocurrido


if __name__ == '__main__':
    read_container()
