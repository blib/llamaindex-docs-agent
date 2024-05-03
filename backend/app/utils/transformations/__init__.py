"""Custom Transformations."""
import os
from app.utils.transformations.deduplicator import Deduplicator
from app.utils.transformations.url_extractor import URLExtractor
from app.utils.transformations.upserter import Upserter
from app.utils.transformations.hyperlinks_remover import HyperlinksRemover
from app.utils.transformations.summarizer import DocsSummarizer
from yandex_chain import YandexLLM, YandexGPTModel, YandexEmbeddings

__all__ = [
  "Deduplicator",
  "URLExtractor",
  "Upserter",
  "DocsSummarizer",
  "HyperlinksRemover",
]

summarize_model = YandexLLM(
    api_key=os.getenv("YANDEX_API_KEY"),
    folder_id=os.getenv("YANDEX_FOLDER_ID"),
    model=YandexGPTModel.Pro,
)
