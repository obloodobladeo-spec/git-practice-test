# try:
#     anwer = int(input("값을 입력하세요 : "))
#     if anwer % 2 == 0:
#         print("짝수입니다.")

#     elif anwer % 2 == 1:
#         print("홀수입니다.")

# except ValueError:
#     # 만약에 예외가 발생한다면
#     print("값을 잘못입력하였습니다.")

# finally:
#     print("감사합니다.")

# try except 구문으로 예외를 처리합니다.

# isdigit() 함수는 문자열이 숫자로만 구성되어 있는지 여부를 불 값으로 반환해주는 함수입니다

# try:
#     # 숫자로 변환합니다.
#     number_input_a = int(input("정수 입력> "))
#     # 출력합니다.
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except:
#     print("무언가 잘못되었습니다.")
# else: # 예외가 발생하지 않았을 때 실행할 코드
#     pass
# finally: # 어떤 경우든 마지막에 실행되고 종료되는 코드
#     pass

list_number = [52, 273, 32, 72, 100]
while(True):
    try:
        # 숫자를 입력 받습니다.
        number_input = int(input("정수 입력> "))
        # 리스트의 요소를 출력합니다.
        print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    except ValueError as exception:
        # ValueError가 발생하는 경우
        print("정수를 입력해 주세요!")
        print(type(exception), exception)
    except IndexError as exception:
        # IndexError가 발생하는 경우
        print("리스트의 인덱스를 벗어났어요!")
        print(type(exception), exception)
    except Exception as exception:
        # 이외의 예외가 발생한 경우
        print("미리 파악하지 못한 예외가 발생했습니다.")
        print(type(exception), exception)
