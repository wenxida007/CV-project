def union(au, bu, area_intersection):
    """计算并集面积
    :param au: a框坐标
    :param bu: b框坐标
    :param intersection: 交集面积
    :return:
    """
    # a框面积
    area_a = (au[2] - au[0]) * (au[3] - au[1])

    # b框面积
    area_b = (bu[2] - bu[0]) * (bu[3] - bu[1])

    # a+b面积-交集面积
    area_union = area_a + area_b - area_intersection
    return area_union


def intersection(ai, bi):
    """计算交集
    :param ai: a框坐标
    :param bi: b框坐标
    :return:
    """
    # 1、求出交集的左上角点
    # ai和bi的左上角的x谁更大
    # ai和bi的左上角的y谁更大
    x_left = max(ai[0], bi[0])
    y_left = max(ai[1], bi[1])

    # 2、求出交集的右下角点
    x_right = min(ai[2], bi[2])
    y_right = min(ai[3], bi[3])

    # 求出长宽
    w = x_right - x_left
    h = y_right - y_left

    if w < 0 or h < 0:
        return 0
    return w * h


def IoU(a, b):
    """计算交并比
    :param a: a框坐标
    :param b: b框坐标
    :return:
    """
    # 1、做异常处理
    if a[0] >= a[2] or a[1] >= a[3] or b[0] >= b[2] or b[1] >= b[3]:
        return 0.0

    # 2、计算交并比，计算交集，计算并集  交集/并集+epsilon
    area_i = intersection(a, b)
    area_u = union(a, b, area_i)

    return float(area_i) / float(area_u + 1e-6)


if __name__ == '__main__':
    # 假设一个图片10 x 10的大小，左上角(0, 0) 右下角(10, 10)
    # A框：(1, 1, 5, 5)，B框：(3, 3, 6, 6)#
    a = (1, 1, 5, 5)
    b = (1, 1, 6, 6)
    print("交并比为：%f" % IoU(a, b))