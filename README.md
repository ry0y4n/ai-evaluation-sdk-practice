```bash
python -m venv .venv
.\.venv\Scripts\activate

pip install -r .\requirements.txt

python .\main.py
```

もし、依存関係でエラーが出た場合は以下コマンドで `Marshmallow` をダウングレード

```bash
pip install marshmallow==3.18.0
```
