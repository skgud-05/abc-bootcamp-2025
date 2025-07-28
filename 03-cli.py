from dotenv import load_dotenv
from ai import get_personality_analysis
load_dotenv()
print('#AI 관상가 입니다.얼굴 특징을 입력해주시면 성격과 미래를 알려드릴게요.')
line= input("얼굴 특징: ").strip()
if not line:
    print("에러: 얼굴특징을 입력하지 않았습니다.")
else:
    print("입력하신 얼굴 특징:", line)
    print("입력중..")
    result=get_personality_analysis(line)
    print("분석완료")
    print(result)

 

