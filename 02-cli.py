from dotenv import load_dotenv
load_dotenv()  # .env 파일이 있다면, 환경변수로서 로딩
import os
API_KEY=os.environ["OPENAI_API_KEY"]

from openai import OpenAI
i=0
client = OpenAI(api_key=API_KEY)  # OPENAI_API_KEY 환경변수 지정이 필요
response = client.responses.create(
    model="gpt-4o",
    input="점심 메뉴를 추천해줘, 추천해줄 때 본론만 말해",
)
print("usage :", response.usage)
print(response.output_text)