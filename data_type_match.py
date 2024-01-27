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
        return f"[{intrange_custom(**params)}, {intrange_custom(**params)}]"
    else:
        raise Exception("multirange_custom is given None as a parameter")


def multinumrange_custom(params=None):
    if params:
        return f"[{numrange_custom(**params)}, {numrange_custom(**params)}]"
    else:
        raise Exception("multinumrange_custom is given None as a parameter")


def multidaterange_custom(params=None):
    if params:
        return f"[{daterange_custom(**params)}, {daterange_custom(**params)}]"
    else:
        raise Exception("multidaterange_custom is given None as a parameter")


data_func_map = {
    MySQLDataType.BIGINT.value: {"func": fake.pyint,
                                 "params": {"min_value": 0, "max_value": 9223372036854775808, "step": 1}},
    MySQLDataType.BINARY.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 1, "step": 1}},
    MySQLDataType.BIT.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 1, "step": 1}},
    MySQLDataType.BLOB.value: {"func": fake.binary, "params": {"length": 1048576}},
    MySQLDataType.BOOLEAN.value: {"func": fake.pybool, "params": {"truth_probability": 50}},
    MySQLDataType.CHAR.value: {"func": fake.bothify, "params": {"text": "?"}},
    MySQLDataType.DATE.value: {"func": fake.date, "params": {"pattern": '%Y-%m-%d'}},
    MySQLDataType.DATETIME.value: {"func": fake.date_time, "params": {}},
    MySQLDataType.DECIMAL.value: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.DOUBLE.value: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.FLOAT.value: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.INTEGER.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    "INT": {"func": fake.pyint, "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MySQLDataType.JSON.value: {"func": fake.json, "params": {}},
    MySQLDataType.LONGBLOB.value: {"func": fake.binary, "params": {"length": 1048576}},
    MySQLDataType.LONGTEXT.value: {"func": fake.sentence, "params": {}},
    MySQLDataType.MEDIUMBLOB.value: {"func": fake.binary, "params": {"length": 1048576}},
    MySQLDataType.MEDIUMINT.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MySQLDataType.MEDIUMTEXT.value: {"func": fake.sentence, "params": {}},
    MySQLDataType.NCHAR.value: {"func": fake.sentence, "params": {}},
    MySQLDataType.NVCHAR.value: {"func": fake.sentence, "params": {}},
    MySQLDataType.NUMBERIC.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    OracleDataType.NUMBER.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MySQLDataType.SET.value: {"func": fake.pyset, "params": {}},
    MySQLDataType.SMALLINT.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 32767, "step": 1}},
    MySQLDataType.REAL.value: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    MySQLDataType.TEXT.value: {"func": fake.sentence, "params": {}},
    MySQLDataType.TIME.value: {"func": fake.time, "params": {"pattern": "%H:%M:%S"}},
    MySQLDataType.TIMESTAMP.value: {"func": fake.unix_time, "params": {}},
    MySQLDataType.TINYBLOB.value: {"func": fake.binary, "params": {"length": 1048576}},
    MySQLDataType.TINYINT.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 255, "step": 1}},
    MySQLDataType.TINYTEXT.value: {"func": fake.text, "params": {"max_nb_chars": 200}},
    MySQLDataType.VARBINARY.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 1, "step": 1}},
    MySQLDataType.VARCHAR.value: {"func": fake.word, "params": {}},
    MySQLDataType.YEAR.value: {"func": fake.year, "params": {}},
    PostgreSqlDataType.INET.value: {"func": fake.ipv4, "params": {"address_class": "c"}},
    PostgreSqlDataType.CIDR.value: {"func": fake.ipv4, "params": {"address_class": "c"}},
    PostgreSqlDataType.CITEXT.value: {"func": fake.pystr, "params": {}},
    PostgreSqlDataType.UUID.value: {"func": fake.uuid4, "params": {}},
    PostgreSqlDataType.MACADDR.value: {"func": fake.hexify, "params": {"text": '^^:^^:^^:^^:^^:^^'}},
    PostgreSqlDataType.MACADDR8.value: {"func": fake.hexify, "params": {"text": '"^^:^^:^^:^^:^^:^^:^^:^^"'}},
    PostgreSqlDataType.OID.value: {"func": fake.pyint, "params": {"min_value": 0, "max_value": 255, "step": 1}},
    PostgreSqlDataType.REGCLASS.value: {"func": fake.language_name, "params": {}},
    PostgreSqlDataType.REGCONFIG.value: {"func": fake.language_name, "params": {}},
    PostgreSqlDataType.DOUBLE_PRECISION.value: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    PostgreSqlDataType.BYTEA.value: {"func": fake.binary, "params": {"length": 255}},
    PostgreSqlDataType.INTERVAL.value: {"func": fake.bothify, "params": {"text": "# hours"}},
    PostgreSqlDataType.ARRAY.value: {"func": fake.pylist, "params": {}},
    PostgreSqlDataType.HSTORE.value: {"func": fake.pyset, "params": {}},
    PostgreSqlDataType.INT4RANGE.value: {"func": intrange_custom,
                                         "params": {"min_value": 0, "max_value": 2000000000, "step": 1}},
    PostgreSqlDataType.INT8RANGE.value: {"func": intrange_custom,
                                         "params": {"min_value": 0, "max_value": 9000000000000000, "step": 1}},
    PostgreSqlDataType.NUMRANGE.value: {"func": numrange_custom, "params": {}},
    PostgreSqlDataType.DATERANGE.value: {"func": daterange_custom, "params": {}},
    PostgreSqlDataType.INT4MULTIRANGE.value: {"func": multiintrange_custom,
                                              "params": {"min_value": 0, "max_value": 2000000000, "step": 1}},
    PostgreSqlDataType.INT8MULTIRANGE.value: {"func": multiintrange_custom,
                                              "params": {"min_value": 0, "max_value": 9000000000000000, "step": 1}},
    PostgreSqlDataType.NUMMULTIRANGE.value: {"func": multinumrange_custom, "params": {}},
    PostgreSqlDataType.DATEMULTIRANGE.value: {"func": multidaterange_custom, "params": {}},
    PostgreSqlDataType.JSONB.value: {"func": fake.json_bytes, "params": {}},
    OracleDataType.BFILE.value: {"func": fake.binary, "params": {}},
    OracleDataType.CLOB.value: {"func": fake.pystr, "params": {}},
    OracleDataType.NCLOB.value: {"func": fake.pystr, "params": {}},
    OracleDataType.RAW.value: {"func": fake.binary, "params": {}},
    OracleDataType.BINARY_DOUBLE.value: {"func": fake.pyfloat,
                                         "params": {"min_value": -9.9999999999999, "max_value": -9.9999999999999999}},
    OracleDataType.BINARY_FLOAT.value: {"func": fake.pyfloat,
                                        "params": {"min_value": -9.99999999999, "max_value": -9.99999999999}},
    OracleDataType.LONG.value: {"func": fake.pyfloat, "params": {"min_value": None, "max_value": None}},
    OracleDataType.NVARCHAR2.value: {"func": fake.word, "params": {}},
    OracleDataType.ROWID.value: {"func": fake.pystr, "params": {}},
    MSSQLDataType.DATETIME2.value: {"func": fake.date, "params": {"pattern": '%Y-%m-%d'}},
    MSSQLDataType.DATETIMEOFFSET.value: {"func": fake.date_time, "params": {}},
    MSSQLDataType.SMALLDATETIME.value: {"func": fake.date, "params": {"pattern": '%Y-%m-%d'}},
    MSSQLDataType.ROWVERSION.value: {"func": fake.binary, "params": {}},
    MSSQLDataType.UNIQUEIDENTIFIER.value: {"func": fake.hexify, "params": {"text": "^^^^-^^^-^^^^-^^^^-^^^-^^^^"}},
    MSSQLDataType.SQL_VARIANT.value: {"func": fake.pyint,
                                      "params": {"min_value": 0, "max_value": 2147483647, "step": 1}},
    MSSQLDataType.XML.value: {"func": fake.xml, "params": {}},
    "SERIAL": {"func": fake.pyint, "params": {"min_value": 0, "max_value": 200000000, "step": 1}},
}


def get_func_for_data_type(data_type):
    func = data_func_map.get(data_type, None)
    if func:
        return func
    else:
        raise Exception
