import os
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv(verbose=True)

credential = DefaultAzureCredential()

#groundednessはmodel_configを、groundedness_proはazure_ai_projectを引数に渡す
azure_ai_project = {
    "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
    "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
    "project_name": os.environ.get("AZURE_PROJECT_NAME"),
}

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
}

#必要なevaluatorをimport
from azure.ai.evaluation import GroundednessProEvaluator, GroundednessEvaluator, CoherenceEvaluator, FluencyEvaluator, RelevanceEvaluator, SimilarityEvaluator

#evaluatorのインスタンスを作成
groundedness_eval = GroundednessEvaluator(model_config)
# groundedness_pro_eval = GroundednessProEvaluator(azure_ai_project=azure_ai_project, credential=credential) # Groundness Pro は West US 2 でのみ利用可能
coherence_eval = CoherenceEvaluator(model_config)
fluency_eval = FluencyEvaluator(model_config)
relevance_eval = RelevanceEvaluator(model_config)

#queryとresponseを定義
query_response = {
    "context": "ダイニングチェア。木製の座面。四本の脚。背もたれ。ブラウン。幅18インチ、奥行き20インチ、高さ35インチ。耐荷重250ポンド。",
    "query": "Contoso Home Furnishingsのダイニングチェアの製品仕様に基づいて、魅力的なマーケティング製品説明を提供してください。",
    "ground_truth": "このダイニングチェアはブラウンの木製で、四本の脚と背もたれがあります。寸法は幅18インチ、奥行き20インチ、高さ35インチです。耐荷重は250ポンドです。",
    "response": "私たちの時代を超えた木製ダイニングチェアをご紹介します。快適さと耐久性を兼ね備えたデザインです。頑丈な四本脚のベースと木製の座面で作られており、250ポンドまでの信頼できるサポートを提供します。滑らかなブラウンの仕上げは、素朴なエレガンスを加え、エルゴノミクスに基づいた背もたれは快適なダイニング体験を保証します。寸法は幅18インチ、奥行き20インチ、高さ35インチで、形と機能の完璧なバランスを実現し、どんなダイニングスペースにも適した多用途なオプションです。この美しくシンプルでありながら洗練された座席オプションで、あなたの家を格上げしましょう。"
}

#evaluatorにqueryとresponseを渡してgroundednessを評価
groundedness_score = groundedness_eval(
    **query_response
)
print(groundedness_score)

# groundedness_pro_score = groundedness_pro_eval(
#     **query_response
# )
# print(groundedness_pro_score)

#evaluatorにqueryとresponseを渡してcoherenceを評価
coherence_score = coherence_eval(
    **query_response
)
print(coherence_score)

#evaluatorにqueryとresponseを渡してfluencyを評価
fluency_score = fluency_eval(
    **
    query_response
)
print(fluency_score)

#evaluatorにqueryとresponseを渡してrelevanceを評価
relevance_score = relevance_eval(
    **query_response
)
print(relevance_score)
