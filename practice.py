import random

def main():
    practice_1()

def practice_1():
    intt = 082
    print(str(intt))
def practice_2():
    l = []
    l2 = [2,4,5,6,10,12]

    set1 = set(l)
    set2 = set(l2)

    set3 = set1.union(set2)

    print(set3)

    l3 = [12, 1, 24, 5, 15]

    set4 = set(l3)
    set5 = set3.union(set4)
    print(set5)

    

if __name__ == '__main__':
    main()