from simple_ddl_parser import DDLParser


"""

Given sql DDL script, return list of
    - Attribute Name
    - Attribute Datatype

    TODO: add more above if appropriate

"""


def parse_ddl_script(ddl):
    parse = DDLParser(ddl)
    print(parse.run())


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
