# Muhammadaziz

n=int(input("nechta son kerak: "))
sonlar=list(map(int, input().split()[:n]))

natija=list(map(lambda son: son**3,sonlar))
natija1=list(filter(lambda son: son%2==0,sonlar))
natija2=list(filter(lambda son: son>=50,sonlar))
natija3=list(map(abs,sonlar))
print("sonlar kubi",natija)
print("juft sonlar",natija1)
print("50kdan kata sonlar",natija2)
print("musfatga aylantirish",natija3)