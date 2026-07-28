a = "백두 무궁 한라 삼천"

# 공백 문자를 기준으로 나누어 봐!
print(a.split(" "))

print(10 == 100)

a = True
b = 0
c = []
while(a):
    print("Yes")
    c.append("yes")
    b += 1
    if b >= 10:
        a = False
print(c)

a = "맛있는 {}".format("짜장면")
print(a)
food = "제육볶음"
a = f"맛있는 {food}"
print(a)
