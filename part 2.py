file = open('26.txt', 'r')
n, m = map(int, file.readline().split())
a_list = list()
b_list = list()
result = list()
for i in file.readlines():
    a, b = map(str, i.split())
    if b == 'A':
        a_list.append([a, b])
    else:
        b_list.append([a, b])
a_list.sort(key=lambda x: x[0])
b_list.sort(key=lambda x: x[0])
for i in b_list:
    if sum(result) > m:
        del(result[-1])
        break
    else:
        result.append(int(i[0]))
count_b = len(result)
result_sum = sum(result)
iter = 0
for i in a_list:
    iter += 1
    cash = result[-1]
    del(result[-1])
    count_b -= 1
    result.insert(0, int(i[0]))
    print(result)
    if result_sum < sum(result):
        del(result[0])
        result.append(cash)
        count_b += 1
        break
    else:
        result_sum = sum(result)
print(count_b, m - sum(result))


def create_basket(goods, N, money):
    # на вход товары по возрастанию цены, кол-во товаров, кол-во денег
    # на выходе кол-во товаров В и остаток денег

    a_goods = list(filter(lambda x: x[1] == 'A', goods))
    b_goods = list(filter(lambda x: x[1] == 'B', goods))
    size, a_size, b_size, v_money = 0, 0, 0, money

    # определяем максимальное кол-во товаров, которое можем купить
    for g in goods:
        if v_money >= g[0]:
            size += 1
            v_money -= g[0]
        else:
            break

        # если можем купить все товары
        if size == N:
            return (len(b_goods), v_money)

    # заполняем корзину товарами B
    for g in b_goods:
        if money >= g[0]:
            b_size += 1
            money -= g[0]
        else:
            break

    # пока не достигнем нужного размера, добавляем товары А
    # удаляя самый дорогой товар В если закончились деньги
    while (b_size + a_size < size):
        if money >= a_goods[a_size][0]:
            money -= a_goods[a_size][0]
            a_size += 1
        else:
            b_size -= 1
            money += b_goods[b_size][0]
    return [b_size, money]


goods = []
with open('26.txt') as f:
    N, M = map(int, f.readline().split())
    for line in f:
        a, b = line.split()
        goods.append([int(a), b])
    goods.sort(key=lambda x: x[0])

print(create_basket(goods, N, M))










