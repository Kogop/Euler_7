# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def num_of_easy_number(n):
    list_of_easy_numbers = [2]
    temp_list = []
    counter = 0
    j = 3
    while len(list_of_easy_numbers) < n:
        for i in list_of_easy_numbers:  # добавить счетчик чтобы считал что простое число не делиться на другие простые числа
            temp_list.append(j % i)                            # и если не делится на остальные простые, то только тогда его можно записывать
        for o in range(0, len(temp_list)):                                 # логично же? похуй, 3 ночи, завтра додумаю
            if temp_list[o] == 0:
                break
            else:
                counter += 1
            if counter == len(temp_list):
                #print(j)
                list_of_easy_numbers.append(j)
        counter = 0
        temp_list = []
        if len(list_of_easy_numbers) == n:
            break
        j += 1
    return list_of_easy_numbers[-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(num_of_easy_number(int(input("введите номер искомого простого числа\n"))))
    # todo

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
