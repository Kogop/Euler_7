# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def num_of_easy_number(n):
    list_of_easy_numbers = [2]
    while len(list_of_easy_numbers) < n:
        for j in range(2, 99999999999999999):
            for i in list_of_easy_numbers:      #добавить счетчик чтобы считал что простое число не делиться на другие простые числа
                                                # и если не делится на остальные простые, то только тогда его можно записывать
                                                # логично же? похуй, 3 ночи, завтра додумаю
                if j % i != 0:
                    print(j % i)
                    if list_of_easy_numbers.count(j) == 0:  # число должно добавляться только если оно не делится на каждое из чисел из списка
                        for k in list_of_easy_numbers:
                            j % list_of_easy_numbers[k]

                        list_of_easy_numbers.append(j)
                        break
                if len(list_of_easy_numbers) == n:
                    break
            if len(list_of_easy_numbers) == n:
                break

    return list_of_easy_numbers[-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(num_of_easy_number(int(input("введите номер искомого простого числа\n"))))
    # todo

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
