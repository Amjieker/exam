from algorithm import const_data
from algorithm import oper_func
from algorithm import temp_fun
import datetime
import importlib
'''
test_data = {
    # 考试时间，考试长度，安排教师人数 一定需要
    ("exam_name", "计算机网络考试"),
    ("exam_date", "2022-01-09 10:00:00"),
    ("exam_len", 2.5),
    ("exam_address", "A6-215"),
    ("exam_count", 2)
}
'''

arranged_teacher_info = {}
course_teacher_info = []
course_teacher_map = {}
person = []
arranged_teacher_count = []


def init():
    importlib.reload(temp_fun)
    global arranged_teacher_info
    global course_teacher_map
    global course_teacher_info
    global person
    global arranged_teacher_count
    arranged_teacher_info = temp_fun.get_arrangement()
    course_teacher_info = temp_fun.get_allTeacher()
    course_teacher_map = {}
    arranged_teacher_count = []
    person = temp_fun.get_teacher()
    for loop in course_teacher_info:
        temp = course_teacher_map.get(loop[0], [])
        temp.append((loop[4], loop[5], loop[6]))
        course_teacher_map[loop[0]] = temp
    # 预处理监考次数

    for key, val in arranged_teacher_info.items():
        arranged_teacher_count.append((key, len(val)))
    for key, val in course_teacher_map.items():
        x_cnt = arranged_teacher_info.get(key, 0)
        if x_cnt == 0:
            arranged_teacher_count.append((key, 0))
    for loop in person:
        x_cnt = arranged_teacher_info.get(loop, 0)
        if x_cnt == 0:
            arranged_teacher_count.append((loop, 0))

    arranged_teacher_count = list(
        sorted(arranged_teacher_count, key=lambda cmp: cmp[-1])
    )

def check_course_table(teacher_num, what_day, now_week, begin, lens):
    t_list = course_teacher_map.get(teacher_num)
    if t_list is None:
        return True
    # print(what_day, now_week, begin)
    for i in t_list:
        for j in i[0]:
            # print(list(range(int(j[0]), int(j[-1]))), now_week)
            if now_week in list(range(int(j[0]), int(j[-1]) + 1)):
                if what_day == i[2]:
                    for k in i[1]:
                        a, b = oper_func.now_time(begin, k[0], k[-1])
                        # print(a, b, begin)
                        if (
                                oper_func.time_cmp(
                                    begin.__str__(),
                                    lens,
                                    a.__str__()
                                ) == 0
                        ) or (
                                oper_func.time_cmp(
                                    begin.__str__(),
                                    lens,
                                    b.__str__()
                                ) == 0
                        ):
                            return False
                    # print(teacher_num, k, j, end=" ")
                    # print(a, end=" ")
                    # print(b)
    return True


def check_arrange_table(x, begin, lens):
    t = arranged_teacher_info.get(x)
    if t is None:
        return True
    for i in arranged_teacher_info[x]:
        print(i)
        print(oper_func.time_cmp(
            i[2].__str__(),
            i[3],
            begin.__str__()
        ), oper_func.time_cmp(
            i[2].__str__(),
            i[3],
            (begin + datetime.timedelta(hours=lens)).__str__()
        ))
        if (
                oper_func.time_cmp(
                    i[2].__str__(),
                    i[3],
                    begin.__str__()
                ) == 0
        ) or (
                oper_func.time_cmp(
                    i[2].__str__(),
                    i[3],
                    (begin + datetime.timedelta(hours=lens)).__str__()
                ) == 0
        ):
            return False
    return True


# def arrange(pack):
def arrange(exam_count, exam_date, exam_len):
    # count = pack["exam_count"]
    # date = pack["exam_date"]
    # lens = pack["exam_len"]
    print(type(exam_count), exam_count)
    print(type(exam_date), exam_date)
    print(type(exam_len), exam_len)
    init()
    # print(person)
    # print(arranged_teacher_info)
    # print(course_teacher_map)
    # print(course_teacher_info)
    # print(arranged_teacher_count)
    count = exam_count
    date = exam_date
    lens = exam_len
    begin = oper_func.transfer_date(date)
    what_day = oper_func.transfer_week(begin)  # 星期几
    now_week = oper_func.cur_week(const_data.cur_semester_start_date, begin.date().__str__())  # 第几周
    ans = []
    for i in arranged_teacher_count:
        print(i)
        x, y = i[0], i[1]
        # print(check(x, what_day, now_week, begin, lens))
        if check_course_table(x, what_day, now_week, begin, lens) is False:
            continue
        if check_arrange_table(x, begin, lens) is False:
            continue

        # print("check to ", x, person[x])
        ans.append(x)
        count -= 1
        if count == 0:
            break
    if count > 0:
        return None, "寻找失败，没有合适的教师，请重新考试时间"
    else:
        return ans, "匹配成功"


def repeat_arrange(exam_count, exam_date, exam_len=1):
    return arrange(exam_count, exam_date, exam_len)


def notion(teacher_account, title, exam_course, exam_address, exam_date, exam_person, exam_id=None):
    temp_fun.insert_exam_notion(teacher_account, title, exam_course, exam_address, exam_date, exam_person, exam_id)


def set_arrange(teacher_account, ids=None):
    if ids is None:
        ids = temp_fun.get_exam_back_id()
    temp_fun.set_arrange(teacher_account, ids, 0)
