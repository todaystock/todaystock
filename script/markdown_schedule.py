# coding=utf-8
import time
import os
import os.path as osp

def is_leap_year(year):
    # 判断是否为闰年
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def get_num_of_days_in_month(year, month):
    # 给定年月返回月份的天数
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


def get_total_num_of_day(year, month):
    # 自1800年1月1日以来过了多少天
    days = 0
    for y in range(1800, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365

    for m in range(1, month):
        days += get_num_of_days_in_month(year, m)

    return days


def get_start_day(year, month):
    # 返回当月1日是星期几，由1800.01.01是星期三推算
    return 3 + get_total_num_of_day(year, month) % 7


# 月份与名称对应的字典
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def get_month_name(month):
    # 返回当月的名称
    return month_dict[month]


def print_month_title(year, month, cal):
    # 打印日历的首部

    cal.write('   ' + str(year) + '/' + str(month) + '\n')
    cal.write('   ' + str(get_month_name(month)) +  '  ' + str(year) + '\n')
    cal.write('Sun | Mon | Tue  | Wed | Thu | Fri | Sat \n')
    cal.write('日 | 一 | 二  | 三 | 四 | 五 | 六  \n')
    cal.write('---| ---| ---| ---| ---| ---| ---|\n')


def print_month_body(year, month):
    '''
    打印日历正文
    格式说明：空两个空格，每天的长度为5
    需要注意的是print加逗号会多一个空格
    '''
    i = get_start_day(year, month)
    if i != 7:
        # cal.write(' ') # 打印行首的两个空格
        cal.write('  |')
        cal.write('  |' * (i %7))   # 从星期几开始则空5*几个空格
    for j in range(1, get_num_of_days_in_month(year, month)+1):
        cal.write(' [' + str(j) + '](#' + str(month) + str(j) + ') |')# 宽度控制，4+1=5
        i += 1
        if i % 7 == 0:  # i用于计数和换行
            cal.write('\n')   # 每换行一次行首继续空格

def print_month_body_index(year, month, cal):
    '''
    打印日历正文
    格式说明：空两个空格，每天的长度为5
    需要注意的是print加逗号会多一个空格
    '''
    i = get_start_day(year, month)
    if i != 7:
        # cal.write(' ') # 打印行首的两个空格
        cal.write('  |')
        cal.write('  |' * (i %7))   # 从星期几开始则空5*几个空格
    for j in range(1, get_num_of_days_in_month(year, month)+1):
        dirstr = './stocktime/' + str(year) + '/' + str(month) + '/' + str(j)
        A_file = osp.join(dirstr, 'A.md')
        H_file = osp.join(dirstr, 'H.md')
        US_file = osp.join(dirstr, 'US.md')
        img_dir = osp.join(dirstr, 'imgs')
          
        if not osp.exists(dirstr):
            os.makedirs(dirstr)
        if not osp.exists(img_dir):
            os.makedirs(img_dir)
        
        if not osp.exists(A_file):
            new_file = open(A_file,"w")
            new_file.close()
        if not osp.exists(H_file):
            new_file = open(H_file,"w")
            new_file.close()
        if not osp.exists(US_file):
            new_file = open(US_file,"w")
            new_file.close()

        cal.write(' [' + str(j) + '](' + dirstr + ') |')# 宽度控制，4+1=5
        i += 1
        if i % 7 == 0:  # i用于计数和换行
            cal.write('\n')   # 每换行一次行首继续空格

def run():
    #   主函数部分
    # year = int(input("Please input target year:"))
    # month = int(input("Please input target month:"))
    from datetime import datetime
    year = datetime.today().year
    month = datetime.today().month

    cal = open(str(year) + '-' + str(month) + '-日历markdown版.txt','w')
    print_month_title(year, month, cal)
    print_month_body_index(year, month, cal)
    cal.close()

if __name__ == "__main__":
    run()