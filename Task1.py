
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
N = int(input('введите номер дня недели - '))

if N == 6 or N == 7:
    print('это выходной')
else:
    print('рабочий день')

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('введите коорлинату Х - '))
y = int(input('введите координату Y - '))
if x>0 and y>0 :
    print('точка находится в первой четверти')
elif x<0 and y>0 :
    print('точка находится во второй четверти')
elif x>0 and y<0 :
    print('точка находится в третьй четверти')
elif x<0 and y<0 :
    print('точка находится в четвертой четверти')
elif x == 0 and y != 0 :
    print('точка находится но оси Y')
elif x != 0 and y == 0 :
    print('точка находится но оси X')
elif x == 0 and y == 0 :
    print('точка находится в начале систем5ы координат')


#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('введите номер четверти - '))

if n==1 :
    print('x>0 y>0')
elif n==2 :
    print('x<0 y>0')
elif n==3 :
    print('x>0 y<0')
elif n==4 :
    print('x<0 y<0')
else:
    print('ошибка. это не номер четверти')


#ННапишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('введите координату X точки А - '))
y1 = int(input('введите координату Y точки А - '))
x2 = int(input('введите координату X точки B - '))
y2 = int(input('введите координату Y точки B - '))
len = (((x2-x1)**2) + ((y2-y1)**2))**(0.5)
print('расстояние между точками = ',  round(len,2))

#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for i in True, False:
    x = i
    for j in True, False:
        y = j
        for l in True, False:
            z = l
            print('Значения предикат X Y Z: ',x, y, z)
            answer = ( not( x or y or z)) == ( (not x)and (not y)and (not z))
            print('истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ', answer)
            print('')
