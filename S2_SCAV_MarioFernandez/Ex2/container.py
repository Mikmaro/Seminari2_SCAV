# Mario Fernández
# Exercise 2

"""
Primero utilicé la misma función que el anterior
lab para poder cortar el vídeo de BBB (llamado Big_Buck_Bunny.mp4),
esta vez del primer minuto.
A continuación, se hace toda la extracción de los tracks y finalmente
el packaging en un archivo que se llamará package_BBB.mp4
"""

import os
import wget


def package():
    url1 = 'https://drive.google.com/uc?export=download&id=1-W3v4K9wa8yFImuH96yUqlBKkuONdeLg'
    wget.download(url1)  # Vídeo descargado -> Big_Buck_Bunny.mp4

    # Cortar los primeros 60 segundos del vídeo original Big_Buck_Bunny, cuyo output
    # será cut_video_60_seconds_with_volume
    cmd0 = 'ffmpeg -ss 0 -i Big_Buck_Bunny.mp4 -c copy -t 60 cut_video_60_seconds_with_volume.mp4'
    os.system(cmd0)

    # Después de extraer el vídeo a 60 segundos, quitar el audio de este vídeo
    # El vídeo resultante (sin volumen) será cut_video_60_seconds.mp4
    cmd1 = 'ffmpeg -i cut_video_60_seconds_with_volume.mp4 -c copy -an cut_video_60_seconds.mp4'

    # La linea convertirá el vídeo de 1 minuto ...
    # ... en un archivo mp3 (audio_of_cut_video_60_seconds.mp3)
    cmd2 = 'ffmpeg -i cut_video_60_seconds_with_volume.mp4 mp3_audio_of_cut_video_60_seconds.mp3'

    # Luego, convertir el anterior mp3 en stereo (stereo_audio_of_cut_video_60_seconds.mp3)
    cmd3 = 'ffmpeg -i mp3_audio_of_cut_video_60_seconds.mp3 -ac 2 mp3_stereo_audio_of_cut_video_60_seconds.mp3'

    # Después se debe extraer el aac con menor bitrate
    # Utilizando -b:a 20k, esto permitirá que el bitrate baje considerablemente ...
    # ... respecto a los audios anteriores
    cmd4 = 'ffmpeg -i cut_video_60_seconds_with_volume.mp4 -b:a 20k -map a aac_audio_of_cut_video_60_seconds.aac'

    os.system(cmd1)

    os.system(cmd2)

    os.system(cmd3)

    os.system(cmd4)

    # Finalmente hacer todo el package dentro del archivo output, que será package_BBB.mp4
    # Utilizando -map para cada uno de los archivos anteriores:
    # map 0 --> cut_video_60_seconds.mp4 (SIN VOLUMEN)
    # map 1 --> mp3_stereo_audio_of_cut_video_60_seconds.mp3 (primer track de audio, .mp3)
    # map 2 --> aac_audio_of_cut_video_60_seconds.aac (segundo track de audio, .aac)

    cmd5 = 'ffmpeg -i cut_video_60_seconds.mp4 -i mp3_stereo_audio_of_cut_video_60_seconds.mp3 -i ' \
           'aac_audio_of_cut_video_60_seconds.aac -map 0 -map 1 -map 2 -c copy package_BBB.mp4'

    os.system(cmd5)

    ''' Si se quiere ver las características de este archivo, haciendo:
        ffmpeg -i package_BBB.mp4
        He adjuntado una captura en esta misma carpeta para poder ver los dos audio tracks disponibles
        
        Si, una vez obtenido este vídeo (package_BBB.mp4) se abre con VLC y se selecciona
        la pestaña Audio->Pista de Audio, se puede seleccionar cualquiera de las dos audio tracks 
    '''


if __name__ == '__main__':
    package()
