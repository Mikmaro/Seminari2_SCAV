# Mario Fernández
# Exercise 1

"""
El video input es cut_video_12_seconds.mp4, y el ouptut es video_macroblock_motion_vector.mp4.
He seguido el mismo prodecimiento de la práctica anterior respecto al wget para así ya tener
descargado en la carpeta que se esté trabajando el vídeo cut_video_12_seconds.mp4.
Esto también implica a los demás ejercicios, los vídeos necesarios de input se descargan
mediante los wget
"""
import os
import wget


def macroblock_motion_vector():
    url1 = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url1)
    cmd = 'ffmpeg -flags2 +export_mvs -i cut_video_12_seconds.mp4 -vf codecview=mv=pf+bf+bb ' \
          'video_macroblock_motion_vector.mp4'

    os.system(cmd)


if __name__ == '__main__':
    macroblock_motion_vector()
