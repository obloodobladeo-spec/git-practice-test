# csv 파일 컴마 세퍼레이트 벨류
# 컴마로 구분된 값들로 구성된 파일, 형식을 지켜서 값들을 구분한다.(행과 열을 구분)
import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w", encoding="utf8") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

# 책 5-2 재귀함수 공부해보기

# with open("info.txt", "r", encoding="utf8") as file:
#     for line in file:
#         (name, weight, height) = line.strip().split(", ")

#         if (not name) or (not weight) or (not height):
#             continue

#         bmi = int(weight) / ((int(height) / 100) ** 2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상체중"
#         else:
#             result = "저체중"

#         print('\n'.join([
#             "이름 : {}",
#             "몸무게 : {}",
#             "키 : {}",
#             "BMI : {}",
#             "결과 : {}"
#         ]).format(name, weight, height, int(bmi), result))
#         print()

# 고급 예외 처리
