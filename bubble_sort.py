"""
冒泡排序 (Bubble Sort) 算法

原理：重复遍历列表，比较相邻元素并交换，使较大元素逐步"冒泡"到末尾。
时间复杂度：最好 O(n)，平均/最坏 O(n²)
"""


def bubble_sort(arr):
    """
    冒泡排序 - 原地排序

    Args:
        arr: 待排序的列表

    Returns:
        排序后的列表（原地修改）
    """
    n = len(arr)

    for i in range(n):
        swapped = False  # 优化：若本轮无交换则已有序，可提前结束

        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def bubble_sort_desc(arr):
    """
    冒泡排序 - 降序版本
    """
    n = len(arr)

    # 外层循环控制排序轮数，每一轮将本轮最大值“冒泡”到未排序区间的末尾
    for i in range(n):
        swapped = False  # 标记本轮是否发生了交换（用于优化）
        # 内层循环负责遍历未排序区间，相邻元素两两比较并交换
        for j in range(0, n - 1 - i):
            # 若前一个元素小于后一个元素，则交换（实现降序）
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True   # 发生交换
        # 如果一整轮下来没有发生过交换，说明已排序，提前结束
        if not swapped:
            break

    return arr  # 返回排序后的数组（原地修改）


if __name__ == "__main__":
    # 测试数据：1234567 的各位数字（乱序）
    # 准备测试数据，包含 1~7 的乱序数字
    data = [7, 2, 5, 1, 6, 3, 4]
    print("原始数据:", data)  # 输出初始数组
    bubble_sort(data)         # 对数组进行升序排序
    print("升序结果:", data)   # 输出排序后的数组

    # 测试降序
    data2 = [3, 7, 1, 5, 2, 6, 4]
    print("\n原始数据:", data2)
    bubble_sort_desc(data2)
    print("降序结果:", data2)


    # Python 中的变量是对内存中某个值的引用或“名字”。
    # 你可以把变量理解成一个“标签”，用来指向存储数据的地方。
    