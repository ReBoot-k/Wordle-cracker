"""
Дата релиза: 19.10.2023
"""

import base64
import re
import urllib.parse

PATTERN_ONE = re.compile("(https://wordleplay\.com/.+/\?challenge=?)(?P<word>.+)")
PATTERN_TWO = re.compile("(https://wordleplay\.com/.+/\?tour=?)(?P<word>.+)")

def decode_url(string):
    result = urllib.parse.unquote(string)
    return result


def decode_base64(string):
    encode = string.encode()
    decode = base64.b64decode(encode)
    result = decode.decode()
    return result


print("Cracker wordleplay.com\n")
while True:
    link = input("Введите ссылку: ")

    data_regex = PATTERN_ONE.match(link) or PATTERN_TWO.match(link)
    if data_regex:
        data_string = data_regex.group("word")
        data_normalize = decode_url(data_string)
        data = decode_base64(data_normalize)
        if ";" in data:
            data = ", ".join(data.split(";"))

        result = "Ответ: {}\nНормализованная ссылка: {}\n".format(data, data_regex.group(1) + urllib.parse.quote(data_string))
    else:
        result = "Не понимаю. Блокирую!"

    print(result)