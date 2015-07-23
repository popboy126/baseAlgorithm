#-*-coding: utf-8-*-


#直接插入排序
def InsertPos(array, highpos, value):
    """
    查找待查入的位置
    :param array: 待插入数据数组
    :param highpos: 数组中有序部分的最大坐标
    :param value: 插入的数据值
    :return: 返回插入位置
    """
    for i in range(highpos - 1, -1, -1):
        if value >= array[i]:               #哨兵的作用体现在这里
            break;
    return i + 1               #最小位置为1


def InsertSort(array, isreversed = False):
    """
    直接插入排序
    :param araay: 待做插入排序的列表或是元组数据
    :param isreversed: 是否逆序输出
    :return: 返回排序后的结果
    """
    UnSortArray = [0]
    UnSortArray.extend(array)   #这么做的目的是增加哨兵位
    for i in range(2, len(UnSortArray)):
        #开始主循环过程
        UnSortArray[0] = UnSortArray[i]     #设置哨兵
        pos = InsertPos(UnSortArray, i, UnSortArray[i]) #查找位置
        #后移记录
        for j in range(i, pos, -1):
            UnSortArray[j] = UnSortArray[ j - 1 ]
        UnSortArray[pos] = UnSortArray[0]       #完成数据插入

    return UnSortArray[:0:-1] if isreversed else UnSortArray[1:]