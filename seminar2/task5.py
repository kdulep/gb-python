
#Реализуйте алгоритм перемешивания списка.
import random

def shuffle(data):
    for i in range(0,len(data)):
        j=random.randint(0,i)
        tmp=data[j]
        data[j]=data[i]
        data[i]=tmp
    return data
    
n = int(input("Введите n: "))

data = random.sample(range(-n, n+1), n*2+1)
print("Исходный список:", data)
#random.shuffle(data)
data=shuffle(data)
print("Измененный список:", data)
