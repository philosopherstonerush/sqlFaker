from unittest import TestCase
from logic import parse_ddl_script
import json


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
        "table_name": "books",
        "schema": None,
        "primary_key": [
            "id"
        ],
        "columns": [
            {
                "name": "id",
                "type": "int",
                "size": None,
                "references": None,
                "unique": False,
                "nullable": False,
                "default": None,
                "check": None
            },
            {
                "name": "price",
                "type": "int",
                "size": None,
                "references": None,
                "unique": False,
                "nullable": True,
                "default": None,
                "check": None
            }
        ],
        "alter": {},
        "checks": [],
        "index": [],
        "partitioned_by": [],
        "tablespace": None
    }
]

        output = parse_ddl_script(s)

        self.assertEqual(output, expected)

    def test_return_foreign_key(self):
        ddl_script = """CREATE TABLE consultants(
    id serial NOT NULL,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    email varchar(200),
    departments_id integer NOT NULL,
    contract_date date
); """

        expected = [
    {
        "table_name": "consultants",
        "schema": None,
        "primary_key": [],
        "columns": [
            {
                "name": "id",
                "type": "serial",
                "size": None,
                "references": None,
                "unique": False,
                "nullable": False,
                "default": None,
                "check": None
            },
            {
                "name": "first_name",
                "type": "varchar",
                "size": 100,
                "references": None,
                "unique": False,
                "nullable": False,
                "default": None,
                "check": None
            },
            {
                "name": "last_name",
                "type": "varchar",
                "size": 100,
                "references": None,
                "unique": False,
                "nullable": False,
                "default": None,
                "check": None
            },
            {
                "name": "email",
                "type": "varchar",
                "size": 200,
                "references": None,
                "unique": False,
                "nullable": True,
                "default": None,
                "check": None
            },
            {
                "name": "departments_id",
                "type": "integer",
                "size": None,
                "references": None,
                "unique": False,
                "nullable": False,
                "default": None,
                "check": None
            },
            {
                "name": "contract_date",
                "type": "date",
                "size": None,
                "references": None,
                "unique": False,
                "nullable": True,
                "default": None,
                "check": None
            }
        ],
        "alter": {},
        "checks": [],
        "index": [],
        "partitioned_by": [],
        "tablespace": None
    }
]

        output = parse_ddl_script(ddl_script)

        self.assertEqual(output, expected)

    #  Parsing an empty DDL script returns an empty list.
    def test_empty_ddl_script(self):
        ddl_script = ""

        expected = []

        # Arrange
        expected_output = expected

        # Act
        output = parse_ddl_script(ddl_script)

        # Assert
        self.assertEqual(output, expected_output)

