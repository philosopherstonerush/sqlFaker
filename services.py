

"""

Write methods that manipulate Table and column info here

"""


class Table:

    def __init__(self, columns, primary_key, alter, checks, index, partitioned_by, tablespace, schema, table_name):
        self.columns = columns
        self.primary_key = primary_key
        self.alter = alter
        self.checks = checks
        self.index = index
        self.partitioned_by = partitioned_by
        self.tablespace = tablespace
        self.schema = schema
        self.table_name = table_name

    def add_columns(self, cols):
        """
        adds a list of columns objs
        :param cols: Column objects
        :return: None
        """

        self.columns.extend(cols)

    def get_columns_json_list(self):
        temp = []
        for elem in self.columns:
            res = elem.get_json_response()
            temp.append(res)
        return temp

    def __str__(self):
        temp_list = [str(x) for x in self.columns]
        return str(temp_list)

    def get_json_response(self):
        temp = []
        for elem in self.columns:
            res = elem.get_json_response()
            temp.append(res)
        return self.__dict__

    @staticmethod
    def from_json(json_dict):
        return Table(
            [Column.from_json(x) for x in json_dict["columns"]],
            json_dict["primary_key"],
            json_dict["alter"],
            json_dict["checks"],
            json_dict["index"],
            json_dict["partitioned_by"],
            json_dict["tablespace"],
            json_dict["schema"],
            json_dict["table_name"]
        )


class Column:

    def __init__(self, name, type, size, references, unique, nullable, default, check):
        self.name = name
        self.type = type
        self.size = size
        self.references = references
        self.unique = unique
        self.nullable = nullable
        self.default = default
        self.check = check

        self.generated_data = None

    def generate_data(self):
        pass

    def get_json_response(self):
        return self.__dict__

    def __str__(self):
        # TODO: Can improve this
        return "check " + self.check + "name " + self.name

    # Return column instances
    @staticmethod
    def from_json(json_dict):
        return Column(
            json_dict["name"],
            json_dict["type"],
            json_dict["size"],
            Reference.from_json(json_dict["references"]),
            json_dict["unique"],
            json_dict["nullable"],
            json_dict["default"],
            json_dict["check"]
        )


class Reference:

    def __init__(self, table="", schema="", on_delete="", on_update="", deferrable_initially="", column=""):
        self.table = table
        self.schema = schema
        self.on_delete = on_delete
        self.on_update = on_update
        self.deferrable_initially = deferrable_initially
        self.column = column

    @staticmethod
    def from_json(json_dict):
        try:
            if len(json_dict) != 0:
                # Returns references instances
                return Reference(
                    json_dict["table"],
                    json_dict["schema"],
                    json_dict["on_delete"],
                    json_dict["on_update"],
                    json_dict["deferrable_initially"],
                    json_dict["column"],
                )
        except Exception:
            return None


class AWSResponse:

    def __init__(self, status_code=400, body=""):
        self.statusCode = status_code
        self.headers = {
            "Content-Type": "application/json"
        }
        if isinstance(body, str):
            self.body = body
        else:
            self.body = ""

        self.isBase64Encoded = False

    def set_body(self, body):
        if isinstance(body, str):
            self.body = body
        else:
            raise Exception("Invalid type")

    def set_status_code(self, status):
        if isinstance(status, int):
            self.statusCode = status
        else:
            raise Exception("Invalid type")

    def get_json_response(self):

        return self.__dict__
