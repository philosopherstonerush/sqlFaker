import json

from simple_ddl_parser import DDLParser
from services import AWSResponse, Table, Column, Reference

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype

    TODO: add more above if appropriate

"""


def parse_ddl_script(ddl):

    parse = DDLParser(ddl).run()

    tables = []

    for elem in parse:
        tables.append(Table.from_json(elem))

    print("done")


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


def generate_data(info_list):
    pass
