from fastapi.testclient import TestClient
from pytest_httpserver import HTTPServer
import pytest

from api_sample.server import APIServer


# https://pytest-httpserver.readthedocs.io/en/latest/

@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("127.0.0.1", 9000)


def test_user_api(httpserver: HTTPServer):
    # http://localhost/todos/1 を叩くと下の形の json が返ってくるように設定
    fixture_json = {"userId": 1, "id": 1, "title": "delectusautautem", "completed": False}
    httpserver.port = 9000
    httpserver.expect_request('/todos/1').respond_with_json(fixture_json)

    app = APIServer.run()
    client = TestClient(app)

    res = client.get("http://localhost:8000/user")

    expected_json = '{"userId":1,"id":1,"title":"delectusautautem","completed":false}'

    assert res.json() == expected_json
