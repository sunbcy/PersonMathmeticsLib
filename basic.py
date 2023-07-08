# permutation
def fact_op(num):
    """factorial operation--迭代操作"""
    ret_n = 1
    n = 1
    while n < num+1:
        ret_n *= n
        n += 1
    return ret_n


def permutation(n, r):
    """排列
    ret = n! / (n-r)!
    """
    return int(fact_op(n) / fact_op(n-r))


# combination
def combination(n, r):
    """组合
    ret = n! / ((r!) * (n-r)!)
    """
    return int(fact_op(n) / (fact_op(r) * fact_op(n-r)))


print(combination(10, 4))
