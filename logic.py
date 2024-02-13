import json
import sys

from data_type_match import get_func_for_data_type
from simple_ddl_parser import DDLParser
from services import AWSResponse, Table, Reference, Column, Result
from custom_providers import provider_dict_map, get_provider_function
from extract_custom_data import TableDatabase

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
        for i in range(len(tables_list)):
            if tables_list[i]:
                tables_list[i] = SPLIT_SUBSTRING + tables_list[i]
        parsed_result = []
        for elem in tables_list:
            if elem != "":
                parse = DDLParser(elem, silent=True).run(output_mode="sql")
                if parse and "comments" not in parse[0]:
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
            body=json.dumps(e.__cause__)
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


def generate_data(ddl_script, custom_data=None, size=10, opt=False):
    try:
        if custom_data:
            db = TableDatabase(custom_data)
            table_obj_dict = db.ret_table_obj()  # {'table_name1': <object>, 'table_name2': <object>}

        rows_to_generate = size

        # {table_name: {col_name_1: res_obj_1, col_name_2: res_obj_2}
        result = dict()
        parsed_info = parse_ddl_script(ddl_script)

        table_objs = []

        # {ref_table_name: {ref_col_name: res_obj_current}
        col_with_references = dict()

        for elem in parsed_info:
            if "comments" not in elem:
                table_objs.append(Table.from_json(elem))

        for table in table_objs:
            result.update({table.get_table_name(): dict()})

        for table in table_objs:

            table_name = table.get_table_name()
            table_columns = table.get_columns_objs()
            primary_key = table.get_primary_key()

            if custom_data:
                table_obj = table_obj_dict[table_name]
                col_obj_dict = table_obj.ret_col_obj()  # {"colname1': <object>, 'colname2': <object>}

            for col in table_columns:

                column_name = col.get_name()
                is_referenced = False
                col_in_custom_data = False
                has_references = False
                is_primary_key = False

                if custom_data:
                    col_in_custom_data = True if column_name in col_obj_dict.keys() else False

                res_obj = Result(table_name, column_name)

                if primary_key == column_name:
                    is_primary_key = True
                if col.get_references() is not None:
                    has_references = True
                if col_with_references.get(table_name, None) is not None:
                    cols_references = col_with_references.get(table_name)
                    if column_name in cols_references:
                        is_referenced = True
                is_referring_table_provided = False

                if has_references:
                    ref = col.get_references()

                    is_referring_table_provided = True if result.get(ref.get_table_name(), None) is not None else False

                if is_referring_table_provided:
                    already_have_value = result.get(ref.get_table_name()).get(ref.get_column_name(), None)
                    if already_have_value is not None:
                        res_obj.set_generated_data_list(already_have_value.get_generated_data_list())
                        result.get(table_name).update({column_name: res_obj})
                    else:
                        col_with_references.update({ref.get_table_name(): {ref.get_column_name(): res_obj}})
                        result.get(table_name).update({column_name: res_obj})
                    continue

                if is_primary_key:
                    col.set_unique_true()
                    col.set_nullable_false()

                if col_in_custom_data:
                    generated_data = _get_data(col, rows_to_generate, col_obj_dict[column_name].provider)
                else:
                    generated_data = _get_data(col, rows_to_generate)
                res_obj.set_generated_data_list(generated_data)
                result.get(table_name).update({column_name: res_obj})

                if is_referenced is True:
                    referring_res_obj = col_with_references.get(table_name).get(column_name)
                    referring_res_obj.set_generated_data_list(generated_data)

        for table in result:
            for key in result[table]:
                value = result[table][key]
                result[table][key] = value.get_generated_data_list()

        if opt:
            return AWSResponse(
                status_code=200,
                body=json.dumps(result)
            ).get_json_response()
        else:
            return result
    except Exception as e:
        return AWSResponse(
            status_code=400,
            body=json.dumps(e.__cause__)
        ).get_json_response()


def _get_data(col, size, subprovider=None):
    if subprovider:
        if col.get_autoincrement():
            subprovider = "SERIAL"
            func, param = get_provider_function(subprovider)
            res = []
            for i in range(size):
                value = func(None if i == 0 else value)
                res.append(value)
            return res
        func, param = get_provider_function(subprovider)
        res = []
        for _ in range(size):
            res.append(func(**param))
        return res
    else:
        data_type = col.get_type()
        if col.get_autoincrement():
            data_type = "SERIAL"
        generator = get_func_for_data_type(data_type)
        func = generator.get("func")
        params = generator.get("params")

        if data_type == "SERIAL":
            return func(params)
        else:
            res = []
            if "custom" in func.__name__:
                for _ in range(size):
                    res.append(func(params))
            else:
                for _ in range(size):
                    res.append(func(**params))
            return res
