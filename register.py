
class Person:
    def __init__(self, firstName, lastName, age) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self) -> str:
        return f'name : {self.firstName} {self.lastName}'

class Teacher(Person):
    """
    to create teacher object who has name and course study
    """
    def __init__(self, firstName, lastName, age, course_study) -> None:
        super().__init__(firstName, lastName, age)
        self.course_study = course_study
    def __str__(self) -> str:
        return f'{super().__str__()}\ncouser study : {self.course_study}'


class Course:
    """
    To create course which student can choose
    """
    def __init__(self, name , department) -> None:
        self.name = name
        self.department = department
        self.course_teachers = {}

    # this method use when we want add a teachers for courses
    def add_teacher(self, teacher):
        teacher_list = [teacher]
        if self.name == teacher.course_study:
            if teacher.course_study not in self.course_teachers.keys():
                self.course_teachers.update({self.name:teacher_list})
            else:
                self.course_teachers[teacher.course_study].extend(teacher_list)
        else:
            print('there is no course which correspond to teacher\'s study path ')

    def count(self, study_path):
        teacher_count = 0
        for i in range(len(self.course_teachers[study_path])):
            teacher_count += 1
        return f'{teacher_count} are present this {study_path}'
        
    def __str__(self) -> str:
        return self.course_teachers
                
    

electeronic = Course('electeronic', 'power')
django = Course('django', 'IT')
ghahri = Teacher('mojtaba', 'ghahri', 36, 'electeronic')
ghahria = Teacher('mojtaba', 'ghahri', 36, 'electeronic')
mahdi = Teacher('mahdi', 'raki',25,'django')
maha = Teacher('maha', 'mah', 36, 'electeronic')
django.add_teacher(mahdi)
electeronic.add_teacher(ghahria)
electeronic.add_teacher(maha)
art = Course('art', 'cinema')






for item in django.course_teachers['django']:
    print(item)

print(django.course_teachers)
electeronic.count('electeronic')
print(electeronic.count('electeronic'))


