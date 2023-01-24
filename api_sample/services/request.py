import urllib.parse

import requests


# 実装例のために叩く API として使用。
# https://jsonplaceholder.typicode.com/

# client library: requests
# https://requests.readthedocs.io/en/latest/

class SampleRequester:

    def __init__(self, base_url=None):
        if base_url is None:
            self._base_url = 'http://localhost:9000'
        else:
            self._base_url = base_url

    def request(self, user_id: int) -> str:
        url = urllib.parse.urljoin(self._base_url, 'todos/' + str(user_id))
        res = requests.get(url)
        return self.reshape_res(res.text)

    def reshape_res(self, res: str) -> str:
        # このクラスの責務じゃないので本来別クラスでやるべき
        res = res.replace('\n', '')
        res = res.replace(' ', '')
        return res
