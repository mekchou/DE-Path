
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])
print(student['age'])
print(student.get('name'))
# will show errer if using student['phone'] because it doesn't exist
print(student.get('phone')) 
print(student.get('phone', 'Not Found')) 
student['phone'] = '1234567'
print(student.get('phone', 'Not Found')) 
student['name'] = 'Amy'
print(student.get('name'))
print(student)

student.update({'name': 'Jane', 'age': 26, 'phone': 7654321})
print(student)

del student['age']
print(student)

student['age'] = 26
print(student)
age = student.pop('age')
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
  print(key)
for key, value in student.items():
  print(key, value)