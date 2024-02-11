from faker import Faker
from constants import MySQLDataType
fake = Faker()
from datetime import datetime
 
start_Date=datetime(1970,1,1)
end_date = datetime.now()

def Serial_custom(value = None):
       if value is None:
              value=fake.pyint()
       return value+1


provider_dict_map = {
       "address": {"func": fake.address, "param": {}},
       "building_number": {"func": fake.building_number, "param": {}},
       "city": {"func": fake.city, "param": {}},
       "city_suffix": {"func": fake.city_suffix, "param": {}},
       "country": {"func": fake.country, "param": {}},
       "country_code": {"func": fake.country_code, "param": {}},
       "current_country": {"func": fake.current_country, "param": {}},
       "current_country_code": {"func": fake.current_country_code, "param": {}},
       "postcode": {"func": fake.postcode, "param": {}},
       "street_address": {"func": fake.street_address, "param": {}},
       "street_name": {"func": fake.street_name, "param": {}},
       "street_suffix": {"func": fake.street_suffix, "param": {}},
       "licence_plate": {"func": fake.license_plate, "param": {}},
       "vin": {"func": fake.vin, "param": {}},
       "aba": {"func": fake.aba, "param": {}},
       "bank_country": {"func": fake.bank_country, "param": {}},
       "bban": {"func": fake.bban, "param": {}},
       "iban": {"func": fake.iban, "param": {}},
       "swift": {"func": fake.swift, "param": {"length": None}},
       "swift11": {"func": fake.swift11, "param": {}},
       "swift8": {"func": fake.swift8, "param": {}},
       "ean": {"func": fake.ean, "param": {"length": 13}},
       "ean13": {"func": fake.ean13, "param": {}},
       "ean8": {"func": fake.ean8, "param": {}},
       "localized_ean": {"func": fake.localized_ean, "param": {"length": 13}},
       "localized_ean13": {"func": fake.localized_ean13, "param": {}},
       "localized_ean8": {"func": fake.localized_ean8, "param": {}},
       "color": {"func": fake.color, "param": {"hue": None, "luminosity": None}},
       "color_name": {"func": fake.color_name, "param": {}},
       "hex_color": {"func": fake.hex_color, "param": {}},
       "rgb_color": {"func": fake.rgb_color, "param": {}},
       "rgb_css_color": {"func": fake.rgb_css_color, "param": {}},
       "safe_color_name": {"func": fake.safe_color_name, "param": {}},
       "safe_hex_color": {"func": fake.safe_hex_color, "param": {}},
       "bs": {"func": fake.bs, "param": {}},
       "catch_phrase": {"func": fake.catch_phrase, "param": {}},
       "company": {"func": fake.company, "param": {}},
       "company_suffix": {"func": fake.company_suffix, "param": {}},
       "credit_card_expire": {"func": fake.credit_card_expire, "param": {"start": start_Date, "end": end_date}},
       "credit_card_full": {"func": fake.credit_card_full, "param": {"card_type": "mastercard"}},
       "credit_card_number": {"func": fake.credit_card_number, "param": {"card_type": "mastercard"}},
       "credit_card_provider": {"func": fake.credit_card_provider, "param": {"card_type": "mastercard"}},
       "credit_card_security_code": {"func": fake.credit_card_security_code, "param": {"card_type": "mastercard"}},
       "cryptocurrency": {"func": fake.cryptocurrency, "param": {}},
       "cryptocurrency_code": {"func": fake.cryptocurrency_code, "param": {}},
       "cryptocurrency_name": {"func": fake.cryptocurrency_name, "param": {}},
       "currency": {"func": fake.currency, "param": {}},
       "currency_code": {"func": fake.currency_code, "param": {}},
       "currency_name": {"func": fake.currency_name, "param": {}},
       "currency_symbol": {"func": fake.currency_symbol, "param": {}},
       "pricetag": {"func": fake.pricetag, "param": {}},
       "am_pm": {"func": fake.am_pm, "param": {}},
       "century": {"func": fake.century, "param": {}},
       "date": {"func": fake.date, "param": {"pattern": "%Y%m%d", "end_datetime": end_date}},
       "date_between": {"func": fake.date_between, "param": {"start_date": start_Date, "end_date": end_date}},
       "date_of_birth": {"func": fake.date_of_birth, "param": {}},
       "date_this_century": {"func": fake.date_this_century, "param": {}},
       "date_this_decade": {"func": fake.date_this_decade, "param": {}},
       "date_this_month": {"func": fake.date_this_month, "param": {}},
       "date_this_year": {"func": fake.date_this_year, "param": {}},
       "date_time": {"func": fake.date_time, "param": {}},
       "date_time_ad": {"func": fake.date_time_ad, "param": {"start_datetime": start_Date, "end_datetime": end_date}},
       "date_time_between": {"func": fake.date_time_between,
                             "param": {"start_date": start_Date, "end_date": end_date}},
       "date_time_between_dates": {"func": fake.date_time_between_dates,
                                   "param": {"datetime_start": start_Date, "datetime_end": end_date}},
       "date_time_this_century": {"func": fake.date_time_this_century, "param": {}},
       "date_time_this_decade": {"func": fake.date_time_this_decade, "param": {}},
       "date_time_this_month": {"func": fake.date_time_this_month, "param": {}},
       "date_time_this_year": {"func": fake.date_time_this_year, "param": {}},
       "day_of_month": {"func": fake.day_of_month, "param": {}},
       "day_of_week": {"func": fake.day_of_week, "param": {}},
       "future_date": {"func": fake.future_date, "param": {}},
       "future_datetime": {"func": fake.future_datetime, "param": {}},
       "iso8601": {"func": fake.iso8601, "param": {}},
       "month": {"func": fake.month, "param": {}},
       "month_name": {"func": fake.month_name, "param": {}},
       "past_date": {"func": fake.past_date, "param": {"start_date": start_Date}},
       "past_datetime": {"func": fake.past_datetime, "param": {"start_date": start_Date}},
       "pytimezone": {"func": fake.pytimezone, "param": {}},
       "time": {"func": fake.time, "param": {}},
       "time_delta": {"func": fake.time_delta, "param": {}},
       "time_object": {"func": fake.time_object, "param": {}},
       "time_series": {"func": fake.time_series, "param": {"start_date": start_Date, "end_date": end_date}},
       "timezone": {"func": fake.timezone, "param": {}},
       "unix _time": {"func": fake.unix_time, "param": {"start_datetime": start_Date, "end_datetime": end_date}},
       "year": {"func": fake.year, "param": {}},
       "emoji": {"func": fake.emoji, "param": {}},
       "file_extension": {"func": fake.file_extension, "param": {}},
       "file_name": {"func": fake.file_name, "param": {}},
       "file_path": {"func": fake.file_path, "param": {"depth": 1}},
       "mime_type": {"func": fake.mime_type, "param": {}},
       "unix_device": {"func": fake.unix_device, "param": {}},
       "unix_partition": {"func": fake.unix_partition, "param": {}},
       "coordinate": {"func": fake.coordinate, "param": {}},
       "latitude": {"func": fake.latitude, "param": {}},
       "latlng": {"func": fake.latlng, "param": {}},
       "local_latlng": {"func": fake.local_latlng, "param": {}},
       "location_on_land": {"func": fake.location_on_land, "param": {}},
       "longitude": {"func": fake.longitude, "param": {}},
       "ascii_company_email": {"func": fake.ascii_company_email, "param": {}},
       "ascii_email": {"func": fake.ascii_email, "param": {}},
       "ascii_free_email": {"func": fake.ascii_free_email, "param": {}},
       "ascii_safe_email": {"func": fake.ascii_safe_email, "param": {}},
       "company_email": {"func": fake.company_email, "param": {}},
       "dga": {"func": fake.dga, "param": {}},
       "domain_name": {"func": fake.domain_name, "param": {}},
       "domain_word": {"func": fake.domain_word, "param": {}},
       "email": {"func": fake.email, "param": {}},
       "free_email": {"func": fake.free_email, "param": {}},
       "free_email_domain": {"func": fake.free_email_domain, "param": {}},
       "hostname": {"func": fake.hostname, "param": {}},
       "http_method": {"func": fake.http_method, "param": {}},
       "iana_id": {"func": fake.iana_id, "param": {}},
       "image_url": {"func": fake.emoji, "param": {}},
       "ipv4": {"func": fake.ipv4, "param": {}},
       "ipv4_network_class": {"func": fake.ipv4_network_class, "param": {}},
       "ipv4_private": {"func": fake.ipv4_private, "param": {"address_class": {}}},
       "ipv4_public": {"func": fake.ipv4_public, "param": {"address_class": None}},
       "ipv6": {"func": fake.ipv6, "param": {}},
       "mac_address": {"func": fake.mac_address, "param": {}},
       "nic_handle": {"func": fake.nic_handle, "param": {}},
       "nic_handles": {"func": fake.nic_handles, "param": {"count": 1}},
       "port_number": {"func": fake.port_number, "param": {}},
       "ripe_id": {"func": fake.port_number, "param": {}},
       "safe_domain_name": {"func": fake.safe_domain_name, "param": {}},
       "safe_email": {"func": fake.safe_email, "param": {}},
       "slug": {"func": fake.slug, "param": {}},
       "tld": {"func": fake.tld, "param": {}},
       "uri": {"func": fake.uri, "param": {}},
       "uri_extension": {"func": fake.uri_extension, "param": {}},
       "uri_page": {"func": fake.uri_page, "param": {}},
       "uri_path": {"func": fake.uri_path, "param": {"deep": {}}},
       "url": {"func": fake.url, "param": {}},
       "user_name": {"func": fake.user_name, "param": {}},
       "isbn10": {"func": fake.isbn10, "param": {"separator": "-"}},
       "isbn13": {"func": fake.isbn13, "param": {"separator": "-"}},
       "job": {"func": fake.job, "param": {}},
       "paragraph": {"func": fake.paragraph, "param": {"nb_sentences": 3}},
       "paragraphs": {"func": fake.paragraphs, "param": {"nb": 3}},
       "sentence": {"func": fake.sentence, "param": {"nb_words": 6}},
       "sentences": {"func": fake.sentences, "param": {"nb": 3}},
       "text": {"func": fake.text, "param": {"max_nb_chars": 200, "ext_word_list":None}},
       "texts": {"func": fake.texts, "param": {"nb_texts": 3, "ext_word_list": None}},
       "word": {"func": fake.word, "param": {"ext_word_list": None}},
       "words": {"func": fake.words, "param": {"nb": 3, "ext_word_list": None}},
       "binary": {"func": fake.binary, "param": {"length": 1048576}},
       "boolean": {"func": fake.boolean, "param": {"chance_of_getting_true": 50}},
       "csv": {"func": fake.csv, "param": {"header": None, "data_columns": ('{{name}}', '{{address}}'), "num_rows": 10}},
       "dsv": {"func": fake.dsv, "param": {"header": None, "data_columns": ('{{name}}', '{{address}}'), "num_rows": 10}},
       "image": {"func": fake.image,
                 "param": {"size": (256, 256), "image_format": 'png', "hue": None, "luminosity": None}},
       "fixed_width": {"func": fake.fixed_width, "param": {"data_columns": None, "num_rows": 10}},
       "json": {"func": fake.json, "param": {"data_columns": None, "num_rows": 10}},
       "json_bytes": {"func": fake.json_bytes, "param": {"data_columns": None, "num_rows": 10}},
       "md5": {"func": fake.md5, "param": {"raw_output": False}},
       "null_boolean": {"func": fake.null_boolean, "param": {}},
       "password": {"func": fake.password,
                    "param": {"length": 10, "special_chars": True, "digits": True, "upper_case": True,
                              "lower_case": True}},
       "psv": {"func": fake.psv, "param": {"header": None, "data_columns": ('{{name}}', '{{address}}'), "num_rows": 10}},
       "sha1": {"func": fake.sha1, "param": {"raw_output": False}},
       "sha256": {"func": fake.sha256, "param": {"raw_output": False}},
       "tar": {"func": fake.tar, "param": {"uncompressed_size": 65536, "num_files": 1, "min_file_size": 4096}},
       "tsv": {"func": fake.tsv, "param": {"header": None, "data_columns": ('{{name}}', '{{address}}'), "num_rows": 10}},
       "uuid4": {"func": fake.uuid4, "param": {}},
       "xml": {"func": fake.xml, "param": {"nb_elements": 10, "allowed_types": {}}},
       "zip": {"func": fake.zip, "param": {"uncompressed_size": 65536, "num_files": 1, "min_file_size": 4096}},
       "passport_dob": {"func": fake.passport_dob, "param": {}},
       "passport_number": {"func": fake.passport_number, "param": {}},
       "passport_owner": {"func": fake.passport_owner, "param": {"gender": {}}},
       "first_name": {"func": fake.first_name, "param": {}},
       "first_name_male": {"func": fake.first_name_male, "param": {}},
       "first_name_female": {"func": fake.first_name_female, "param": {}},
       "first_name_nonbinary": {"func": fake.first_name_nonbinary, "param": {}},
       "language_name": {"func": fake.language_name, "param": {}},
       "last_name": {"func": fake.last_name, "param": {}},
       "last_name_male": {"func": fake.last_name_male, "param": {}},
       "last_name_female": {"func": fake.last_name_female, "param": {}},
       "lasy_name_nonbinary": {"func": fake.last_name_nonbinary, "param": {}},
       "name": {"func": fake.name, "param": {}},
       "name_male": {"func": fake.name_male, "param": {}},
       "name_female": {"func": fake.name_female, "param": {}},
       "name_nonbinary": {"func": fake.name_nonbinary, "param": {}},
       "prefix": {"func": fake.prefix, "param": {}},
       "prefix_male": {"func": fake.prefix_male, "param": {}},
       "prefix_female": {"func": fake.prefix_female, "param": {}},
       "prefix_nonbinary": {"func": fake.prefix_nonbinary, "param": {}},
       "suffix": {"func": fake.suffix, "param": {}},
       "suffix_male": {"func": fake.suffix_male, "param": {}},
       "suffix_female": {"func": fake.suffix_female, "param": {}},
       "suffix_nonbinary": {"func": fake.suffix_nonbinary, "param": {}},
       "country_calling_code": {"func": fake.country_calling_code, "param": {}},
       "msisdn": {"func": fake.msisdn, "param": {}},
       "phone_number": {"func": fake.phone_number, "param": {}},
       "profile": {"func": fake.profile, "param": {"fields": None, "sex": None}},
       "simple_profile": {"func": fake.simple_profile, "param": {"sex": None}},
       "enum": {"func":fake.enum, "param": {"enum_cls": MySQLDataType}},
       "pybool": {"func": fake.pybool, "param": {"truth_probability": 50}},
       "pydecimal": {"func": fake.pydecimal,
                     "param": {"left_digits": None, "right_digits": None, "positive": False, "min_value": None,
                               "max_value": None}},
       "pydict": {"func": fake.pydict, "param": {"nb_elements": 10, "variable_nb_elements": True, "value_types": None,
                                                 "allowed_types": {}}},
       "pyfloat": {"func": fake.pyfloat,
                   "param": {"left_digits": None, "right_digits": None, "positive": False, "min_value": None,
                             "max_value": None}},
       "pyint": {"func": fake.pyint, "param": {"min_value": 0, "max_value": 9999}},
       "pyiterable": {"func": fake.pyiterable,
                      "param": {"nb_elements": 10, "variable_nb_elements": True, "allowed_types": None}},
       "pylist": {"func": fake.pylist,
                  "param": {"nb_elements": 10, "variable_nb_elements": True, "allowed_types": None}},
       "pyobject": {"func": fake.pyobject, "param": {}},
       "pyset": {"func": fake.pyset,
                 "param": {"nb_elements": 10, "variable_nb_elements": True, "allowed_types": None}},
       "pystr": {"func": fake.pystr, "param": {"min_chars": 10, "max_chars": 20, "prefix": '', "suffix": ''}},
       "pystr_format": {"func": fake.pystr_format, "param": {}},
       "pystruct": {"func": fake.pystruct, "param": {"count": 10}},
       "pytuple": {"func": fake.pytuple,
                   "param": {"nb_elements": 10, "variable_nb_elements": True, "allowed_types": {}}},
       "sbn9": {"func": fake.sbn9, "param": {"separator": "-"}},
       "ssn": {"func": fake.ssn, "param": {}},
       "android_platform_token": {"func": fake.android_platform_token, "param": {}},
       "chrome": {"func": fake.chrome,
                  "param": {"version_from": 13, "version_to": 63, "build_from": 800, "build_to": 899}},
       "firefox": {"func": fake.firefox, "param": {}},
       "internet_explorer": {"func": fake.internet_explorer, "param": {}},
       "ios_platform_token": {"func": fake.ios_platform_token, "param": {}},
       "linux_platform_token": {"func": fake.linux_platform_token, "param": {}},
       "linux_processor": {"func": fake.linux_processor, "param": {}},
       "mac_platform_token": {"func": fake.mac_platform_token, "param": {}},
       "mac_processor": {"func": fake.mac_processor, "param": {}},
       "opera": {"func": fake.opera, "param": {}},
       "safari": {"func": fake.safari, "param": {}},
       "user_agent": {"func": fake.user_agent, "param": {}},
       "windows_platform_token": {"func": fake.windows_platform_token, "param": {}},
       "SERIAL": {"func": Serial_custom, "param":{}}
   }
def get_provider_function(prov):
       try:
              return provider_dict_map[prov]["func"],provider_dict_map[prov]["param"]
       except:
              raise Exception(f"The requested sub-provider {prov} is not available")
