from api_sample.services import SampleRequester

# 実際は pytest の機能つかってどこかで管理すべきだけどいったんここに置いておく
expected_json = """{"userId":1,"id":1,"title":"delectusautautem","completed":false}"""


def test_request():
    requester = SampleRequester('https://jsonplaceholder.typicode.com/')
    res = requester.request(1)
    assert res == expected_json
