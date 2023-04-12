from pathlib import Path


class Site:

    def __init__(self, src: str, dest: str):
        self.source = Path(src)
        self.destination = Path(dest)

    def create_dir(self, path: Path) -> None:
        directory: Path = self.destination / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self) -> None:
        self.destination.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

