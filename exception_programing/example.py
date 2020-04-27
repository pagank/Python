

class Student(object):
    def __init__(self, name, stu_id, cour_info=None):
        self.stu_id = stu_id
        self.name = name
        self.__cour_info = cour_info

    def course_detail(self):
        return self.__cour_info

    def add_course(self,cour_info):
        self.__cour_info = cour_info

    def __str__(self):
        return "name: {0}, stu_id: {1}".format(self.name, self.stu_id)


class Teacher(object):
    def __init__(self, name, teacher_id, phone_num):
        self.teacher_id = teacher_id
        self.name = name
        self.phone_num = phone_num

    def __str__(self):
        return "name: {0}, teacher_id: {1}".format(self.name, self.teacher_id)



class Course(object):
    def __init__(self, cour_name, cour_id, teacher = None):
        self.cour_name = cour_name
        self.cour_id = cour_id
        self.teacher = teacher

    def binding(self, teacher):
        if teacher:
            self.teacher = teacher
            return {"课程名称": self.cour_name, "教师名称": self.teacher.name}
        else:
            return
