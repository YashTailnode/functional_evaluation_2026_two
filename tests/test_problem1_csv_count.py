import unittest

from solutions.problem1_csv_count import count_csv_records


class CountCsvRecordsTest(unittest.TestCase):
    def test_counts_data_rows_and_excludes_header(self):
        content = "id,name\n1,John\n2,Mary"

        self.assertEqual(count_csv_records(content), 2)

    def test_ignores_trailing_newline_and_blank_rows(self):
        content = "id,name\n1,John\n2,Mary\n\n"

        self.assertEqual(count_csv_records(content), 2)

    def test_handles_empty_content(self):
        self.assertEqual(count_csv_records(""), 0)
        self.assertEqual(count_csv_records("   \n"), 0)

    def test_handles_quoted_multiline_fields(self):
        content = 'id,notes\n1,"hello\nworld"\n2,"done"'

        self.assertEqual(count_csv_records(content), 2)

    def test_can_count_files_without_header(self):
        self.assertEqual(count_csv_records("1,John\n2,Mary", has_header=False), 2)


if __name__ == "__main__":
    unittest.main()
