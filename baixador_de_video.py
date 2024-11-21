from yt_dlp import YoutubeDL

def baixar_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': r'seuCaminho\\%(title)s.%(ext)s'
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"Download concluído com sucesso: {info['title']}")

url = input('Digite a sua URL: ')
baixar_video(url)
