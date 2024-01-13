import json

from faker import Faker
from simple_ddl_parser import DDLParser
from services import AWSResponse, Table
import sys

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype
    - Conditions - Unique, Nullable 
    - Checks

"""


def parse_ddl_script(ddl):
    # NOTE: A good design choice would be to separate the tables into difference scripts.

    try:
        lowercased_string = ''.join(map(lambda x: x.lower(), ddl))
        SPLIT_SUBSTRING = "create table"
        tables_list = lowercased_string.split(SPLIT_SUBSTRING)
        for i in range(len(tables_list)):
            if tables_list[i] != "":
                tables_list[i] = SPLIT_SUBSTRING + tables_list[i]
        parsed_result = []
        for elem in tables_list:
            if elem != "":
                parse = DDLParser(elem, silent=True).run(output_mode="sql")
                parsed_result.append(parse[0])
        return AWSResponse(
            status_code=200,
            body=json.dumps(parsed_result)
        ).get_json_response()
    except Exception as e:
        print(e)
        return AWSResponse(
            status_code=400,
            body="error: DDL script cannot be parsed"
        ).get_json_response()


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
