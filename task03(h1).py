# Задача 1 необязательная. Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:* 
# 1+2*3 => 7; 
# (1+2)*3 => 9;
# Тут может помочь библиотека re

import re

# def arif_string(str: str) -> int:
#     x = 0
#     # if str(len) == 0:
#     #     return x
#     # for i in str:
#     result = re.findall(r'.', str)
#     print(result)
#     for i in range(len(result)):
#         if result[i] == '+' and result[i+1] != '*':
#             sum = int(result[i-1])+int(result[i+1])
#             print(sum)
    
# arif_string('1+2*3')

# text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# splitted_text = text.split(",")
# print(splitted_text)
# print(splitted_text[1])
# print(int((1+2)*3))

def evaluate_expression(expression: str) -> float:
    # Remove whitespaces from the expression
    expression = expression.replace(" ", "")

    # Base case: if the expression is a single number, return it
    if expression.isdigit():
        return float(expression)

    # Check for parentheses and evaluate the expression inside them recursively
    if "(" in expression and ")" in expression:
        start = expression.rindex("(") + 1
        end = expression.index(")", start)
        sub_expression = expression[start:end]
        result = evaluate_expression(sub_expression)
        expression = expression[:start-1] + str(result) + expression[end+1:]

    # Evaluate the expression using eval() function
    return eval(expression)

expression = '(1+2)*3'
result = evaluate_expression(expression)
print(f"Результат: {result}")