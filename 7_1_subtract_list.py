import funcscale


def comparison():
    funcscale.function_list = [
        subtract_list_try_remove,
        subtract_list_for_if,
        subtract_list_while_if_pop,
    ]
    funcscale.argument_list = [
        ((list1, list2), {}),
        ((list3, list4), {}),
        ((list5, list6), {}),
    ]
    funcscale.compare()


list1 = [i for i in range(100, 199)]
list2 = [i for i in range(200, 299)]
list3 = [i for i in range(100, 199)]
list4 = list(reversed(list1))
list5 = [i for i in range(1000, 1999)]
list6 = [i for i in range(2000, 2999)]


#
#
#
def subtract_list_try_remove(lst1, lst2):
    lst = lst1.copy()
    for element in lst2:
        try:
            lst.remove(element)
        except ValueError:
            continue
    return lst


def subtract_list_for_if(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        for i, e1 in enumerate(lst):
            if e1 == e2:
                del lst[i]
                break
    return lst


def subtract_list_while_if_pop(lst1, lst2):
    lst = []
    lst1 = lst1.copy()
    lst2 = lst2.copy()
    lst2_c = []
    while lst1:
        e1 = lst1.pop()
        while lst2:
            e2 = lst2.pop()
            if e1 == e2:
                break
            lst2_c.append(e2)
        else:
            lst.append(e1)
        lst2.extend(lst2_c)
        lst2_c.clear()
    lst.reverse()
    return lst


#
#
#
if __name__ == '__main__':
    comparison()


"""
# これはいらないかな....
def subtract_list_while_if_del(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        n = len(lst)
        i = 0
        while i < n:
            if lst[i] == e2:
                del lst[i]
                break
            i += 1
    return lst


    # コンセプト
    #  del を使わない
    #  while 文
    #
    # これまで見てきた通り del を使うとリストの再構成が起こります。
    # そこで while 文を使って del を使わない書き方にあらためてみました。
    #
    # リストの再構成をなくせばいいかなと思ったけど
    # そうでもなかった
    # ただ、あるデータの性質がある時は異常に速くなる。
    # なんだあれ？
"""
