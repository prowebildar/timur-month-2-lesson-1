# map(что сделать? с кем сделать?) - принимает в себя первым аргументом ссылку на функцию
# и будет ее использовать для каждого элемента указанного списка

# def do_operation(num1, num2, operation):
#     result = operation(num1, num2)  # будет вызвана функция, ссылка на которую была указана
#     print(f'{result=}')
#
#
# def plus(num1, num2):
#     return num1 + num2
#
#
# def minus(num1, num2):
#     return num1 - num2
#
#
#
# do_operation(10, 10, plus)
# do_operation(10, 10, minus)


lst1 = ['text1', 'text2', 'text3']
lst2 = []
for i in lst1:
    lst2.append(i.upper())


# print(lst2)


# def to_upper(text):
#     return text.upper()
#
# test = []
# for i in lst1:
#     print(to_upper(i))
#
#
# lst3 = map(to_upper, lst1)

# print(lst3)
# print(list(lst3))

def change_str(text):
    lst = list(text)
    return '-'.join(lst)


# print(list(map(list, lst1)))
# print(list(map(change_str, lst1)))
# print(list(map(str.upper, lst1)))

test1 = ['a', 'b', 'c']
test2 = ['d', 'e', 'f']
test3 = ['g', 'h', 'i']
#
# def plus(a, b, c):
#     return a + b + c
#
#
# print(list(map(plus, test1, test2, test3)))


# filter(как проверить?, что проверить?) - фильтрует элементы списка, применяя для них фукнцию в которой есть условие
# если элемент после проверки отдает True, то остается в списке, если нет, то не остается


lst5 = [i for i in range(101)]


def is_even(number):
    if number % 2 == 0:
        return True


# print(list(map(is_even, lst5)))
# print(list(filter(is_even, lst5)))


mixed = ['adsf', 4678, 'sadfds', 456, 'sadfs', True, True, [1, 2, 3], 456, 'dfdfs', 'sdfsdf']


def is_str(obj):
    return type(obj) is str


# print(list(filter(is_str, mixed)))

# lambda  - анонимная функция
# lambda args: code

print(list(map(lambda text: text.upper(), lst1)))
print(list(map(lambda text: '-'.join(list(text)), lst1)))
print(list(map(lambda a, b, c: a + b + c, test1, test2, test3)))


print(list(filter(lambda num: num % 2 == 0, lst5)))



