# fastapi-sample

FastAPI と uvicorn をインストール
```bash
$ pip install fastapi
$ pip install fastapi-utils
$ pip install "uvicorn[standard]"
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
$ curl -X POST http://localhost:8000/update
```
