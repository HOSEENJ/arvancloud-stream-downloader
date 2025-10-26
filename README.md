# ArvanCloud Video Downloader

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful, open-source Python tool for downloading videos from ArvanCloud streaming platforms. This downloader extracts HLS (.m3u8) streams and uses FFmpeg to save high-quality videos locally.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features

- **HLS Stream Extraction**: Automatically parses ArvanCloud player configurations to extract .m3u8 URLs
- **High-Quality Downloads**: Downloads videos in original resolution and quality using FFmpeg
- **Audio Compatibility**: Converts AAC audio streams for broad device compatibility
- **Simple CLI Interface**: Easy-to-use command-line interface with interactive prompts
- **Error Handling**: Robust error handling for network issues and invalid URLs
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **No Dependencies on GUI**: Pure command-line tool, no graphical interface required

## Prerequisites

Before using this tool, ensure you have the following installed:

- **Python 3.11 or higher** - [Download Python](https://www.python.org/downloads/)
- **FFmpeg** - A powerful multimedia framework for handling video and audio streams
  - Windows: [Download FFmpeg](https://ffmpeg.org/download.html#build-windows)
  - macOS: Install via Homebrew: `brew install ffmpeg`
  - Linux: Install via package manager: `sudo apt install ffmpeg` (Ubuntu/Debian)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/HOSEENJ/arvancloud-stream-downloader.git
cd arvancloud-stream-downloader
```

### Step 2: Install Python Dependencies

Install the required Python packages using pip:

```bash
pip install requests
```

For better dependency management, consider using a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install requests
```

### Step 3: Verify FFmpeg Installation

Ensure FFmpeg is properly installed and accessible from your command line:

```bash
ffmpeg -version
```

If you see version information, FFmpeg is ready. If not, add FFmpeg to your system's PATH.

## Usage

### Basic Usage

1. Run the downloader script:
   ```bash
   python arvan_dl.py
   ```

2. When prompted, paste your ArvanCloud player URL:
   ```
   🔗 Paste ArvanCloud Player URL: https://example.com/player?config=https://api.arvancloud.com/vod/config.json
   ```

3. Enter your desired output filename:
   ```
   💾 Output filename (e.g. video.mp4): my_downloaded_video.mp4
   ```

4. The tool will automatically:
   - Fetch the stream configuration
   - Extract the .m3u8 URL
   - Download the video using FFmpeg

### Advanced Usage

You can also modify the script for batch processing or integration into other applications. The main functions are:

- `get_m3u8_url(config_url)`: Extracts the HLS stream URL from a config URL
- `download_with_ffmpeg(m3u8_url, output_file)`: Downloads the video using FFmpeg

## Examples

### Example 1: Downloading a Standard Video

```bash
$ python arvan_dl.py
🎬 ArvanCloud Downloader (via FFmpeg)

🔗 Paste ArvanCloud Player URL: https://player.arvancloud.com/vod/?config=https://vod.arvancloud.com/config/abc123
💾 Output filename (e.g. video.mp4): tutorial.mp4

🔍 Getting .m3u8 stream link...
📥 Downloading video to: tutorial.mp4

✅ Done: tutorial.mp4
```

### Example 2: Handling Errors

```bash
$ python arvan_dl.py
🎬 ArvanCloud Downloader (via FFmpeg)

🔗 Paste ArvanCloud Player URL: invalid-url
❌ Failed to fetch config: Invalid URL 'invalid-url': No scheme supplied.
❌ Stream link could not be extracted.
```

## Troubleshooting

### Common Issues

**FFmpeg not found**
- Ensure FFmpeg is installed and added to your system's PATH
- On Windows, you may need to restart your command prompt after installation

**Network errors**
- Check your internet connection
- Verify the ArvanCloud URL is accessible and valid
- Some streams may require authentication or be geo-restricted

**Python import errors**
- Install missing dependencies: `pip install requests`
- Use the correct Python version (3.11+)

**Video download fails**
- The stream might be protected or temporarily unavailable
- Try a different output format or check FFmpeg compatibility

### Getting Help

If you encounter issues not covered here:
1. Check the [Issues](https://github.com/HOSEENJ/arvancloud-stream-downloader/issues) page on GitHub
2. Create a new issue with detailed information about your problem
3. Include your operating system, Python version, and FFmpeg version

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Development Setup

For contributors:

```bash
git clone https://github.com/HOSEENJ/arvancloud-stream-downloader.git
cd arvancloud-stream-downloader
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt  # If we add a requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational and personal use only. Users are responsible for complying with copyright laws and terms of service of the content they download. The authors are not responsible for any misuse of this software.

Always ensure you have legal permission to download and store the content. Respect intellectual property rights.
