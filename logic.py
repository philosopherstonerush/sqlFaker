from faker import Faker
from simple_ddl_parser import DDLParser
from services import AWSResponse, Table

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype
    - Conditions - Unique, Nullable 
    - Checks

    TODO: add more above if appropriate

"""


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


def generate_data():
    pass
