import urllib.parse

import requests


# 具体的な API として使用。
# https://jsonplaceholder.typicode.com/

# client library: requests
# https://requests.readthedocs.io/en/latest/

class SampleRequester:
    _SAMPLE_API_BASE_URL = 'https://jsonplaceholder.typicode.com/todos/'

    def __init__(self):
        pass

    def request(self, id: int) -> str:
        url = urllib.parse.urljoin(self._SAMPLE_API_BASE_URL, str(id))
        res = requests.get(url)
        return res.text
