# Задаем пятизначное число

a = input("Введите пятизначное число: ")

s = (((float(a[3]) ** float(a[4])) * float(a[2])) / (float(a[0]) - float(a[1])))

print (s)

