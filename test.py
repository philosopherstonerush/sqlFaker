from unittest import TestCase
from logic import parse_ddl_script, generate_data
import constants
from data_type_match import get_func_for_data_type, data_func_map

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
        result = generate_data(ddl_script=s)
        print(result)
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

    def test_provider_mapping_for_BIGINT(self):

        data_type = constants.MySQLDataType.BIGINT.value

        func_dict = get_func_for_data_type(data_type)

        func = func_dict.get("func")
        params = func_dict.get("params")

        result = func(**params)

        print(result)

    def test_provider_mapping_for_CITEXT(self):

        data_type = constants.PostgreSqlDataType.CITEXT.value

        func_dict = get_func_for_data_type(data_type)

        func = func_dict.get("func")
        params = func_dict.get("params")

        result = func(**params)

        print(result)

    def test_provider_mapping_for_JSON(self):
        data_type = constants.MySQLDataType.JSON.value

        func_dict = get_func_for_data_type(data_type)

        func = func_dict.get("func")
        params = func_dict.get("params")

        result = func(**params)

        print(result)

    def test_provider_mapping_for_DATE(self):
        data_type = constants.MySQLDataType.DATE.value

        func_dict = get_func_for_data_type(data_type)

        func = func_dict.get("func")
        params = func_dict.get("params")

        result = func(**params)

        print(result)

    def test_provider_mapping_for_numrange(self):
        data_type = constants.PostgreSqlDataType.NUMRANGE.value

        func_dict = get_func_for_data_type(data_type)

        func = func_dict.get("func")
        params = func_dict.get("params")

        result = func(**params)

        print(result)

    def test_provider_mapping_for_daterange(self):
        data_type = constants.PostgreSqlDataType.DATERANGE.value

        func_dict = get_func_for_data_type(data_type)

        func = func_dict.get("func")
        params = func_dict.get("params")

        result = func(**params)

        print(result)

    def test_all_dataType_map_providers(self):
        all_keys = list(data_func_map.keys())
        all_keys_separated = []
        for key in all_keys:
            if isinstance(key, tuple):
                all_keys_separated.append(key[0])
            else:
                all_keys_separated.append(key)
        for key in all_keys_separated:

            func_dict = get_func_for_data_type(key)

            func = func_dict.get("func")
            params = func_dict.get("params")

            if "custom" in func.__name__:
                result = func(params)
            else:
                result = func(**params)

            print(key + ": " + str(result))


    def test_generate_date_for_sample_table_primary_key_given_after(self):
        ddl_script = """CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
); """

        result = generate_data(ddl_script, None)

        print(result)

    def test_generate_data_for_sample_table_primary_key_given_in_column(self):

        ddl_script = """
            
            CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);
        
        """

        result = generate_data(ddl_script, None)

        print(result)