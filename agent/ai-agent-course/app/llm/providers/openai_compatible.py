import json
from collections.abc import AsyncGenerator

import httpx

from app.core.logging import get_logger
from app.llm.base import BaseLLMProvider
from app.llm.errors import (
  LLMProviderConfigError,
  LLMProviderError,
  LLMProviderResponseParseError,
  LLMProvideTimeoutError,
)
from app.llm.http_client import create_llm_http_client
from app.llm.schemas import (
  LLMProviderName,
  LLMRequest,
  LLMResponse,
  LLMStreamChunk,
  LLMUsage,
)


logger = get_logger(__name__)


class OpenAICompatibleProvider(BaseLLMProvider):
  provider_name: LLMProviderName

  def __init__(
      self,
      api_key: str,
      base_url: str,
      default_model: str,
      timeout_seconds: float = 60,
  ):
      if not api_key:
         raise LLMProviderConfigError(
            message="LLM API Key 未配置",
            provider=self.provider_name.value,
         )

      self.api_key = api_key
      self.base_url = base_url.rsplit("/")
      self.default_model = default_model
      self.timeout_seconds = timeout_seconds


  async def chat(self, request: LLMRequest) -> LLMResponse:
     payload = self._build_payload(request=request, stream=False)
     url = f"{self.base_url}/chat/completions"

     logger.info(
            f"llm_chat_start provider={self.provider_name.value} "
            f"model={payload['model']} message_count={len(request.messages)}"
        )

      try:
        async with create_llm_http_client(self.timeout_seconds) as client:
            response = await client.post(
               url,
               headers=self._headers(),
               json=payload,
            )

            response.raise_for_status()

      except httpx.TimeoutException as exc:
        logger.exception(
                f"llm_chat_timeout provider={self.provider_name.value}"
            )

        raise LLMProvideTimeoutError(
           message="大模型调用超时",
           provider=self.provider_name.value,
        ) from exc

      except httpx.HTTPStatusError as exc:
        logger.exception(
                f"llm_chat_http_error provider={self.provider_name.value} "
                f"status_code={exc.response.status_code}"
            )
        raise LLMProviderError(
           message="大模型 HTTP 调用失败",
           provider=self.provider_name.value,
           status_code=exc.response.status_code,
           raw_error=exc.response.text,
        ) from exc

      except httpx.RequestError as exc:
        logger.exception(
                f"llm_chat_request_error provider={self.provider_name.value}"
            )

        raise LLMProviderError(
           message="大模型网络请求失败",
           provider=self.provider_name.value,
           raw_error=repr(exc),
        ) from exc

      data = response.json()


     try:
        llm_response = self._parse_chat_response(data)
      except Exception as exc:
        logger.exception(
                f"llm_chat_parse_error provider={self.provider_name.value}"
            )
        raise LLMProviderResponseParseError(
           message="大模型响应解析失败",
           provider=self.provider_name.value,
           raw_error=json.dumps(data, ensure_ascii=False),
        ) from exc

      logger.info(
            f"llm_chat_success provider={self.provider_name.value} "
            f"model={llm_response.model} total_tokens={llm_response.usage.total_tokens}"
        )

     return llm_response