import json
from faker import Faker
from simple_ddl_parser import DDLParser
from services import AWSResponse, Table, Column, Reference

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype

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
n=None
def parse_ddl_script(ddl):
    global n
    parse = DDLParser(ddl).run()
    n=len(parse)

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

parse_ddl_script(ddl_script)

def generate_data(info_list):
    fake=Faker()
    instances=[]
    for i in range(n):
        instance=Column()

