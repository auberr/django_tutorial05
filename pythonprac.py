class SomeClassName : # Pascal convention
    pass

class someClassName : # Camel convention
    pass

class some_class_name : # snake convention
    pass

tuple = (1,2,3,4,5) # 선언 후 변경 삭제 불가

sets = {1, 2, 3, 4, 5} # 중복된 데이터 없음

dict = {'number': '1'}

number = 10

def func():
    global number
    number = 5

func()
print(number)

num1 = 10
num2 = 5

divide = num1 / num2
print(divide) # float 출력

divide1 = num1 // num2
print(divide1) # 나머지 없는 나누기 int 출력

divide2 = num1 % num2
print(divide2)