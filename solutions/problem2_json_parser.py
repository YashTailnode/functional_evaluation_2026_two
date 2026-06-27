import json


class JsonParseError(ValueError):
    def __init__(self, message: str, *, line: int | None = None, column: int | None = None):
        self.line = line
        self.column = column

        location = ""
        if line is not None and column is not None:
            location = f" at line {line}, column {column}"

        super().__init__(f"{message}{location}")


def parse_json(content: str):
    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise JsonParseError(
            "Invalid JSON",
            line=exc.lineno,
            column=exc.colno,
        ) from exc

