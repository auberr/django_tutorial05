A, B, C = map(int, input().split(' '))

N = 0

if C-B <= 0:
    even=-1
else:
    even = A / (C-B) +1

print(int(even))
    



# EXPRESSION = {
#     "+": lambda x, y: x+y,
#     "-": lambda x, y: x-y,
#     "*": lambda x, y: x*y,
#     "/": lambda x, y: x/y,
# }

# def calc(num1, operator, num2):
#     return EXPRESSION[operator](int(num1), int(num2))

# def main():
#     try:
#         result = calc(*input().split(" "))
#         print(result)
    
#     except:
#         print("잘못된 수식을 입력하셨습니다.")

# main()

# class calc:
#     print('두 수의 연산만 가능')
#     print('a 와 b 를 입력 ex) a + b')
#     values = input('두 수를 띄어씌기를 하나 해서 입력해주세요.')
#     a, operator, b = values.split(" ")
#     print(a, b, operator)

#     def plus(a, b):
#         operator = calc.operator
#         if operator == '+':
#             return a + b
    
#     def minus(a, b):
#         operator = calc.operator
#         if operator == '-':
#             return a - b
    
#     def multiply(a, b):
#         operator = calc.operator
#         if operator == '*':
#             return a * b
    
#     def divide(a, b):
#         operator = calc.operator
#         if operator == '/':
#             return a / b


# calc()
# print(calc.minus(1, 2))

# import random
# lotto = set()
# bonus = set()

# def lotto_number_generator(count):
#     result = []
#     if count < 1:
#         print("1 이상의 값을 입력해주세요.")
#         return False
    
#     for _ in range(count):
#         lotto_numbers = set()
#         bonus_numbers = set()

#         while len(lotto_numbers) < 6:
#             lotto_numbers.add(random.randint(1, 45))
        
#         bonus_numbers.add(random.randint(1,45))

#         result.append(lotto_numbers)
#         result.append(bonus_numbers)
    
#     return result

# lotto_numbers = lotto_number_generator(1)
# print(lotto_numbers)


# products = {
#     "bread": 1000,
#     "milk": 3000,
#     "egg": 6000,
#     "drink": 1500
# }

# for k, v in products.items(): # key만 사용
#     print(k, v)

# members = ['lee', 'park', 'kim']

# new_mem =[]
# for member in members:
#     print(member)
#     new_mem.append(member)
# print(new_mem)

# for i, member in enumerate(members):
#     print(f"{member}는 {i+1}번째 회원입니다.")


# class SomeClassName : # Pascal convention
#     pass

# class someClassName : # Camel convention
#     pass

# class some_class_name : # snake convention
#     pass

# tuple = (1,2,3,4,5) # 선언 후 변경 삭제 불가

# sets = {1, 2, 3, 4, 5} # 중복된 데이터 없음

# dict = {'number': '1'}

# number = 10

# def func():
#     global number
#     number = 5

# func()
# print(number)

# num1 = 10
# num2 = 5

# divide = num1 / num2
# print(divide) # float 출력

# divide1 = num1 // num2
# print(divide1) # 나머지 없는 나누기 int 출력

# divide2 = num1 % num2
# print(divide2)
