import unittest

from solutions.problem2_json_parser import JsonParseError, parse_json


class ParseJsonTest(unittest.TestCase):
    def test_parse_valid_json(self):
        self.assertEqual(parse_json('{"name": "John", "age": 30}'), {"name": "John", "age": 30})

    def test_malformed_json_raises_meaningful_exception(self):
        with self.assertRaises(JsonParseError) as error:
            parse_json('{\n  "name":\n}')

        self.assertIn("Invalid JSON", str(error.exception))
        self.assertEqual(error.exception.line, 3)
        self.assertIsNotNone(error.exception.column)

    def test_original_json_error_is_preserved_as_cause(self):
        with self.assertRaises(JsonParseError) as error:
            parse_json("{bad json")

        self.assertIsNotNone(error.exception.__cause__)


if __name__ == "__main__":
    unittest.main()
