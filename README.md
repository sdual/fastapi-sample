# fastapi-sample

FastAPI と uvicorn をインストール
```bash
$ pip install fastapi fastapi-utils "uvicorn[standard]" requests pytest-httpserver httpx
```

起動の仕方
```
$ python main.py
```

サンプルのエンドポイント
```bash
$ curl -X GET http://localhost:8000/hello
```

```bash
$ curl -X GET http://localhost:8000/user
```

```bash
$ curl -X POST http://localhost:8000/update
```
