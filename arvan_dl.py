import requests
import subprocess
import shutil

def get_m3u8_url(config_url):
    try:
        response = requests.get(config_url)
        response.raise_for_status()
        data = response.json()

        for source in data.get("source", []):
            if source.get("type") == "application/x-mpegURL":
                return source.get("src")

        print("❌ .m3u8 stream not found in 'source' list.")
        return None
    except Exception as e:
        print(f"❌ Failed to fetch config: {e}")
        return None

def download_with_ffmpeg(m3u8_url, output_file):
    if not shutil.which("ffmpeg"):
        print("❌ FFmpeg is not installed or not in PATH.")
        return

    cmd = [
        "ffmpeg",
        "-i", m3u8_url,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        output_file
    ]

    print(f"📥 Downloading video to: {output_file}\n")
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Done: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ ffmpeg failed: {e}")

if __name__ == "__main__":
    print("🎬 ArvanCloud Downloader (via FFmpeg)\n")
    player_url = input("🔗 Paste ArvanCloud Player URL: ").strip()

    if "?config=" in player_url:
        config_url = player_url.split("?config=")[-1]
    else:
        config_url = player_url

    print("\n🔍 Getting .m3u8 stream link...")
    m3u8_url = get_m3u8_url(config_url)

    if m3u8_url:
        output_file = input("💾 Output filename (e.g. video.mp4): ").strip()
        download_with_ffmpeg(m3u8_url, output_file)
    else:
        print("❌ Stream link could not be extracted.")
