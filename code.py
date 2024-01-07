import math as m  # as zorgt ervoor dat ik enkel m hoef te typen ipv math
def _hello(name: str):
    # het volgende kan ook met "Hello " + name, of met f"Hello {name}"
    print("Hello {0}".format(name))

def number():
    # een nummer is een int:
    i = 5
    print(type(i))
    # of een float:
    j = 7.90
    print(type(j))
    # ook kunnen we operaties doen, zoals:
    plus = 5 + 4
    minus = 5 - 4
    keer = 5 * 8
    gedeeld_door = 5 / 4
    print(type(gedeeld_door))
    # automatisch een float, tenzij we aangeven dat het een int moet zijn, zoals:
    gedeeld_door = int(gedeeld_door)
    print(type(plus))
    print(type(minus))
    print(type(keer))
    print(type(gedeeld_door))
    # voor andere operaties bestaat math, zoals sqrt en pow
    # deze moet wel, aan het begin, geimporteerd worden.
    print(m.pow(1, 2))
    return m.sqrt(36)

# lists, tuple, dict, set
# tuple, niet veranderbaar
# list, veranderbaar
# dict, veranderbaar
# set:
# unordered, unchangeable*, and unindexed.
# wel mogelijk om nieuwe dingen toe te voegen
def containers():
    l = [5, 3, 5]
    t = (0, 8, 6, 3)
    d = {1: "a", 2: "b"}
    s = {4, 3}
    # voeg item toe aan lijst
    l.append(1)
    print(l)
    # index van tuple
    print(t[2])
    # voeg key en value toe aan dict
    d[0] = ""
    # overwrite oude key
    d[1] = ""
    # kleine loop, geeft randomness van set weer
    for i in range(0, 3):
        print(i, s)


def loops():
    # there are two types of loops: while and for.
    i = 0
    while True:
        print("Hi")
        i += 1
        if(i == 10):
            # stops the loop early, otherwise would loop indefinitely.
            break
    # can also be done like so
    j = 0
    while j <= 10:
        j += 1
        print("Hello!")
    # for-loops, meanwhile, tend to loop over something, like a list!
    l = ["a", "b", "c"]
    for letter in l:
        print(letter)


def conditionals():
    # conditionals are things like if and else and elif, but also while loops!
    # if their condition is true, like in the case of
    j = 0
    if j <= 10:
        j += 1
    # the bit of code written in the condition will be used.
    # likewise, we can use elif to check for other conditions, given the original 'if' is false.
    # else is used if none of the prior conditions are met - it is not necessary if a return is used in each of the 'if' or 'elif' statements, however.
    i = 100
    if i == 10:
        print("Hello, this won't print!")
        return
    elif i == 100:
        print("This will print!")
        return
    else:
        print("This is the actual else!")
    print("This is *technically* an else as well!")


def main():
    # given a parameter doesn't have a default value, like our _hello() function, we have to give a parameter along.
    # this could be an input, by using the following (commented) code
    # name = input()
    # _hello(name)
    _hello("Roald")
    # removing brackets on a function doesn't run the function, it instead gives the location in memory - this happens if the function is printed, not otherwise
    print(number())  # correct
    print(number)  # incorrect
    containers()
    loops()
    conditionals()


if __name__ == "__main__":
    main()