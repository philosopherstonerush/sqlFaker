import datetime

from constants import MySQLDataType, PostgreSqlDataType, OracleDataType, MSSQLDataType
from faker import Faker

fake = Faker()


# custom generation code

def intrange_custom(params=None):
    lowerBound = fake.pyint(**params)
    return f"[{lowerBound}, {lowerBound + fake.pyint()}]"


def numrange_custom(params=None):
    number = fake.pyfloat(left_digits=2, right_digits=1)
    number_to_add = fake.pyfloat(left_digits=1, right_digits=1)
    return f"[{number}, {number + number_to_add})"


def daterange_custom(params=None):
    date = fake.date()
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    time_delta = datetime.timedelta(days=30)
    date_future_obj = date_obj + time_delta
    return f"[{date_obj.date()}, {date_future_obj.date()}]"


def multiintrange_custom(params=None):
    if params:
        return f"[{intrange_custom(params)}, {intrange_custom(params)}]"
    else:
        raise Exception("multirange_custom is given None as a parameter")


def multinumrange_custom(params=None):
    return f"[{numrange_custom(params)}, {numrange_custom(params)}]"


def multidaterange_custom(params=None):
    return f"[{daterange_custom(params)}, {daterange_custom(params)}]"


data_func_map = {
    MySQLDataType.BIGINT.value[0]: {"func": fake.pyint,
                                    "params": {"min_value": 0, "max_value": 9223372036854775808, "step": 1}},
    MySQLDataType.BINARY.value[0]: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 1, "step": 1}},
    MySQLDataType.BIT.value[0]: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 1, "step": 1}},
    MySQLDataType.BLOB.value[0]: {"func": fake.binary, "params": {"length": 30}},
    MySQLDataType.BOOLEAN.value[0]: {"func": fake.pybool, "params": {"truth_probability": 50}},
    MySQLDataType.CHAR.value[0]: {"func": fake.bothify, "params": {"text": "?"}},
    MySQLDataType.DATE.value[0]: {"func": fake.date, "params": {"pattern": '%Y-%m-%d'}},
    MySQLDataType.DATETIME.value[0]: {"func": fake.date_time, "params": {}},
    MySQLDataType.DECIMAL.value[0]: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.DOUBLE.value[0]: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.FLOAT.value[0]: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.INTEGER.value[0]: {"func": fake.pyint,
                                     "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    "INT": {"func": fake.pyint, "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MySQLDataType.JSON.value[0]: {"func": fake.json, "params": {}},
    MySQLDataType.LONGBLOB.value[0]: {"func": fake.binary, "params": {"length": 104}},
    MySQLDataType.LONGTEXT.value[0]: {"func": fake.sentence, "params": {}},
    MySQLDataType.MEDIUMBLOB.value[0]: {"func": fake.binary, "params": {"length": 104}},
    MySQLDataType.MEDIUMINT.value[0]: {"func": fake.pyint,
                                       "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MySQLDataType.MEDIUMTEXT.value[0]: {"func": fake.sentence, "params": {}},
    MySQLDataType.NCHAR.value[0]: {"func": fake.sentence, "params": {}},
    MySQLDataType.NVCHAR.value[0]: {"func": fake.sentence, "params": {}},
    MySQLDataType.NUMBERIC.value[0]: {"func": fake.pyint,
                                      "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    OracleDataType.NUMBER.value[0]: {"func": fake.pyint,
                                     "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MySQLDataType.SET.value[0]: {"func": fake.pyset, "params": {}},
    MySQLDataType.SMALLINT.value[0]: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 32767, "step": 1}},
    MySQLDataType.REAL.value[0]: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.TEXT.value[0]: {"func": fake.sentence, "params": {}},
    MySQLDataType.TIME.value[0]: {"func": fake.time, "params": {"pattern": "%H:%M:%S"}},
    MySQLDataType.TIMESTAMP.value[0]: {"func": fake.unix_time, "params": {}},
    MySQLDataType.TINYBLOB.value[0]: {"func": fake.binary, "params": {"length": 10}},
    MySQLDataType.TINYINT.value[0]: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 255, "step": 1}},
    MySQLDataType.TINYTEXT.value[0]: {"func": fake.text, "params": {"max_nb_chars": 200}},
    MySQLDataType.VARBINARY.value[0]: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 1, "step": 1}},
    MySQLDataType.VARCHAR.value[0]: {"func": fake.word, "params": {}},
    MySQLDataType.YEAR.value[0]: {"func": fake.year, "params": {}},
    PostgreSqlDataType.INET.value[0]: {"func": fake.ipv4, "params": {"address_class": "c"}},
    PostgreSqlDataType.CIDR.value[0]: {"func": fake.ipv4, "params": {"address_class": "c"}},
    PostgreSqlDataType.CITEXT.value[0]: {"func": fake.pystr, "params": {}},
    PostgreSqlDataType.UUID.value[0]: {"func": fake.uuid4, "params": {}},
    PostgreSqlDataType.MACADDR.value[0]: {"func": fake.hexify, "params": {"text": '^^:^^:^^:^^:^^:^^'}},
    PostgreSqlDataType.MACADDR8.value[0]: {"func": fake.hexify, "params": {"text": '"^^:^^:^^:^^:^^:^^:^^:^^"'}},
    PostgreSqlDataType.OID.value[0]: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 255, "step": 1}},
    PostgreSqlDataType.REGCLASS.value[0]: {"func": fake.language_name, "params": {}},
    PostgreSqlDataType.REGCONFIG.value[0]: {"func": fake.language_name, "params": {}},
    PostgreSqlDataType.DOUBLE_PRECISION.value[0]: {"func": fake.pyfloat,
                                                   "params": {"min_value": None, "max_value": None}},
    PostgreSqlDataType.BYTEA.value[0]: {"func": fake.binary, "params": {"length": 255}},
    PostgreSqlDataType.INTERVAL.value[0]: {"func": fake.bothify, "params": {"text": "# hours"}},
    PostgreSqlDataType.ARRAY.value[0]: {"func": fake.pylist, "params": {}},
    PostgreSqlDataType.HSTORE.value[0]: {"func": fake.pyset, "params": {}},
    PostgreSqlDataType.INT4RANGE.value[0]: {"func": intrange_custom,
                                            "params": {"min_value": 0, "max_value": 2000000000, "step": 1}},
    PostgreSqlDataType.INT8RANGE.value[0]: {"func": intrange_custom,
                                            "params": {"min_value": 0, "max_value": 9000000000000000, "step": 1}},
    PostgreSqlDataType.NUMRANGE.value[0]: {"func": numrange_custom, "params": {}},
    PostgreSqlDataType.DATERANGE.value[0]: {"func": daterange_custom, "params": {}},
    PostgreSqlDataType.INT4MULTIRANGE.value[0]: {"func": multiintrange_custom,
                                                 "params": {"min_value": 0, "max_value": 2000000000, "step": 1}},
    PostgreSqlDataType.INT8MULTIRANGE.value[0]: {"func": multiintrange_custom,
                                                 "params": {"min_value": 0, "max_value": 9000000000000000, "step": 1}},
    PostgreSqlDataType.NUMMULTIRANGE.value[0]: {"func": multinumrange_custom, "params": {}},
    PostgreSqlDataType.DATEMULTIRANGE.value[0]: {"func": multidaterange_custom, "params": {}},
    PostgreSqlDataType.JSONB.value[0]: {"func": fake.json_bytes, "params": {}},
    OracleDataType.BFILE.value[0]: {"func": fake.binary, "params": {}},
    OracleDataType.CLOB.value[0]: {"func": fake.pystr, "params": {}},
    OracleDataType.NCLOB.value[0]: {"func": fake.pystr, "params": {}},
    OracleDataType.RAW.value[0]: {"func": fake.binary, "params": {}},
    OracleDataType.BINARY_DOUBLE.value[0]: {"func": fake.pyfloat,
                                            "params": {"min_value": -9.9999999999999,
                                                       "max_value": 9.9999999999999999}},
    OracleDataType.BINARY_FLOAT.value[0]: {"func": fake.pyfloat,
                                           "params": {"min_value": -9.99999999999, "max_value": 9.99999999999}},
    OracleDataType.LONG.value[0]: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    OracleDataType.NVARCHAR2.value[0]: {"func": fake.word, "params": {}},
    OracleDataType.ROWID.value[0]: {"func": fake.pystr, "params": {}},
    MSSQLDataType.DATETIME2.value[0]: {"func": fake.date, "params": {"pattern": '%Y-%m-%d'}},
    MSSQLDataType.DATETIMEOFFSET.value[0]: {"func": fake.date_time, "params": {}},
    MSSQLDataType.SMALLDATETIME.value[0]: {"func": fake.date, "params": {"pattern": '%Y-%m-%d'}},
    MSSQLDataType.ROWVERSION.value[0]: {"func": fake.binary, "params": {}},
    MSSQLDataType.UNIQUEIDENTIFIER.value[0]: {"func": fake.hexify, "params": {"text": "^^^^-^^^-^^^^-^^^^-^^^-^^^^"}},
    MSSQLDataType.SQL_VARIANT.value[0]: {"func": fake.pyint,
                                         "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MSSQLDataType.XML.value[0]: {"func": fake.xml, "params": {}},
    "SERIAL": {"func": fake.pyint, "params": {"min_value": 0, "max_value": 200000000, "step": 1}},
}


def get_func_for_data_type(data_type):
    func = data_func_map.get(data_type, None)
    if func:
        return func
    else:
        raise Exception("Cannot find the required data type")
