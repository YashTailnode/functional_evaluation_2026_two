from collections import defaultdict
from collections.abc import Iterable
from typing import Any


def process_records(records: Iterable[dict[str, Any]]) -> list[list[dict[str, Any]]]:

    records = list(records)
    records_by_id: dict[Any, list[dict[str, Any]]] = defaultdict(list)

    for record in records:
        records_by_id[record["id"]].append(record)

    return [records_by_id[record["id"]] for record in records]

