# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 11:38
# @Author  : MaxLong
# @Project : flask_mock
# @FileName: days.py
# @Software: PyCharm
# @Contact : MaxLongGlobal
import time
from datetime import date


year,month,day = map(int,input().split('/'))


def day_of_year(year1, month1, day1, xq):
    if xq >= 6:
        print("距离周末还有:", 0, end="天\n")
    else:
        print("距离周末还有:", 6 - xq, end="天\n")

    d_qm = date(year1, 4, 5) - date(year1, month1, day1)
    if d_qm.days >= 0:
        print("距离清明还有:", d_qm.days, end="天\n")

    d_wy = date(year1, 5, 1) - date(year1, month1, day1)
    if d_wy.days >= 0:
        print("距离五一还有:", d_wy.days, end="天\n")

    d_dw = date(year1, 6, 3) - date(year1, month1, day1)
    if d_dw.days >= 0:
        print("距离端午还有:", d_dw.days, end="天\n")

    d_zq = date(year1, 9, 10) - date(year1, month1, day1)
    if d_zq.days >= 0:
        print("距离中秋还有:", d_zq.days, end="天\n")

    d_gq = date(year1, 10, 1) - date(year1, month1, day1)
    if d_gq.days >= 0:
        print("距离国庆还有:", d_gq.days, end="天\n")

    d_yd = date(year1 + 1, 1, 1) - date(year1, month1, day1)
    if d_yd.days >= 0:
        print("距离元旦还有:", d_yd.days, end="天\n")

    d_cj = date(year1 + 1, 1, 22) - date(year1, month1, day1)
    if d_cj.days >= 0:
        print("距离春节还有:", d_cj.days, end="天\n")


# -*- main -*-
if __name__ == '__main__':
    # print('Hello, MaxLongGlobal! Welcome to use python.')
    dd = time.strftime('%Y-%m-%d-%w').split('-')
    year, month, day, xq = int(dd[0]), int(dd[1]), int(dd[2]), int(dd[3])
    # day_of_year(year, month, day, xq)
