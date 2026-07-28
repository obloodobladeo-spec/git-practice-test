import test_module as tt

anwer = tt.number_input()

r = round(tt.get_circumference(anwer), 2)
a = round(tt.get_circle_area(anwer), 2)
print("둘래값:{}, 넓이 값:{}".format(r, a))

 