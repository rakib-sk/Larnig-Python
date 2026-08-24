import subprocess
import os

def banner():
    os.system("clear")
    print("=" * 50)
    print("        🎬 Video Downloader CLI")
    print("=" * 50)

while True:
    banner()

    url = input("🔗 Enter Video URL: ").strip()

    print("\nQuality")
    print("[1] Best")
    print("[2] 1080p")
    print("[3] 720p")
    print("[4] Audio Only")
    print("[0] Exit")

    choice = input("\nSelect: ")

    if choice == "0":
        break

    if choice == "1":
        fmt = "best"
    elif choice == "2":
        fmt = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    elif choice == "3":
        fmt = "bestvideo[height<=720]+bestaudio/best[height<=720]"
    elif choice == "4":
        fmt = "bestaudio"
    else:
        print("Invalid Choice")
        input("Press Enter...")
        continue

    cmd = [
        "yt-dlp",
        "-f", fmt,
        "-o", "Downloads/%(title)s.%(ext)s",
        url
    ]

    subprocess.run(cmd)

    input("\nPress Enter to continue...")