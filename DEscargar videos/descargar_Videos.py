import yt_dlp

def download_video(link):
    #Creando un objeto YoutubeDl
    ydl_opts = {
        'format':'bestvideo + bestaudio/best',#FFmpeg
        'outtmpl':'%(title)s.%(ext)s',
        'merge_output_format': 'mp4'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Descarga Completa")
        
    except Exception as e:
        print(f'Hubo un problema al descargar el video: {e}')

#main
if(__name__=='__main__'):
    link = str(input("URL: ")).strip();
    download_video(link)