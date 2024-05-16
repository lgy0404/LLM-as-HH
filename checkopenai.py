import os

openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is not None:
    print("OPENAI_API_KEY 已设置，值为:", openai_api_key)
else:
    print("OPENAI_API_KEY 未设置")
