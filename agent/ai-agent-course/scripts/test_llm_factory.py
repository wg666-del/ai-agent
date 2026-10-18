import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.llm.factory import LLMProviderFactory, infer_provider_from_model


models = [
  "deepseek-chat",
  "qwen-plus",
  "gpt-4.1-mini",
  "unknown-model",
]

for model in models:
  provider = infer_provider_from_model(model)
  print(model, "=>", provider)