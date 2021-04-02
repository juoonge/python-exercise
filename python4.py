# 함수

# 문제 1
'''
def is_odd(num):
    return 'even' if num % 2 == 0 else 'odd'
print(is_odd(12))
'''

# 문제 2
'''
def average(list):
    avg = 0.0
    for i in list:
        avg += i
    return avg/len(list)


list = []
while True:
    num = int(input("input number >> "))
    if num == -1:
        break
    list.append(num)
print(average(list))
'''
