import subprocess

def downloader(number):
    for i in range(int(number)):
      inpo = input("Testo: ")
      subprocess.run(["yt-dlp.exe", inpo])

    
