# import os
# from pathlib import Path
# from typing import Any

# print(os.getcwd())

# current_file = Path(__file__)
# print(current_file)
# print(current_file.parent)

from app.basics.utils import format_user_name

result = format_user_name("大伟")

print(result)