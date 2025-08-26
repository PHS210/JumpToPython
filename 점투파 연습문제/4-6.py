user_input = input(" 저장할내용을입력하세요:")
f = open('test.txt', 'a', encoding='utf-8') # 내 용 을 추 가 하 기 위 해 'a' 를 사 용
f.write(user_input)
f.write("\n") # 입 력 한 내 용 을 줄 단 위 로 구 분 하 기 위 해 줄 바 꿈 문 자 삽입
f.close()