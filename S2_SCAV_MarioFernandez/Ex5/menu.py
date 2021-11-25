# Mario Fernández
# Exercise 5

"""

"""

import os
import wget
import subprocess


class seminar2:  # Esta será la clase para este ejercicio
    # ex1
    def macroblock_motion_vector(self):
        url1 = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

        wget.download(url1)
        cmd = 'ffmpeg -flags2 +export_mvs -i cut_video_12_seconds.mp4 -vf codecview=mv=pf+bf+bb ' \
              'video_macroblock_motion_vector.mp4'

        os.system(cmd)

    # ex2
    def package(self):
        url1 = 'https://drive.google.com/uc?export=download&id=1-W3v4K9wa8yFImuH96yUqlBKkuONdeLg'
        wget.download(url1)  # Vídeo descargado -> Big_Buck_Bunny.mp4

        cmd0 = 'ffmpeg -ss 0 -i Big_Buck_Bunny.mp4 -c copy -t 60 cut_video_60_seconds_with_volume.mp4'
        os.system(cmd0)

        cmd1 = 'ffmpeg -i cut_video_60_seconds_with_volume.mp4 -c copy -an cut_video_60_seconds.mp4'

        cmd2 = 'ffmpeg -i cut_video_60_seconds_with_volume.mp4 mp3_audio_of_cut_video_60_seconds.mp3'

        cmd3 = 'ffmpeg -i mp3_audio_of_cut_video_60_seconds.mp3 -ac 2 mp3_stereo_audio_of_cut_video_60_seconds.mp3'

        cmd4 = 'ffmpeg -i cut_video_60_seconds_with_volume.mp4 -b:a 20k -map a aac_audio_of_cut_video_60_seconds.aac'

        os.system(cmd1)

        os.system(cmd2)

        os.system(cmd3)

        os.system(cmd4)

        cmd5 = 'ffmpeg -i cut_video_60_seconds.mp4 -i mp3_stereo_audio_of_cut_video_60_seconds.mp3 -i ' \
               'aac_audio_of_cut_video_60_seconds.aac -map 0 -map 1 -map 2 -c copy package_BBB.mp4'

        os.system(cmd5)

    # ex3
    def read_container(self):
        url = 'https://drive.google.com/uc?export=download&id=1JNG_179igGs6Z-8Tw4SnM874c2tCEVlN'

        wget.download(url)  # Vídeo descargado --> package_BBB.mp4

        cmd0 = ['ffprobe', '-show_entries', 'stream=codec_name', '-of', 'default=nokey=1:noprint_wrappers=1',
                'package_BBB.mp4']
        output = subprocess.Popen(cmd0, stdout=subprocess.PIPE).communicate()[0]

        list = output.split()

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

    # ex4
    def subtitles(self):
        url1 = 'https://drive.google.com/uc?export=download&id=1n5CW5f1SeJafp5aD3GO5ztaHlX6q_tCu'

        wget.download(url1)  # descargado --> subtitles.srt

        url2 = 'https://drive.google.com/uc?export=download&id=1hLGMB-PnlJodOS8ngbfjmbmUj9h6VKO-'

        wget.download(url2)

        cmd1 = 'ffmpeg -ss 0 -i 2001_trailer.mp4 -c copy -t 68 final_2001_trailer.mp4'
        os.system(cmd1)

        cmd2 = 'ffmpeg -i final_2001_trailer.mp4 -vf subtitles=2001_subtitles.srt video_with_subtitles.mp4'

        os.system(cmd2)

    # menú
    def menu(self):  # Misma estructura de menú que la práctica 2 (P2)
        os.system('clear')

        print("Selecciona un ejercicio con las teclas [1][2][3][4], o [5] para salir:")

        print("\t[1] - Ejercicio 1: Macroblocks y motion vectors")

        print("\t[2] - Ejercicio 2: ¡Crearás un container!")

        print("\t[3] - Ejercicio 3: ¡Analizarás el container")

        print("\t[4] - Ejercicio 4: ¡Crearás un vídeo con subtítulos!")

        print("\t[5] - Salir ")


if __name__ == '__main__':
    s = seminar2()  # crear nueva instancia de la clase para utilizar las siguientes funciones
    while True:
        s.menu()
        ejercicio_escogido = input("Selecciona ejercicio: ")

        if ejercicio_escogido == "1":
            s.macroblock_motion_vector()

        elif ejercicio_escogido == "2":
            s.package()

        elif ejercicio_escogido == "3":
            s.read_container()
            #  debido a que el manú se vuelve a mostrar una vez se ha compilado la funión read_container,
            # la verdad que merece más la pena ver este ejercicio dentro de la carpeta de Ex3
            # ya que no da tiempo de ver el output con el menú

        elif ejercicio_escogido == "4":
            s.subtitles()

        elif ejercicio_escogido == "5":
            break

        else:
            input("Ese ejercicio no existe. Escoge de nuevo: ")
