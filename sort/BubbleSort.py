#-*-coding: utf-8-*-

#冒泡排序


def BubbleSort(array, isreversed = False):
    """
    此函数实现冒泡排序
    :param array:  为待排序列表或元组
    :param isreversed: 为假表示升序排，为真表示降序排
    :return: 返回已排序的结果
    """
    UnsortArray = list(array)
    SortFlag = True    #交换标志
    while SortFlag:
        SortFlag = False
        for i in range(1, len(UnsortArray)):
            if UnsortArray[i] < UnsortArray[i - 1]:
                tmp = UnsortArray[i - 1]
                UnsortArray[i - 1] = UnsortArray[i]
                UnsortArray[i] = tmp
                SortFlag = True
    else:
        return UnsortArray[::-1] if isreversed else UnsortArray
