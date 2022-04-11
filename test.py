from algorithm import arrange

test_data = {
    # 考试时间，考试长度，安排教师人数 。。。 形如这样的数据
    "exam_name": "计算机网络考试",
    "exam_date": "2022-01-09 0:25:01",
    "exam_len": 2.5,
    "exam_address": "A6-215",
    "exam_count": 2
}

# 处理监考排序
a, b = arrange.arrange(exam_count=1, exam_date="2022-01-09 0:25:01", exam_len=float(1.01))

print(a, b)
# 注意在 这之前，一定要把本场考试信息存入数据库中

# 开始存入通知信息和监考安排信息

# for loop in a:
#     arrange.notion(
#         teacher_account = loop,
#         title = "yes",
#         exam_course="yes",
#         exam_address="A6-215",
#         exam_date="2022-01-09 0:25:01",
#         exam_person="22"
#     )
#     arrange.set_arrange(loop)
#     print(loop)

# 注意，重新安排监考请调用时加上考试编号
'''
for loop in a:
    arrange.notion(
        teacher_account = loop,
        title = "yes",
        exam_course="yes",
        exam_address="A6-215",
        exam_date="2022-01-09 0:25:01",
        exam_person="22"
        exam_id = xxx
    )
    arrange.set_arrange(loop, exam_id)
'''
