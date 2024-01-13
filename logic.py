import json
from faker import Faker
from simple_ddl_parser import DDLParser
from services import AWSResponse, Table,Reference,Column
from data_type_match import gen_data

"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype
    - Conditions - Unique, Nullable 
    - Checks

"""
ddl_script = """
                    CREATE TABLE Department(
            DeptNo int PRIMARY KEY,
            DName varchar(266),
            Location varchar(266),
            Time timestamp
        );

        CREATE TABLE Employee(
            EmpNo int,
            EmpName varchar(266),
            Salary int,
            DeptNo int,
            FOREIGN KEY (DeptNo) REFERENCES Department(DeptNo)
        ); 
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
def generate_data(default):
    if default== "YES":
        rows=5
        fake=gen_data()
        result={}
        for x,i in enumerate(json.loads(parse_ddl_script(ddl_script)["body"])):
            table= Table.from_json(i)
            result[table.table_name]=[]
            for i in table.get_columns_json_list():
                if (i['references']):
                    generate = fake.get_provider_for_data_type(i["type"],i["size"],rows,i["references"].column)
                    result[table.table_name].append(f"{fake.data_type}:{generate}")
                else:
                    generate = fake.get_provider_for_data_type(i["type"], i["size"], rows)
                    result[table.table_name].append(f"{fake.data_type}:{generate}")


        return result
    else:
        pass
print(generate_data("YES"))