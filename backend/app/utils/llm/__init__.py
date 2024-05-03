import os

from llama_index.core import Settings
from llama_index.llms.langchain import LangChainLLM
from llama_index.llms.openai import OpenAI
from yandex_chain import YandexLLM, YandexGPTModel, YandexEmbeddings


llm = LangChainLLM(llm=YandexLLM(
    api_key=os.environ.get("YANDEX_API_KEY"),
    folder_id=os.environ.get("YANDEX_FOLDER_ID"),
    model=YandexGPTModel.Pro,
    llm2=OpenAI()
))

embed_model = YandexEmbeddings(
    api_key=os.environ.get("YANDEX_API_KEY"),
    folder_id=os.environ.get("YANDEX_FOLDER_ID"),
)

summarize_model = YandexLLM(
    api_key=os.getenv("YANDEX_API_KEY"),
    folder_id=os.getenv("YANDEX_FOLDER_ID"),
    model=YandexGPTModel.Pro,
)
