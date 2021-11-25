# Mario Fernández
# Exercise 4

"""

"""
import os
import wget


def subtitles():
    # Una vez hecho esto, utilicé el siguiente enlace del tráiler de la película 2001:
    # https://www.youtube.com/watch?v=oR_e9y-bka0
    # Y, en una página de "Descargar subtitulos de YouTube a .srt", me descargué el archivo .srt
    # A continuación, colgué dicho archivo a una carpeta de mi Drive, obtuve dicho enlace ...
    # ... y con un convertidor de descargas de Drive, obtuve la siguiente url, la cual permitirá...
    # ... descargar el archivo mediante el comando de wget

    url1 = 'https://drive.google.com/uc?export=download&id=1n5CW5f1SeJafp5aD3GO5ztaHlX6q_tCu'

    wget.download(url1)  # descargado --> subtitles.srt

    # Para no volver a utilizar el vídeo de BBB y obtener un resultado más interesante, he utilizado
    # en este caso el mismo vídeo (el tráiler de 2001) mediante el mismo procedimiento anterior ...
    # ..., primero de todo descargando el vídeo de YouTube a mp4, luego subiendo el archivo al Drive,...
    # ..., después obtener el enlace de descarga para utilizarlo con el wget

    url2 = 'https://drive.google.com/uc?export=download&id=1hLGMB-PnlJodOS8ngbfjmbmUj9h6VKO-'

    wget.download(url2)

    # El vídeo resultante anterior se llama 2001_trailer.mp4, y los subtitulos se llaman 2001_subtitles.srt
    # Antes, he decidido cortar el tráiler (más adelante explicaré porqué (*))
    cmd1 = 'ffmpeg -ss 0 -i 2001_trailer.mp4 -c copy -t 68 final_2001_trailer.mp4'
    os.system(cmd1)

    # La siguiente comanda permite incrustrar los subtitulos en el vídeo, ...
    # ... resultando el vídeo final -> video_with_subtitles.mp4
    cmd2 = 'ffmpeg -i final_2001_trailer.mp4 -vf subtitles=2001_subtitles.srt video_with_subtitles.mp4'

    os.system(cmd2)

    ''' COMENTARIO (*):
    Realmente los diálogos paran de producirse a partir del mintuto 1:08, por eso he preferido
    parar el trailer hasta ese punto, utilizando la misma función que se ha utilizado en el
    ejercicio 2 y en el lab anterior para cortar un vídeo 
    '''


if __name__ == '__main__':
    subtitles()
