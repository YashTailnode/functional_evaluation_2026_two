import csv
from io import StringIO


def count_csv_records(content: str, has_header: bool = True) -> int:
    if not content or not content.strip():
        return 0

    reader = csv.reader(StringIO(content))
    rows = [row for row in reader if any(cell.strip() for cell in row)]

    if has_header and rows:
        return len(rows) - 1

    return len(rows)

