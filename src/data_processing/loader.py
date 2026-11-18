from pathlib import Path

def video_exists(video_path: str) -> bool:
    return Path(video_path).is_file()