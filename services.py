"""

Write methods that manipulate Table and column info here

"""


class Table:

    def __init__(self, columns):
        self.columns = columns

    def add_columns(self, cols):
        self.columns.extend(cols)

    def __str__(self):
        temp_list = [str(x) for x in self.columns]
        return str(temp_list)


class Column:

    def __init__(self, check, data_type, name, nullable, unique):
        self.check = check
        self.data_type = data_type
        self.name = name
        self.nullable = nullable
        self.unique = unique

    def __str__(self):
        # TODO: Can improve this
        return "check " + self.check + "name " + self.name

class AWSResponse:

    def __init__(self, statusc_code, headers, body, isBase64Encoded):
        pass
