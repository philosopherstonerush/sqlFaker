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
                "name": "Id",
                "data_type": "int",
            },
            {
                "name": "Price",
                "data_type": "int"
            }
        ]

        output = parse_ddl_script(s)

        print(json.dumps(output, indent=4))

        self.assertEqual(output, expected)

    def test_return_foreign_key(self):
        ddl_script = """
                            CREATE TABLE Orders (
                    OrderID int NOT NULL,
                    OrderNumber int NOT NULL,
                    PersonID int,
                    PRIMARY KEY (OrderID),
                    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)); 
        """

        output = parse_ddl_script(ddl_script)

        print(json.dumps(output, indent=4))

    def test_create_two_tables(self):
        ddl_script = """
            
        CREATE TABLE Department(
            DeptNo int PRIMARY KEY,
            DName varchar(266),
            Location varchar(266)
        );

        CREATE TABLE Employee(
            EmpNo int,
            EmpName varchar(266),
            Salary int,
            DeptNo int,
            FOREIGN KEY (DeptNo) REFERENCES Department(DeptNo)
        );
        
        """

        output = parse_ddl_script(ddl_script)

        print(json.dumps(output, indent=4))

    def test_un_detectable_tables(self):
        ddl = """CREATE TABLE authors (
                        id INT(11) NOT NULL AUTO_INCREMENT,
                        first_name VARCHAR(50) NOT NULL,
                        last_name VARCHAR(50) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        birthdate DATE NOT NULL,
                        added TIMESTAMP NOT NULL,
                        PRIMARY KEY (id),
                        UNIQUE INDEX email (email)
                    );
                """
        output = parse_ddl_script(ddl)

        print(json.dumps(output, indent=4))

