# 제어문, 반복문

# 문제 1
'''
shirt
'''


# 문제 2
'''
num = 1
sum = 0
while num < 101:
    if num % 4 == 0:
        sum += num
    num += 1
print("sum=", sum)
'''

# 문제 3
'''
sum = 0
for i in range(1, 101):
    if i % 5 == 0:
        sum += i
print("sum=", sum)
'''

# 문제 4
# sol 1.
'''
sum = 0
count = 0
py_score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
while len(py_score):
    score = py_score.pop()
    if score >= 60:
        count += 1
        sum += score
avg = sum/count
print("average=", avg)
'''

# sol 2.
'''
sum = 0
count = 0
py_score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
for score in py_score:
    if score >= 60:
        count += 1
        sum += score
avg = sum/count
print("average=", avg)
'''

# 문제 5
'''
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
    print("\n")
'''

# 문제 6

'''
def Wordcount(sentence):
    word_list = sentence.split(" ")
    dic = {}
    for i in word_list:
        count = word_list.count(i)
        dic[i] = count
    for key, value in dic.items():
        print(key, "=", value)

sentence = '다들 파이썬은 어떠신가요 파이썬은 나중에 다른 곳에서도 많이 쓰인답니다 파이썬은 다른 언어보다 코딩 하기 쉬워요 멋사 멋사 화이팅'
Wordcount(sentence)
'''
