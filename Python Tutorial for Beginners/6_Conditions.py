
if True:
  print('condition was True')
if False:
  print('condition was True')


language = 'Python'

if language == 'Python':
  print('Language is Python')
elif language == 'Java':
  print('Language is Java')
else:
  print('No Match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
  print('Admin Page')
else:
  print('Bad Creds')

if not logged_in:
  print('Please Log In')
else:
  print('Welcome')

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(id(a))
print(id(b))
# is is used to check if it's the same id in memory
print(a is b)
b = a
print(a is b)
print(a == b)

