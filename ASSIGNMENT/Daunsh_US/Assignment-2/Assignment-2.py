import random

for i in range (30,90):

    H= random.randint(65,75)
    T= random.randint(35,40)
    if (H>=75 or T>=40):
        print("!!! High Values !!!  Humidity : ",H," Temparature : ",T)
    else:
        print("Low Values !  Humidity : ",H," Temparature : ",T)
    print("*************************************************")