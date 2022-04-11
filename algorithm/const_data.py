# 宜宾校区 与 李白河校区 时间
time_mapping_case1 = {
    '1': ["8:50", "9:35"],
    '2': ["9:45", "10:30"],
    '3': ["10:45", "11:30"],
    '4': ["11:40", "12:25"],
    '5': ["12:35", "13:00"],
    '6': ["13:10", "13:40"],
    '7': ["13:50", "14:35"],
    '8': ["14:45", "15:30"],
    '9': ["15:45", "16:30"],
    '10': ["16:40", "17:25"],
    '11': ["18:30", "19:15"],
    '12': ["19:25", "20:10"],
    '13': ["20:20", "21:05"],
    '14': ["21:15", "22:00"]
}
# 汇东校区时间
time_mapping_case2 = {
    '1': ["8:15", "9:00"],
    '2': ["9:10", "9:55"],
    '3': ["10:20", "11:05"],
    '4': ["11:15", "12:00"],
    '5': ["14:30", "15:15"],
    '6': ["15:25", "16:10"],
    '7': ["16:20", "17:05"],
    '8': ["17:15", "18:00"],
    '9': ["19:00", "19:45"],
    '10': ["19:55", "20:40"]
}

# 周一到周日映射
week_day_dict = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期日',
}

# 当前年份
year = "2021"
# 当前学期
semester = "2"
# 当前学期起始周日期
cur_semester_start_date = "2021-8-30"

# connect mysql

username = "root"
password = "3306066"
mysqldb = "exam"

sql_get_Teacher = \
    '''
        SELECT
            teacher_account_id,
            name,
            address,
            college_id
        FROM
            teacher_teacher
    '''
sql_get_arrange = \
    '''
        SELECT
        teacher_teacher.teacher_account_id,
        teacher_teacher.name,
        arrange_exam.date,
        arrange_exam.time_length,
        arrange_exam.address,
        arrange_arrange.invigilate_state
    
        FROM
            teacher_teacher,
            arrange_exam,
            arrange_arrange 
        WHERE
            teacher_teacher.teacher_account_id = arrange_arrange.teacher_account_id
        AND arrange_exam.id = arrange_arrange.exam_id_id
    '''
sql_get_teacher_course = \
    '''
        SELECT
            *
        FROM
            teacher_course
            JOIN teacher_teacher ON teacher_teacher.teacher_account_id = teacher_course.teacher_account_id
        WHERE year = %s AND semester = %s
    '''

sql_get_last_exam = \
    '''
    SELECT
        * 
    FROM
        arrange_exam 
    ORDER BY
        id DESC 
        LIMIT 1
    '''

sql_set_notion = \
    '''
    INSERT INTO `exam_arrange`.`notification` 
    ( `teacher_account`, `title`, `exam_course`, 
    `exam_address`, `exam_date`, `exam_person`, `exam_id` )
    VALUES
        (
            '%s',
            '%s',
            '%s',
            '%s',
            '%s',
            '%s',
            %s
        )
    '''

sql_set_arrange = \
    '''
        INSERT INTO `exam_arrange`.`exam_arrange` 
        ( `teacher_account`, `exam_id`, `invigilate_state`, `arrange_date` )
        VALUES
            (
                '%s',
                %s,
                '%s',
                '%s'
            )
    '''
