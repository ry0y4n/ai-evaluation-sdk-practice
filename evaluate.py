import os
import pandas as pd
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from azure.ai.evaluation import GroundednessEvaluator, CoherenceEvaluator, FluencyEvaluator, RelevanceEvaluator, SimilarityEvaluator
from customEvaluator.codeBase.answer_length import AnswerLengthEvaluator
from customEvaluator.promptBase.friendliness import FriendlinessEvaluator


load_dotenv(verbose=True)

# credential = DefaultAzureCredential()

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
}

# エバリュエータのインスタンスを作成
groundedness_eval = GroundednessEvaluator(model_config)
coherence_eval = CoherenceEvaluator(model_config)
fluency_eval = FluencyEvaluator(model_config)
relevance_eval = RelevanceEvaluator(model_config)
similarity_eval = SimilarityEvaluator(model_config)

# 評価するデータを用意
query_response = {
    "context": "ダイニングチェア。木製の座面。四本の脚。背もたれ。ブラウン。幅18インチ、奥行き20インチ、高さ35インチ。耐荷重250ポンド。",
    "query": "Contoso Home Furnishingsのダイニングチェアの製品仕様に基づいて、魅力的なマーケティング製品説明を提供してください。",
    "ground_truth": "このダイニングチェアはブラウンの木製で、四本の脚と背もたれがあります。寸法は幅18インチ、奥行き20インチ、高さ35インチです。耐荷重は250ポンドです。",
    "response": (
        "私たちの時代を超えた木製ダイニングチェアをご紹介します。快適さと耐久性を兼ね備えたデザインです。"
        "頑丈な四本脚のベースと木製の座面で作られており、250ポンドまでの信頼できるサポートを提供します。"
        "滑らかなブラウンの仕上げは、素朴なエレガンスを加え、エルゴノミクスに基づいた背もたれは快適なダイニング体験を保証します。"
        "寸法は幅18インチ、奥行き20インチ、高さ35インチで、形と機能の完璧なバランスを実現し、どんなダイニングスペースにも適した多用途なオプションです。"
        "この美しくシンプルでありながら洗練された座席オプションで、あなたの家を格上げしましょう。"
    )
}

# evaluatorにqueryとresponseを渡してgroundednessを評価
groundedness_score = groundedness_eval(
    **query_response
)
print(groundedness_score)

# evaluatorにqueryとresponseを渡してcoherenceを評価
coherence_score = coherence_eval(
    **query_response
)
print(coherence_score)

# evaluatorにqueryとresponseを渡してfluencyを評価
fluency_score = fluency_eval(
    **
    query_response
)
print(fluency_score)

# evaluatorにqueryとresponseを渡してrelevanceを評価
relevance_score = relevance_eval(
    **query_response
)
print(relevance_score)

# evaluatorにqueryとresponseを渡してsimilarityを評価
similarity_score = similarity_eval(
    **query_response
)
print(similarity_score)

# # evaluatorにresponseを渡してanswer_lengthを評価
# answer_length_evaluator = AnswerLengthEvaluator()
# answer_length = answer_length_evaluator(answer=query_response["response"])
# print(answer_length)

# # evaluatorにresponseを渡してfriendlinessを評価
# friendliness_eval = FriendlinessEvaluator(model_config)
# friendliness_score = friendliness_eval(response=query_response["response"])
# print(friendliness_score)

# 結果をリストにまとめて DataFrame に変換
results = [
    {
        "Evaluator": "Groundedness",
        "Score": groundedness_score.get("groundedness"),
        # "GPT Score": groundedness_score.get("gpt_groundedness"),
        "Reason": groundedness_score.get("groundedness_reason")
    },
    {
        "Evaluator": "Coherence",
        "Score": coherence_score.get("coherence"),
        # "GPT Score": coherence_score.get("gpt_coherence"),
        "Reason": coherence_score.get("coherence_reason")
    },
    {
        "Evaluator": "Fluency",
        "Score": fluency_score.get("fluency"),
        # "GPT Score": fluency_score.get("gpt_fluency"),
        "Reason": fluency_score.get("fluency_reason")
    },
    {
        "Evaluator": "Relevance",
        "Score": relevance_score.get("relevance"),
        # "GPT Score": relevance_score.get("gpt_relevance"),
        "Reason": relevance_score.get("relevance_reason")
    },
    {
        "Evaluator": "Similarity",
        "Score": similarity_score.get("similarity"),
        # "GPT Score": similarity_score.get("gpt_similarity"),
        "Reason": ""
    },
    # {
    #     "Evaluator": "Answer Length",
    #     "Score": answer_length.get("answer_length"),
    #     "Reason": ""
    # },
    # {
    #     "Evaluator": "Friendliness",
    #     "Score": friendliness_score.get("friendliness"),
    #     # "GPT Score": friendliness_score.get("gpt_friendliness"),
    #     "Reason": friendliness_score.get("friendliness_reason")
    # }
]

df = pd.DataFrame(results)
print("=======================================================================")
print(df)
print("=======================================================================")
