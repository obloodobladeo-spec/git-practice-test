# class Student:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science

#     def get_sum(self):
#         return self.korean + self.math \
#             + self.english + self.science

#     def get_average(self):
#         return round(self.get_sum() / 4, 1)

#     def to_string(self):
#         print("{}\t{}\t{}".format(\
#             self.name,\
#             self.get_sum(),\
#             self.get_average()
#             ))

# students = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 92, 98, 96, 98),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 98, 92, 96, 92),
#     Student("윤아린", 95, 98, 98, 98),
#     Student("윤명월", 64, 88, 92, 92)
# ]

# print("이름\t총점\t평균")
# for student in students:
#     student.to_string()

# print에서 정의된 형태로 출력된다.
# _str__ 은 출력 행태를 정해준다.
class Coffee:
    def __str__(self):
        return "부드러운 형태"

c= Coffee()
print(c)

