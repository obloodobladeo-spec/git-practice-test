# string = input("입력 : ") # input은 항상 str으로 값을 받음.
# if string is not int:
#     string = int(string) # input은 항상 str으로 값을 받음.
# print("자료 :", string)
# # print("자료형 :", type(string))
# print(string + 1)

# print(float(string))

output_a = "{:d}".format(52)
print(output_a)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52) # 5칸
output_c = "{:10d}".format(52) # 10칸

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52) # 양수
output_e = "{:05d}".format(-52) # 음수

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
