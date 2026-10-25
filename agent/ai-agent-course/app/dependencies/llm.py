from app.core.config import settings
from app.langchain_models.langchain_provider import LangChainLLMProvider
from app.llm.base import BaseLLMProvider
from app.llm.factory import LLMProviderFactory


async def get_llm_provider() -> BaseLLMProvider:
  if settings.default_llm_provider.startswith("langchain_"):
    provider = settings.default_llm_provider.replace("langchain_", "")

    return LangChainLLMProvider(
      provider=provider,
      model=settings.default_model,
    )

  return LLMProviderFactory.create(
    provider=settings.default_llm_provider,
  )