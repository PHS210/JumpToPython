f = open ('text.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')
f = open('text.txt', 'w')
f.write(body)
f.close


# body.replace('python', 'java')
# body = body.replace('python', 'java')
# 둘중 뭐가 맞음?