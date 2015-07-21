#-*-coding: utf-8-*-

#快速排序

#分块函数
def Partition(array, lowpos, highpose):
    """
    返回一趟快排结果
    :param array: 列表待排序数组
    :param lowpos: 低位位置
    :param highpose: 高位位置
    :return: 返回枢轴位置
    """
    pivotkey = array[lowpos]    #默认选第一个元素为枢轴
    while lowpos < highpose:
        #开始从高端开始
        while (lowpos < highpose) and (array[highpose] >= pivotkey):
            highpose -= 1
        else:
            array[lowpos] = array[highpose]
        #下面开始低端
        while (lowpos < highpose) and (array[lowpos] <= pivotkey):
            lowpos += 1
        else:
            array[highpose] = array[lowpos]
    #一遍快排结束
    array[lowpos] = pivotkey
    return lowpos   #返回位置

#快排递归函数
def QSort(array, lowpos, highpos):
    """
    用递归的方式来实现快排
    :param array: 待排序数组
    :param lowpos: 最低位
    :param highpos: 最高位
    :return: 无返回值
    """
    if lowpos < highpos:
        pivotloc = Partition(array, lowpos, highpos)    #一轮排序
        QSort(array, lowpos, pivotloc - 1)
        QSort(array, pivotloc + 1, highpos)



def QuickSort(array, isreversed = False):
    """
    实现快速排序
    :param array: 元组或列表
    :param isreversed: 是否逆序
    :return: 返回结果
    """
    UnsortArray = list(array)
    QSort(UnsortArray, 0, len(UnsortArray) - 1)
    return UnsortArray[::-1] if isreversed else UnsortArray #判断结果是否需要逆序


