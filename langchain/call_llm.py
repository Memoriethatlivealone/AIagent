from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
base_url=os.getenv("OPENAI_BASE_URL"),#平台提供的URL
api_key=os.getenv("OPENAI_API_KEY"),#平台提供的API-Key
)
completion = client.chat.completions.create(
model="gpt-5.6-sol",#模型名称（中转站API模型ID，横杠连接）
messages=[{"role": "user", "content": "你好 你是什么模型"}],#用户
)
print(completion.choices[0].message.content)