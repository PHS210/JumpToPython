movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2,3]
# 이 코드는 틀렸다. 콤마를 이용해 여러 인덱스를 동시에 지정하는 문법은 지원X
# 따라서 슬라이시을 이용해야 한다.

del movie_rank[2:4]
print(movie_rank)