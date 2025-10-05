import yt_dlp
import os
import imageio_ffmpeg  # Biblioteca que fornece o FFmpeg

def baixar_com_ytdlp(link: str, formato: str = 'mp4', path: str = '.'):
    """
    Baixa um vídeo ou áudio do YouTube usando a biblioteca yt-dlp.
    Para MP3, utiliza o FFmpeg fornecido pela biblioteca imageio-ffmpeg.

    Args:
        link (str): O link do vídeo do YouTube.
        formato (str): O formato desejado ('mp4' ou 'mp3').
        path (str): O diretório para salvar o arquivo.
    """
    print(f"\nIniciando download com yt-dlp...")
    
    # Garante que o diretório de destino exista
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Pasta '{path}' criada com sucesso!")

    try:
        if formato.lower() == 'mp4':
            print("Formato: MP4 (melhor vídeo com áudio)")
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }
        
        elif formato.lower() == 'mp3':
            print("Formato: MP3 (apenas áudio, com conversão)")
            
            ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

            ydl_opts = {
                'format': 'bestaudio/best',
                'ffmpeg_location': ffmpeg_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(path, '%(title)s.mp3'),
            }
        else:
            print("Formato inválido. Escolha 'mp4' ou 'mp3'.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        print(f"\nDownload concluído com sucesso! Verifique a pasta: '{os.path.abspath(path)}'")

    except Exception as e:
        print(f"\nOcorreu um erro inesperado com o yt-dlp: {e}")


# --- Ponto de entrada do Script ---
if __name__ == '__main__':
    print("--- YouTube Downloader (versão final com yt-dlp) ---")
    
    # --- ALTERAÇÃO AQUI ---
    # Define o caminho fixo para salvar os arquivos.
    # O 'r' antes da string é importante para que o Python leia o caminho do Windows corretamente.
    save_path = r"C:\Users\Rodriguez\Documents\Baixador"
    
    url = input("Cole o link do vídeo do YouTube aqui: ")
    
    formato_escolhido = ""
    while formato_escolhido not in ['mp4', 'mp3']:
        formato_escolhido = input("Qual formato você deseja (mp4 ou mp3)? ").lower()
        if formato_escolhido not in ['mp4', 'mp3']:
            print("Opção inválida! Tente novamente.")

    # A pergunta sobre onde salvar foi removida.
    
    baixar_com_ytdlp(url, formato_escolhido, save_path)