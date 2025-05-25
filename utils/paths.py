def sanitize(path: str) -> str:
    return path.replace("/", "\\").strip()