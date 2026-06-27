import unittest

from solutions.problem3_process_records import process_records


class ProcessRecordsTest(unittest.TestCase):
    def test_groups_records_by_id_preserving_result_order(self):
        records = [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"},
            {"id": 1, "name": "C"},
        ]

        self.assertEqual(
            process_records(records),
            [
                [{"id": 1, "name": "A"}, {"id": 1, "name": "C"}],
                [{"id": 2, "name": "B"}],
                [{"id": 1, "name": "A"}, {"id": 1, "name": "C"}],
            ],
        )

    def test_empty_input_returns_empty_list(self):
        self.assertEqual(process_records([]), [])

    def test_accepts_generators(self):
        records = ({"id": item % 2, "value": item} for item in range(3))

        self.assertEqual(
            process_records(records),
            [
                [{"id": 0, "value": 0}, {"id": 0, "value": 2}],
                [{"id": 1, "value": 1}],
                [{"id": 0, "value": 0}, {"id": 0, "value": 2}],
            ],
        )


if __name__ == "__main__":
    unittest.main()
