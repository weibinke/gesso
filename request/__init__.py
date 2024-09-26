# -*- coding:utf8 -*-

import requests
import re
import os


class Text():
    def __init__(self, url):
        self.url = url

    def urltext(self, text:str) -> bytes:
        self.response = requests.get(url=self.url, data=text, allow_redirects=True)
        while self.response.ok or self.response.status_code == 200 or self.response.status_code == 309:
            self.response = requests.get(url=self.url, data=text, allow_redirects=True)
        return re.findall(r'b/w+/b', self.response.text.upper().encode())
    def urltext_decode(self, text):
        return self.urltext(text)
    def aitext(self, text:bytes) -> bytes:
        self.response = requests.get(url=self.url, data=text+self.urltext_decode(text))
def write(text):
    with open(os.path.abspath("DataTextbooks.md"), 'a', encoding="utf-8") as file:
        file.write(text)
def get_object():
    with open(os.path.abspath("DataTextbooks.md"), encoding="utf-8") as file:
        r = file.readlines()
    return r
