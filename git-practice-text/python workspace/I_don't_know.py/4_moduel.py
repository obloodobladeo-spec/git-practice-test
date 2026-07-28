import random
import os
# print(random.random())
# print(random.random() * 10)
# print(int(random.random() * 10))

# 실수값 반환
# num = int((random.random() * 10) + 1) # 1 ~ 10 이하 값을 반환
# print(num)
# num = random.uniform(10, 20) # 지정한 범위 사이의 실수 값
# print(num)

# 정수값 반환
# num = random.randrange(0, 10)
# print(num)

# choice, shuffle, sample
# num = list(range(1, 46))
# print(random.choice(num)) # 하나를 선택
# random.shuffle(num) # 리스트 안의 숫자를 랜덤하게 섞음
# print(num)
# print(random.sample(num, k=2)) # 리스트 안의 값을 k값 만큼 뽑음

# num2 = range(1, 51)
# print(random.sample(num2, k=2))

# os.rename("file.txt", "new.txt")
# os.remove("new.txt")

print("현재 운영체제 이름:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더의 내부 요소:", os.listdir())
print(os.path.dirname(__file__))

os.rmdir("hello")