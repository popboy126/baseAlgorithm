#-*-coding: utf-8-*-

#堆排序


#调整为大顶堆
def HeapAdjust(array, startpos):
    """
    调整为大顶堆
    :param array: 待调整堆
    :param startpos: 开始位置
    :return: 无返回值
    """
    m = len(array) - 1
    if m < 1:
        return None
    array[0] = array[startpos]        #记录当前值
    i = 2 * startpos
    while i <= m:
        if i < m and array[i] <= array[i + 1]:
            i += 1
        if array[0] >= array[i]:
            break
        array[startpos] = array[i]
        startpos = i
        i *= 2
    array[startpos] = array[0]

def HeapSort(array, isreversed = False):
    """
    堆排序主体函数
    :param array: 待排序数组
    :param isreversed: 是否逆序
    :return: 返回排序结果
    """
    UnsortArray = [0]
    UnsortArray.extend(array)
    SortedArray = list()
    m = len(array) - 1
    for i in range(m / 2, 0, -1):
        HeapAdjust(UnsortArray, i)
    #下面开始排序
    while len(UnsortArray) > 1:
        #先输出
        SortedArray.append(UnsortArray[1])
        UnsortArray[1] = UnsortArray[-1]
        UnsortArray.pop(-1)

        #调整堆
        HeapAdjust(UnsortArray, 1)

    return SortedArray[::-1] if not isreversed else SortedArray

