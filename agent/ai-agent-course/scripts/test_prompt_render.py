import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.prompts.base import PromptScenario
from app.services.prompt_service import prompt_service


def main():
    messages = prompt_service.render_by_scenario(
        scenario=PromptScenario.GENERAL_CHAT,
        variables={
            "user_question": "什么是 Prompt Engineering？"
        }
    )

    for message in messages:
        print("role:", message.role)
        print("content:")
        print(message.content)
        print("=" * 60)


if __name__ == "__main__":
    main()