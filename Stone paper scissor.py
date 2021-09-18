import random
def generate_random():
    sys=random.randint(1,3)
    if sys==1:
        comp='st'
    elif sys==2:
        comp='p'
    else:
        comp='sc'
    # print(comp)
    
    return comp


def game(sys,user):
    if sys==user:
        return None
    if user=='sc':
        if sys=='st':
            return False
        else:
            return True
    if user=='st':
        if sys=='p':
            return False
        else:
            return True
    if user=='p':
        if sys=='sc':
            return False
        else:
            return True
            
    
play='y'
print("choices:\n1.stone(st) 2.paper(p) 3.scissor(sc)")
i=0
while play=='y':
    user=input("your turn:")
    i+=1
    sys=generate_random()
    print(f"The computer chose {sys} ",end="")
    res=game(sys,user)
    if res==None:
        print("Its a Tie!")
    elif res:
        print("You win")
    else:
        print("You lost!")
    if i==5:
        print("Press y is you wanna play again!")
        play=input()
        i=0

    
    
