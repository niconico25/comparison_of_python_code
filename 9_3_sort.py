import funcscale
import random


def comparison():
    funcscale.function_list = [
        bubble_sort_,
        insertion_sort_,
        heap_sort_,
        merge_sort_,
        quick_sort_,
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**i) for _ in range(10**i)], ), {})
        for i in range(4)
    ]
    funcscale.str_argument_list = [
        f'[randint(0, 10**{i}) for i in range(0, 10**{i})]'
        for i in range(4)
    ]
    funcscale.compare()


#
# bubble sort
#
def bubble_sort(lst):
    n = len(lst)
    for i in reversed(range(n)):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_(lst):
    bubble_sort(lst)
    return lst


#
# insertion sort
#
def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]


def insertion_sort_(lst):
    insertion_sort(lst)
    return lst


#
# merge sort
#
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return

    left = lst[:n // 2]
    right = lst[n // 2:]
    lst.clear()
    merge_sort(left)
    merge_sort(right)

    left.reverse()
    right.reverse()
    while left and right:
        if left[-1] <= right[-1]:
            lst.append(left.pop())
        else:
            lst.append(right.pop())

    while left:
        lst.append(left.pop())
    while right:
        lst.append(right.pop())


def merge_sort_(lst):
    merge_sort(lst)
    return lst


#
# quick sort
#
def quick_sort(lst):
    if not lst:
        return []

    center = lst.pop()
    left = quick_sort([e for e in lst if e <= center])
    right = quick_sort([e for e in lst if center < e])
    return left + [center] + right


def quick_sort_(lst):
    return quick_sort(lst)


#
# heap sort
#
def heap_sort(lst):
    heapify(lst)
    return [heappop(lst) for _ in range(len(lst))]


def heap_sort_(lst):
    return heap_sort(lst)


# そのまま from heapq import heappop してしまうと
# C 言語実装の heapop が import されて鬼のように速くなるので
# heapq.py からコピペ
def heappop(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapify(x):
    n = len(x)
    for i in reversed(range(n // 2)):
        _siftup(x, i)


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2 * pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


#
# main
#
if __name__ == '__main__':
    comparison()
