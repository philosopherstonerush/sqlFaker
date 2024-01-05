
from unittest import TestCase
from logic import parse_ddl_script

# Write tests here

class ParseTesting(TestCase):

    def test_handles_simple_ddl(self):

        s = """
        
        CREATE TABLE Books
        (
            Id INT PRIMARY KEY,
            Price INT
        )
        
        """

        expected = [
            {
                "name": "Id",
                "data_type": "int",
            },
            {
                "name": "Price",
                "data_type": "int"
            }
        ]

        output = parse_ddl_script(s)

        self.assertEqual(output, expected)