def binary_s(target, lst, left_p=0, right_p=0):

    # sets pointers at start of search
    if left_p == 0 and right_p == 0 and len(lst) > 1:
        right_p = len(lst)

    # sets midpoint between left and right pointers
    mp = left_p + ((right_p - left_p) // 2)

    # if target number found
    if lst[mp] == target:
        return {"num": target, "index": mp}

    # number not found in list
    elif abs(left_p - right_p) == 1:
        return False

    # number greater or smaller than midpoint
    elif target < lst[mp]:
        right_p = mp
    else:
        left_p = mp

    # iterates through function again
    return binary_s(target, lst, left_p, right_p)
