# Azure AI Evaluation SDK のサンプル コード

# 使い方

## 事前準備

```bash
git clone https://github.com/ry0y4n/ai-evaluation-sdk-practice.git
cd ai-evaluation-sdk-practice
```

## 仮想環境と依存関係のインストール

```bash
python -m venv .venv
.\.venv\Scripts\activate

pip install -r .\requirements.txt
```

## サンプルコードの実行

```bash
python .\evaluate.py
```

> もし、依存関係でエラーが出た場合は以下コマンドで `Marshmallow` をダウングレード
>
> ```bash
> pip install marshmallow==3.18.0
> ```

# 参考情報

-   [Azure AI Evaluation client library for Python](https://pypi.org/project/azure-ai-evaluation/)
-   [SDK のリファレンス](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-evaluation-readme?view=azure-python)
-   [SDK のソース コード](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/evaluation/azure-ai-evaluation)
