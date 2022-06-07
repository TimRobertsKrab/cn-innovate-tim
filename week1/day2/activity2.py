import random as r
cast = ["Bill Murray","Dan Aykroyd",
"Sigourney Weaver","Harold Ramis",
"Rick Moranis","Annie Potts",
"William Atherton","Ernie Hudson",
"David Margulies"]

unsorted_cast = cast.copy()

is_ghost_buster = [True,True,False,True,False,False,False,True]

def show_cast_members():
    print(cast)
    while True:
        try:
            num1=int(input(f"Enter an integer between 1 and {len(cast)}: ")) 
        except:
            print("Invalid input. Try again")
        else:
            if num1 > len(cast) or num1 < 0:
                print(f"Enter an integer between 0 and {len(cast)} (inclusive)")
                continue
            break

    
    if num1 != len(cast):
        while True:
            try:
                num2=int(input(f"Enter an integer between {num1} and {len(cast)}: ")) 
            except:
                print("Invalid input. Try again")
            else:
                if num2 > len(cast) or num2 < num1:
                    print(f"Enter an integer between {num1} and {len(cast)} (inclusive)")
                    continue
                break
    else:
        num2 = len(cast)

    cast.sort()
    print(cast[num1-1:num2])

def gb_game():
    while True:
        i = r.randint(0,len(cast)-1)
        print(f"Does {unsorted_cast[i]} play a Ghostbuster? ")
        answer = input("Y or N? ")
        if (answer == "N" and is_ghost_buster[i]) or (answer == "Y" and not is_ghost_buster[i]):
            print("YOU LOSE")
            break

    
show_cast_members()  
gb_game()





