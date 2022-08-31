
# List...changing list will change list that = to list being changed
courses = ['History', 'Math', 'Physics', 'CS']
courses_2 = ['Art', 'Education']

print(courses)
print(len(courses))
print(courses[2])
print(courses[-1])
print(courses[0:2])

courses_1 = courses
courses_1.insert(0, 'Art')
print(courses_1)

courses_1.insert(0, 'Language')
print(courses_1)
courses_1.insert(0, courses_2)
print(courses_1)
courses_1.remove(courses_2)

courses_1.extend(courses_2)
print(courses_1)

popped = courses_1.pop()
print(courses_1)
print(popped)

courses_1.append(courses_2)
print(courses_1)
courses_1.pop()
courses_1.pop()
print(courses_1)
courses_1.reverse()
print(courses_1)

# sort w/o changing original list
sorted_courses = sorted(courses_1)
print(sorted_courses)
print(courses_1)


# sort asc, will change the list
courses_1.sort() 
print(courses_1)

# sort desc
courses_1.sort(reverse = True)
print(courses_1)

# find index
print(courses_1.index('Art'))

# check if exist in list
print('Art' in courses_1)

# for loop printing each elelment of courses_1
for item in courses_1:
  print(item)

for index, course in enumerate(courses_1):
  print(index, course)
for index, course in enumerate(courses_1, start = 1):
  print(index, course)



nums = [1, 5, 2, 4, 3]
print(max(nums))
print(sum(nums))


# turn list to string
course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)


# Tuples...immutable. cannot be assigned 
tuple_1 = ('History', 'Math', 'Physics', 'CS')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Sets...don't care about orders. throw away duplicates
cs_courses = {'History', 'Math', 'Physics', 'CS'}
print(cs_courses)
cs_courses = {'History', 'Math', 'Physics', 'CS', 'Math'}
print(cs_courses)

print('Math' in cs_courses) # can be done in list/tuples but is optimed for sets
art_courses = {'History', 'Math', 'Art', 'Design'}
# check if values are common
print(cs_courses.intersection(art_courses))
# check difference, in cs not in art
print(cs_courses.difference(art_courses))
# combine sets
print(cs_courses.union(art_courses))

# empty_list
# empty_list = []
# empty_list = list()

# Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# Empty Tuples
# empty_set = {} # This in incorrect. It's an empty dictionary
# empty_set = set()


