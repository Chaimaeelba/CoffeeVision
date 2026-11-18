from pathlib import Path

def video_exists(video_path: str) -> bool:
    return Path(video_path).is_file()
def is_video_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in {".mp4", ".avi", ".mov"}