import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证以脚本方式（python tests/xxx.py）运行也能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import settings

print(settings.app_name)
print(settings.app_env)
print(settings.app_version)
print(settings.api_v1_prefix)
print(settings.default_model)
print(settings.supported_models_list)