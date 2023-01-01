# string = input('Привет, что нужно посчитать?(вводите цифры и символы через пробел):')
# print(string)
# my_list = string.split()
# print(my_list)
# for i in range(len(my_list)):
#     if my_list[i].isdigit():
#         my_list[i] = int(my_list[i])

# print(my_list)
# result = 0
# while len(my_list) != 1:
#     i = 0
#     while '*' in my_list or '/' in my_list and i < len(my_list):
#         if my_list[i] == '*':
#             result = my_list[i - 1] * my_list[i + 1]
#             my_list[i - 1] = result
#             my_list.pop(i)
#             my_list.pop(i)
#         elif my_list[i] == '/':
#             result = my_list[i - 1] / my_list[i + 1]
#             my_list[i - 1] = result
#             my_list.pop(i)
#             my_list.pop(i)
#         else:
#             i = i + 1
#         print(my_list)
#     i = 0  
#     while ('+' in my_list or '-' in my_list) and i < len(my_list):
#         if my_list[i] == '+':
#             result = my_list[i - 1] + my_list[i + 1]
#             my_list[i - 1] = result
#             my_list.pop(i)
#             my_list.pop(i)
#         elif my_list[i] == '-':
#             result = my_list[i - 1] - my_list[i + 1]
#             my_list[i - 1] = result
#             my_list.pop(i)
#             my_list.pop(i)
#         else:
#             i = i + 1
#         print(my_list)
# print(my_list)
# answer = (my_list[0])
# print(f'Ответ = {answer}')   