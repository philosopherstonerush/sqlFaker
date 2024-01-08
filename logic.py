from faker import Faker
from simple_ddl_parser import DDLParser
from services import Table

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype
    - Conditions - Unique, Nullable 
    - Checks

    TODO: add more above if appropriate

"""

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

tables = []


def parse_ddl_script(ddl):

    # NOTE: A good design choice would be to separate the tables into difference scripts.

    try:
        parse = DDLParser(ddl, silent=False).run(output_mode="mysql")
    except Exception:
        return AWSResponse(
            status_code=400,
            body="error: DDL script cannot be parsed"
        ).get_json_response()

    tables = []

    for elem in parse:
        tables.append(Table.from_json(elem))



    return parse


"""

Given a list of 

    [
        {
            name, 
            provider, 
            subprovider
        }, ...
    ], 
    
    return list of  generated data as
    [
        {
            name: ___
            data: ---
        },...
    ]

"""

def to_generate (prov, size):
    data = []
    rows=10
    for i in range(rows):
        print(prov,end=",")
    print()



parse_ddl_script(ddl_script)


def generate_data():
    fake = Faker()
    for inst in tables:
        for colinst in inst.columns:
            types = str(colinst.type)
            match types.upper():
                case "INT":
                    to_generate(fake.pyint(0, 2147483647), colinst.size)
                case "TINYINT":
                    to_generate(fake.pyint(0, 255), colinst.size)
                case "BIT" | "BINARY" | "VARBINARY" | "IMAGE":
                    to_generate(fake.pyint(0, 1), colinst.size)
                case "SMALLINT":
                    to_generate(fake.pyint(0, 32767), colinst.size)
                case "MEDIUMINT":
                    to_generate(fake.pyint(0, 8388607), colinst.size)
                case "BIGINT":
                    to_generate(fake.pyint(0, 9223372036854775808), colinst.size)
                case "BOOL" | "BOOLEAN":
                    to_generate(fake.pybool(), colinst.size)
                case "VARCHAR" | "CHAR" | "TEXT" | "NVARCHAR" | "NCHAR" | "NTEXT":
                    to_generate(fake.name(), colinst.size)
                case "FLOAT" | "SMALLMONEY" | "MONEY" | "DECIMAL" | "DEC":
                    to_generate(fake.pyfloat(0, 214748.3647), colinst.size)
                case "DATE":
                    to_generate(fake.date(), colinst.size)
                case "DATETIME" | "DATETIME2" | "SMALLDATETIME":
                    to_generate(fake.date_time_between(1753-1-1, 9999-12-31), colinst.size)
                case "TIME":
                    to_generate(fake.time(), colinst.size)
                case "YEAR":
                    to_generate(fake.year(), colinst.size)
                case "TIMESTAMP":
                    to_generate(fake.unix_time(), colinst.size)


generate_data()
