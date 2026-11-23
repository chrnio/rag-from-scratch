from pathlib import Path

DEFAULT_ENCODING = "utf-8"

def load_text(path, encoding=DEFAULT_ENCODING):
    """Loads the whole file as a single string."""
    # changed from PosixPath() to Path() for cross-platform source compatibility
    return Path(path).expanduser().read_text(encoding=encoding, errors="ignore")

def iter_lines(path, encoding=DEFAULT_ENCODING):
    """Yields the file line by line."""
    with Path(path).expanduser().open(encoding=encoding) as file:
        yield from file
