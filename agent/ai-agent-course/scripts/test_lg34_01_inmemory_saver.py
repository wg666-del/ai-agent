import sys
from pathlib import Path

# 将项目根目录加入 sys.path，保证无论从哪个目录运行都能导入 app 包
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.langgraph_persistence.demo_01_inmemory_saver import main


if __name__ == "__main__":
    main()