courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],

]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

durations_dict = {}

for id, lists in enumerate(courses_list):

    key = lists['duration']
    durations_dict[key] = durations_dict.get(key, []) + [id]
    
durations_dict = dict(sorted(durations_dict.items()))

for k, v in durations_dict.items():
    if len(v) == 1: print (f'{courses[v[0]]} - {k} месяцев')
    else:
        print (f'{courses[v[0]]} - {k} месяцев')
        print(f'{courses[v[1]]} - {k} месяцев')