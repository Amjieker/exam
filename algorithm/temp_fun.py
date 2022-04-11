import datetime

import pymysql
from algorithm import const_data
from algorithm import oper_func

conn = pymysql.connect(
    host='127.0.0.1',
    user=const_data.username,
    passwd=const_data.password,
    port=3306,
    db=const_data.mysqldb,
    charset='utf8'
)


def get_allTeacher():
    cur = conn.cursor()
    cur.execute(const_data.sql_get_teacher_course % (const_data.year, const_data.semester))
    list_res = []
    for loop in cur.fetchall():
        t = [
            loop[7],
            loop[9],
            loop[14],
            loop[11],
            oper_func.split_num(loop[3]),  # 第几周
            oper_func.split_num(loop[5]),  # 第几节课
            loop[4]  # 星期几
        ]
        list_res.append(t)
        # print(loop)
    return list_res


# print(get_allTeacher())

def get_arrangement():
    cur = conn.cursor()
    cur.execute(const_data.sql_get_arrange)
    res_map = {}
    for loop in cur.fetchall():
        tmp_list = res_map.get(loop[0], [])
        tmp_list.append(loop)
        res_map[loop[0]] = tmp_list
    return res_map


def get_teacher():
    cur = conn.cursor()
    cur.execute(const_data.sql_get_Teacher)
    tm_mp = {}
    for loop in cur.fetchall():
        # print(loop)
        tm_mp[loop[0]] = (loop[0], loop[1], loop[2])
    return tm_mp


# get_teacher()


# get_allTeacher()

# print(get_arrangement())
# for i, b in get_arrangement().items():
#     print(i)
#     for j in b:
#         print(j)
def get_exam_back_id():
    cur = conn.cursor()
    cur.execute(const_data.sql_get_last_exam)
    return cur.fetchone()[0]


def insert_exam_notion(teacher_account, title, exam_course, exam_address, exam_date, exam_person, ids=None):
    cur = conn.cursor()
    if ids is None:
        ids = get_exam_back_id()
    cur.execute(const_data.sql_set_notion % (
        teacher_account,
        title,
        exam_course,
        exam_address,
        exam_date,
        exam_person,
        ids
    ))
    conn.commit()


# insert_exam_notion("11101", "111", "计算机", "A6-215", "2022-02-27 21:10:36", "22")

def set_arrange(teacher_account, exam_id, invigilate_state):
    cur = conn.cursor()
    cur.execute(
        const_data.sql_set_arrange % (
            teacher_account,
            exam_id,
            invigilate_state,
            datetime.datetime.now().__str__()
        )
    )
    conn.commit()
