with open('student_details.txt', 'r') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

f = open('D:\\images.jpeg', 'rb')
f2 = open('img.jpeg', 'wb')
for file in f:
    f2.write(file)
