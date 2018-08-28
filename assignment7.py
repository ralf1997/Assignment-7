# Q.1 Create user defined dictionary

dict1 = {}
i = 'x'
while i != 'end':
    key = input('enter the key value for dictionary: ')
    value = input('enter the value for corresponding key: ')
    dict1[key] = value
    i = input('enter "end" to terminate input and print dictionary otherwise anything to continue')
print(dict1)


# Q.2: nested dictionary

records = {'Prince': {'Chemistry': 55, 'Physics': 88, 'English': 75}, 'Rana': {'Chemistry': 76, 'Physics': 65, 'English': 88}, 'Avi': {'Chemistry': 82, 'Physics': 70, 'English': 80}}
name = input("Enter the name: ")
for key in records:
    if name == key:
        print(key, records[key])
