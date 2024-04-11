import random

# Сделал дополнительно алгоритмом "быстрой сортировки"


class Student:

    def __init__(self, name='', group_numb='', grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.group_numb = group_numb
        self.average_grades = 0
        self.grades = grades


class HoarSort:

    def support_func(self, lst):
        less_buf = [i_dict for i_dict in lst if list(i_dict.values())[0] < list(lst[-1].values())[0]]
        equal_buf = [i_dict for i_dict in lst if list(i_dict.values())[0] == list(lst[-1].values())[0]]
        larger_buf = [i_dict for i_dict in lst if list(i_dict.values())[0] > list(lst[-1].values())[0]]
        return less_buf, equal_buf, larger_buf

    def sorting_process(self, lst, reverse=False):
        if len(lst) <= 1:
            return lst
        less_buf, equal_buf, larger_buf = self.support_func(lst)
        if reverse:
            return self.sorting_process(larger_buf, reverse=True) + equal_buf + self.sorting_process(less_buf,
                                                                                                     reverse=True)
        else:
            return self.sorting_process(less_buf) + equal_buf + self.sorting_process(larger_buf)

    def sorting(self, objects_list, reverse=False):
        numb_dict = dict()
        lst_of_dicts = []
        for i_object in objects_list:
            numb_dict[i_object] = i_object.average_grades
            lst_of_dicts.append({i_object: numb_dict[i_object]})
        sorted_objects = self.sorting_process(lst_of_dicts, reverse)
        return sorted_objects


students = [Student() for student_numb in range(0, 10)]

for count, i_student in enumerate(students):
    i_student.name = f'Student{count + 1}'
    i_student.group_numb = random.randint(1, 10)
    i_student.grades = [random.randint(3, 5) for _ in range(0, 5)]
    i_student.average_grades = sum(i_student.grades) / len(i_student.grades)

# hoar_sort = HoarSort()
# sorted_students = hoar_sort.sorting(objects_list=students, reverse=True)
#
# for i_pair in sorted_students:
#     for i_student in i_pair.keys():
#         print(f'Имя и фамилия студента: {i_student.name}')
#         print(f'Номер группы студента: {i_student.group_numb}-я группа')
#         print(f'Список оценок студента: {i_student.grades}')
#         print(f'{i_student.average_grades}')
#         print()

students.sort(key=lambda x: x.average_grades, reverse=True)


for i_student in students:
    print(f'Имя и фамилия студента: {i_student.name}')
    print(f'Номер группы студента: {i_student.group_numb}-я группа')
    print(f'Список оценок студента: {i_student.grades}')
    print(f'Средняя оценка студента: {i_student.average_grades}')
    print()
