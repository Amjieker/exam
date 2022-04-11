import re
import datetime
from algorithm import const_data

# 正则数字匹配
re_number = re.compile(r"\d+")


# 选择对应的课程时间
def check_course_time(tag=1):
    if tag == 1:
        return const_data.time_mapping_case1
    else:
        return const_data.time_mapping_case2


# 分割字符区间
def split_num(st: str):
    spit_list = st.split(',')
    num_list = []
    for each in spit_list:
        temp = re_number.findall(each)
        num_list.append((temp[0], temp[-1]))
    return num_list


# 转换星期几

def transfer_week(date: datetime.date):
    return const_data.week_day_dict[date.weekday()]


# 转换时间
def transfer_date(st: str) -> datetime.datetime:
    fmt_str = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
    return fmt_str


# 判断时间是否符合
def time_diff(begin: datetime.time, end: datetime.time, cmp: datetime.time):
    if cmp < begin:
        return -1  # "未开始"
    if cmp > end:
        return 1  # "已结束"
    return 0  # "正在进行"


# dist of len

# def time_add_dist(times: datetime.datetime, lens: float, cmp: datetime.datetime):
def time_cmp(times: str, lens: float, cmp: str):
    times_trans = transfer_date(times)
    cmp_trans = transfer_date(cmp)
    if times_trans.date() == cmp_trans.date():
        return time_diff(
            times_trans.time(),
            (times_trans + datetime.timedelta(hours=float(lens))).time(),
            cmp_trans.time()
        )
    elif times_trans.date() > cmp_trans.date():
        return 1
    elif times_trans.date() < cmp_trans.date():
        return -1


def cur_week(base_date: str, now_date: str):
    return (
                   datetime.datetime.strptime(now_date, "%Y-%m-%d") -
                   datetime.datetime.strptime(base_date, "%Y-%m-%d")
           ).days // 7 + 1


def now_time(base_date: datetime.datetime, begin: str, end: str):
    return (
        datetime.datetime.strptime(
            base_date.date().__str__() + " " +
            const_data.time_mapping_case1[begin][0],
            "%Y-%m-%d %H:%M"),
        datetime.datetime.strptime(
            base_date.date().__str__() + " " +
            const_data.time_mapping_case1[end][-1],
            "%Y-%m-%d %H:%M")
    )


if __name__ == "__main__":
    print(time_cmp("2022-02-25 02:00:00", 2.5, "2022-02-25 04:30:01"))
    print(cur_week("2021-8-30", "2022-1-9"))
    print(now_time(transfer_date("2022-02-25 02:00:00"), '1', '2'))
