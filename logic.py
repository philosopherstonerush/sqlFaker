import json
from faker import Faker
from simple_ddl_parser import DDLParser
from services import AWSResponse, Table, Reference, Column
from data_type_match import GenData

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype
    - Conditions - Unique, Nullable 
    - Checks

"""


def parse_ddl_script(ddl_script, opt=False):
    try:
        lowercased_string = ddl_script.lower().strip()
        SPLIT_SUBSTRING = "create table"
        tables_list = lowercased_string.split(SPLIT_SUBSTRING)
        parsed_result = []
        for i in range(len(tables_list)):
            if tables_list[i]:
                tables_list[i] = SPLIT_SUBSTRING + tables_list[i]
        parsed_result = []
        for elem in tables_list:
            if elem != "":
                parse = DDLParser(elem, silent=True).run(output_mode="sql")
                if parse:
                    parsed_result.append(parse[0])
        if opt:
            return AWSResponse(
                status_code=200,
                body=json.dumps(parsed_result)
            ).get_json_response()
        else:
            return parsed_result
    except Exception as e:
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

"""

{"custom_data":"{"hm":{"consultants":{"columnProviders":[{"name":"id","provider":"NONE","subProvider":"NONE"},{"name":"first_name","provider":"NONE","subProvider":"NONE"},{"name":"last_name","provider":"NONE","subProvider":"NONE"},{"name":"email","provider":"NONE","subProvider":"NONE"},{"name":"departments_id","provider":"NONE","subProvider":"NONE"},{"name":"contract_date","provider":"NONE","subProvider":"NONE"}],"tableName":null}}}","script":"/* Try generating fake data with this or enter your own */
CREATE TABLE consultants(
    id serial NOT NULL,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    email varchar(200),
    departments_id integer NOT NULL,
    contract_date date
); "}

"""


def generate_data(ddl_script, custom_data, size=5):
    rows = 5
    fake = GenData()
    result = {}
    parsed_info = parse_ddl_script(ddl_script)
    for x, i in enumerate(parsed_info):
        table = Table.from_json(i)
        result[table.table_name] = {}
        for i in table.get_columns_json_list():
            if i['references']:
                generate = fake.foreign_keymap(result, i["references"].table, i["references"].column, rows)
                result[table.table_name][i["name"]] = generate
            elif i["autoincrement"]:
                generate = fake.AutoIncrement(i["type"], i["size"], rows)
                result[table.table_name][i["name"]] = generate
            else:
                generate = fake.get_provider_for_data_type(i["type"], i["size"], rows)
                result[table.table_name][i["name"]] = generate
    return AWSResponse(
        status_code=400,
        body=json.dumps(result)
    )
