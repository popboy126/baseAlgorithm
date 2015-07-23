#-*-coding: utf-8-*-

#简单选择排序

def SelectMin(array, startpos):
    """
    找出数组中从startpos位置开始最小的数的位置
    :param array: 待查找数组
    :param startpos: 开始查找位置
    :return: 最小数的位置
    """
    minvalue = array[startpos]
    pos = startpos
    for i in range(startpos, len(array)):
        #开始查找
        if(array[i] < minvalue):
            minvalue = array[i]
            pos = i
    return pos

def SimpleSelectSort(array, isreversed = False):
    """
    简单选择排序主函数
    :param array: 待排序数组，元组或列表
    :param isreversed: 是否需要逆序
    :return: 返回排序结果
    """
    UnsortArray = list(array)
    for i in range(len(UnsortArray)):
        #开始选择过程
        pos = SelectMin(UnsortArray, i)  #选择第i小的数
        if(i != pos):
            tmp = UnsortArray[i]
            UnsortArray[i] = UnsortArray[pos]
            UnsortArray[pos] = tmp
    return UnsortArray[::-1] if isreversed else UnsortArray
