 
def hello_func():
  print('Hello Fuction')

hello_func()

def hello_func2():
  return 'Hello function.'

print(hello_func2())


def hello_func3(greeting):
  return '{} Funrtion.'.format(greeting)
print(hello_func3('Hi'))

def hello_func4(greeting, name = 'You'):
  return '{}, {}' .format(greeting, name)
print(hello_func4('Hi'))
print(hello_func4('Hi', name = 'Dave'))
print(hello_func4('Hi', 'Dave'))

# positional keywords argument, use * or ** since we don't know how many arguments there are
def student_info(*args, **kwargs):
  print(args)
  print(kwargs)

student_info('math','art', name='John', age=22)
print("---------------")

def student_info1(*args, **kwargs):
  print(args)
  print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info1(courses, info)
student_info1(*courses, **info)
print("---------------")

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
  # return true for leap
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
  if  not 1 <= month <= 12:
    return 'Invalid Month'
  
  if month == 2 and is_leap(year):
    return 29
  return month_days[month]

print(is_leap(2017))
print(days_in_month(2016, 2))
print("---------------")