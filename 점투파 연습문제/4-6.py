user_input = input(" 저장할내용을입력하세요:")
f = open('test.txt', 'a', encoding='utf-8') # 내 용 을 추 가 하 기 위 해 'a' 를 사 용
f.write(user_input)
f.write("\n") # 입 력 한 내 용 을 줄 단 위 로 구 분 하 기 위 해 줄 바 꿈 문 자 삽입
f.close()


#여기서 알게된점.
#기존에 해당 파일이 없더라도 a 를 하면 새파일이 만들어지는구나.