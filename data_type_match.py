from constants import MySQLDataType, PostgreSqlDataType, OracleDataType, MSSQLDataType
from faker import Faker


class GenData(Faker):
    def __init__(self):
        super().__init__()
        self.data_type_mapping = {
            MySQLDataType.BIGINT.value: lambda: self.pyint(0, 9223372036854775808),
            MySQLDataType.BINARY.value: lambda: self.pyint(0, 1),
            MySQLDataType.BIT.value: lambda: self.pyint(0, 1),
            MySQLDataType.BLOB.value: lambda: self.binary(),
            MySQLDataType.BOOLEAN.value: lambda: self.pybool(),
            MySQLDataType.CHAR.value: lambda: self.name(),
            MySQLDataType.DATE.value: lambda: self.date_between(1753 - 1 - 1, 9999 - 12 - 31),
            MySQLDataType.DATETIME.value: lambda: self.date_time_between(1753 - 1 - 1, 9999 - 12 - 31),
            MySQLDataType.DECIMAL.value: lambda: self.pyfloat(min_value=0, max_value=214748.3647),
            MySQLDataType.DOUBLE.value: lambda: self.pyfloat(min_value=0, max_value=214748.3647),
            MySQLDataType.ENUM.value: lambda: self.enum(MySQLDataType),
            MySQLDataType.FLOAT.value: lambda: self.pyfloat(min_value=0, max_value=214748.3647),
            MySQLDataType.INTEGER.value: lambda: self.pyint(0, 2147483647),
            "INT": lambda: self.pyint(0, 2147483647),
            MySQLDataType.JSON.value: lambda: self.json(),
            MySQLDataType.LONGBLOB.value: lambda: self.binary(),
            MySQLDataType.LONGTEXT.name: lambda: self.sentence(),
            MySQLDataType.MEDIUMBLOB.name: lambda: self.binary(),
            MySQLDataType.MEDIUMINT.name: lambda: self.pyint(0, 8388607),
            MySQLDataType.MEDIUMTEXT.name: lambda: self.text(16777215),
            MySQLDataType.NCHAR.name: lambda: self.name(),
            MySQLDataType.NVCHAR.name: lambda: self.word(),
            MySQLDataType.NUMBERIC.name: lambda: self.pyint(),
            "NUMBER": lambda: self.pyint(),
            "SET": lambda: self.enum(MySQLDataType),
            "SMALLINT": lambda: self.pyint(0, 32767),
            "REAL": lambda: self.pyfloat(),
            "TEXT": lambda: self.name,
            "TIME": lambda: self.time(),
            "TIMESTAMP": lambda: f"{self.date_time_between()}{self.timezone()}",
            "TINYBLOB": lambda: self.binary(),
            "TINYINT": lambda: self.pyint(0, 255),
            "TINYTEXT": lambda: self.text(255),
            "VARBINARY": lambda: self.pyint(0, 1),
            "VARCHAR": lambda: self.word(),
            "YEAR": lambda: self.year(),
            "INET": lambda: self.ipv6(),
            "CIDR": lambda: self.ipv4(),
            "CITEXT": lambda: self.pystr().lower(),
            "UUID": lambda: self.uuid4(),
            "MACADDR": lambda: self.mac_address(),
            "MACADDR8": lambda: self.hexify("^^:^^:^^:^^:^^:^^:^^:^^"),
            "OID": lambda: self.pyint(),
            "REGCLASS": lambda: self.name(),
            "REGCONFIG": lambda: self.language_name(),
            "DOUBLE_PRECISION": lambda: self.pyfloat(right_digits=15),
            "BYTEA": lambda: self.binary(),
            "INTERVAL": lambda: self.time(),
            "ARRAY": lambda: self.texts(),
            "HSTORE": lambda: self.json_bytes(),
            "INT4RANGE": lambda: f"[{self.pyint(1, 100)},{self.pyint(101, 200)}]",
            "INT8RANGE": lambda: f"[{self.pyint(1, 1000)},{self.pyint(1001, 2000)}]",
            "NUMRANGE": lambda: f"[{self.pyint(1.0, 100.0)},{self.pyint(100.0, 200.0)}]",
            "DATERANGE": lambda: f"[{self.date_between(1753 - 1 - 1, 9999 - 12 - 31)},{self.date_between(1753 - 1 - 1, 9999 - 12 - 31)}]",
            "INT4MULTIRANGE": lambda: f"[[{self.pyint(1, 100)},{self.pyint(101, 200)}],[{self.pyint(1, 100)},{self.pyint(101, 200)}]]",
            "INT8MULTIRANGE": lambda: f"[[{self.pyint(1, 1000)},{self.pyint(1001, 2000)}],[{self.pyint(1, 1000)},{self.pyint(1001, 2000)}]]",
            "NUMMULTIRANGE": lambda: f"[[{self.pyint(1.0, 100.0)},{self.pyint(100.0, 200.0)}],[{self.pyint(1.0, 100.0)},{self.pyint(100.0, 200.0)}]]",
            "DATEMULTIRANGE": lambda: f"[[{self.date_between(1753 - 1 - 1, 9999 - 12 - 31)},{self.date_between(1753 - 1 - 1, 9999 - 12 - 31)}],[{self.date_between(1753 - 1 - 1, 9999 - 12 - 31)},{self.date_between(1753 - 1 - 1, 9999 - 12 - 31)}]]",
            "TSVECTOR": lambda: f"'{self.text()}'::tsvector",
            "TSQUERY": lambda: "&".join([self.word() for _ in range(3)]),
            "TSMULTIRANGE": lambda: f"[[{self.date_time_between()},{self.date_time_between()}],[{self.date_time_between()},{self.date_time_between()}]]",
            "TSTZMULTIRANGE": lambda: f"[[{self.date_time_between()}{self.timezone()},{self.date_time_between()}{self.timezone()}],[{self.date_time_between()}{self.timezone()},{self.date_time_between()}{self.timezone()}]]",
            "TSRANGE": lambda: f"[{self.date_time_between()},{self.date_time_between()}]",
            "TSZTRANGE": lambda: f"[{self.date_time_between()}{self.timezone()},{self.date_time_between()}{self.timezone()}]",
            "JSONB": lambda: self.json_bytes(),
            "BFILE": lambda: self.binary(),
            "CLOB": lambda: self.pystr(214483647),
            "NCLOB": lambda: self.pystr(2147483647),
            "RAW": lambda: self.binary(),
            "BINARY_DOUBLE": lambda: self.pyfloat(min_value=-9.999999999999999999999999,
                                                  max_value=9.9999999999999999999999),
            "BINARY_FLOAT": lambda: self.pyfloat(min_value=-9.99999999999, max_value=9.9999999999),
            "LONG": lambda: self.pyfloat(),
            "NVARCHAR2": lambda: self.word(),
            "ROWID": lambda: self.pystr(),
            "DATETIME2": lambda: self.date_time_between(1753 - 1 - 1, 9999 - 12 - 31),
            "DATETIMEOFFSET": lambda: self.date_time(),
            "SMALLDATETIME": lambda: self.date_time_between(1900 - 1 - 1, 2079 - 6 - 6),
            "ROWVERSION": lambda: self.binary(),
            "UNIQUEIDENTIFIER": lambda: self.hexify("^^^^-^^^-^^^^-^^^^-^^^-^^^^"),
            "SQL_VARIANT": lambda: self.pyint(),
            "XML": lambda: self.xml(),
            "SERIAL": lambda: self.pyint(1, 2147483647)
        }

    def get_provider_for_data_type(self, data_type, charsize, samplesize):
        self.data_type = data_type.upper()
        data = self.data_type_mapping.get(data_type.upper(), self.sentence)
        return [str(data())[:charsize] for _ in range(samplesize)]

    def foreign_keymap(self, result, tablename, colname, samplesize):
        return [result[tablename][colname][i] for i in range(samplesize)]

    def AutoIncrement(self, d_type, size, samplesize):
        value = str(self.data_type_mapping[d_type.upper()]())[:size]
        r = []
        for _ in range(samplesize):
            value = int(value) + 1
            r.append(value)
        return r
