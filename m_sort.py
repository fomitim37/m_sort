"""This programm sorts the array that user had entered."""

def m_sort(l_start):
    """This the function that sorts the array."""

    l_left = l_start[:int(len(l_start) / 2)]
    l_right = l_start[int(len(l_start) / 2):]

    if len(l_left) == 1 or len(l_right) == 1:
        return merge(l_left, l_right)


    l_left = m_sort(l_left)
    l_right = m_sort(l_right)

    return merge(l_left, l_right)

def merge(l_left, l_right):
    """This the second function that sorts halfes of array."""

    l_ret = []
    p_1 = 0
    p_2 = 0
    while True:
        if p_1 == len(l_left) or p_2 == len(l_right):

            if p_1 == len(l_left):
                for i in range(len(l_right) - p_2):
                    l_ret.append(l_right[p_2 + i])
            elif p_2 == len(l_right):
                for i in range(len(l_left) - p_1):
                    l_ret.append(l_left[p_1 + i])

            break

        if l_left[p_1] < l_right[p_2]:
            l_ret.append(l_left[p_1])
            p_1 += 1
        elif l_left[p_1] > l_right[p_2]:
            l_ret.append(l_right[p_2])
            p_2 += 1
        elif l_left[p_1] == l_right[p_2]:
            l_ret.append(l_left[p_1])
            p_1 += 1

    return l_ret


print(m_sort([2, 6, 12, 125, 4, 100, 1]))
