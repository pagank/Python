from example import Student
from example import Teacher
from example import Course


def introduction(tital):
    print("***************{0}***************".format(tital))


def prepare_course():
    """ 课程信息初始化方法 """
    cour_dict = {"01": "网络爬虫", "02": "数据分析",
                 "03": "人工智能", "04": "机器学习",
                 "05": "云计算", "06": "大数据",
                 "07": "图像识别", "08": "Web开发"
                 }
    li = []
    for key in cour_dict:
        # print(key +":" + cour_dict[key])
        cour = Course(cour_dict[key], key)
        li.append(cour)
    #print(li)
    return li


def create_teacher():
    """ 教师初始化方法 """
    teacher_li = [["T1", "张良", "1367746666"],
                  ["T2", "王鹏", "1362w675985"],
                  ["T3", "李旭", "13363700365"],
                  ["T4", "黄国发", "1808936523"],
                  ["T5", "周勤", "132453785"],
                  ["T6", "谢弗顺", "1328580412"],
                  ["T7", "将教师", "1324265456"],
                  ["T8", "杨老佬", "1324567457"]
                  ]
    li = []
    for item in teacher_li:
        teach = Teacher(item[1], item[0], item[2])
        li.append(teach)

    #print(li)
    return li


def course_to_teacher():
    li = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()

    count = len(ls_teacher) - 1
    for cour in ls_course:
        li.append(cour.binding(ls_teacher[count]))
        if count >= 0:
            count -= 1
        else:
            break
    #print(li)
    return li


def create_student():
    ls_student = ["小亮","小明","李红","小丽","Jone","晓丹","小K","慕慕"]
    ls_stu_id = []
    for i in range(1000, 1008):
        ls_stu_id.append(i)
    #print(ls_stu_id)
    li = []
    count = len(ls_student) - 1
    for item in ls_stu_id:
        li.append(Student(ls_student[count], item))
        if count >= 0:
            count -= 1
        else:
            break

    #print(li)
    return(li)

if __name__ == "__main__":
    cour_li = course_to_teacher()
    stu_li = create_student()
    introduction("慕课学院 (1) 班学生信息")
    for stu in stu_li:
        print(stu)
    introduction("慕课学院 (1) 班选课结果")
    count = 0
    for cour in cour_li:
        print("Name: {0}, Selected: [{1}]".format(stu_li[count].name, cour))
        if count < len(stu_li):
            count+=1
        else:
            break

    print("----------------------------------------------------------------")
    t1 = Teacher("三上悠亚",1024,7789120322)
    c1 = Course("水管工","ACK-289")
    print(c1.binding(t1))