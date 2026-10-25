"""
Studio Asset Metadata Stumper
Author: Corey Allen Stickney (Dr. Lucid)
Description: Embeds immutable copyright and artist metadata into audio files.
"""

import sys
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TPE1, TCOM, TCOP, TALB

def stamp_audio_metadata(file_path: str, title: str, album: str = "AI Red Team Sessions"):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found -> {path}")
        return

    print(f"[*] Stamping metadata for: {path.name}")
    
    try:
        audio = ID3(str(path))
    except Exception:
        audio = ID3()

    audio["TIT2"] = TIT2(encoding=3, text=title)
    audio["TPE1"] = TPE1(encoding=3, text="Dr. Lucid (Corey Allen Stickney)")
    audio["TCOM"] = TCOM(encoding=3, text="Corey Allen Stickney")
    audio["TCOP"] = TCOP(encoding=3, text="2026 Corey Allen Stickney. All Rights Reserved.")
    audio["TALB"] = TALB(encoding=3, text=album)
    
    audio.save(str(path))
    print(f"[+] Successfully stamped copyright metadata on {path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python stamp_metadata.py <path_to_audio> <track_title>")
        sys.exit(1)
    
    stamp_audio_metadata(sys.argv[1], sys.argv[2])
