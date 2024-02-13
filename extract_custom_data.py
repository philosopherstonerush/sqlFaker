class ColumnEx:
    def __init__(self, name, provider=None):
        self.name = name
        self.provider = provider

    def set_provider(self, provider):
        self.provider = provider

    def __str__(self):
        return self.name


class TableEx:
    def __init__(self, name):
        self.name = name
        self.column_obj_dict = {}

    def add_column(self, column_name, column_data):
        col = ColumnEx(column_name, column_data["subprovider"])
        self.column_obj_dict[col.name] = col

    def ret_col_obj(self):
        return self.column_obj_dict


class TableDatabase:
    def __init__(self, data):
        self.table_obj = {}
        self.extract_tables(data)

    def extract_tables(self, data):
        for table_name, columns in data.items():
            table = TableEx(table_name)
            for dictionary in columns:
                for column_name, column_data in dictionary.items():
                    table.add_column(column_name, column_data)
                self.table_obj[table_name] = table

    def ret_table_obj(self):
        return self.table_obj


"""
    "consultants": [
        {
            "id": {
                "subprovider": "NONE",
                "provider": "NONE"
            }
        },
        {
            "first_name": {
                "subprovider": "NONE",
                "provider": "NONE"
            }
        },
        {
            "last_name": {
                "subprovider": "NONE",
                "provider": "NONE"
            }
        },
        {
            "email": {
                "subprovider": "NONE",
                "provider": "NONE"
            }
        },
        {
            "departments_id": {
                "subprovider": "NONE",
                "provider": "NONE"
            }
        },
        {
            "contract_date": {
                "subprovider": "NONE",
                "provider": "NONE"
            }
        }
    ]
}"""