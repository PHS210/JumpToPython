lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
# langs = lang1.extend(lang2)
# extend() 메서드는 return 값이 없음
# 따라서 lang1.extend(lang2) 만 호출하고 lang1을 출력해야 함  
print(langs)
# 리스트는 + 연산자로 연결 가능
# extend() 메서드도 있음