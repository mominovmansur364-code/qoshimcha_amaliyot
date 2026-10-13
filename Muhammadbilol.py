def qoshish(son):
    if(son==0):
        return 0

    return son + qoshish(son-1)

def factorial(son):
    if(son==0):
        return 1
    return son*factorial(son-1)


def raqamlar_yigindisi(son):
    if(son==0):
        return 0
    return son%10+raqamlar_yigindisi(son//10)

def raqamlar_soni(son):
    if(son<10):
        return 1
    return 1+raqamlar_soni(son//10)

son=int(input("Sonni kiriting: "))
print(f"1 dan {son} gacha bolgan sonlar yigindisi: {qoshish(son)} ")
print(f"{son} ning factoriali: {factorial(son)} ")
print(f"{son} ning raqamlar yigindisi: {raqamlar_yigindisi(son)} ")
print(f"{son} ning raqamlar soni: {raqamlar_soni(son)} ")
    