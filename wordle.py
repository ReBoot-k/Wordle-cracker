"""
Дата релиза: 19.10.2023
"""

import base64
import re
import urllib.parse

class WordleCracker:
    def __init__(self, pattern="(https://wordleplay\.com/.+/\?(challenge|tour)=?)(?P<word>.+)") -> None:
        self.pattern = re.compile(pattern)


    def decode_url(self, string) -> str:
        result = urllib.parse.unquote(string)
        return result


    def decode_base64(self, string) -> str:
        encode = string.encode()
        decode = base64.b64decode(encode)
        result = decode.decode()
        return result


    def extract_encode_string(self, link) -> dict:
        data_regex = self.pattern.match(link)
        if data_regex:
            data_string = data_regex.group("word")
            data_normalize = data_regex.group(1) + self.decode_url(data_string)
            return {"word_base64": data_string, "normalize": data_normalize}
        return None

    def crack(self, link) -> str:
        extract = self.extract_encode_string(link)
        if extract:
            data_normalize = extract["normalize"]

            data = self.decode_base64(extract['word_base64'])
            data = data.replace(";", ", ")


            result = "Ответ: {}\nНормализованная ссылка: {}\n\n".format(data, data_normalize)
        else:
            result = None

        return result

print("Cracker wordleplay.com\n")
cracker = WordleCracker()

while True:
    link = input("Введите ссылку: ")
    result = cracker.crack(link) or "Не понимаю. Блокирую!"
    print(result)