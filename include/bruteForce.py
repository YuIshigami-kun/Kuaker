from itertools import chain, product

lChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sim = ['\\', '!', '|', '#', '$', '%', '~', '&', '/', '(', ')', '=', '?', '\'', '+', '^', '[', ']', '*', '{', '}', ':', ';', '-', '_']

def genDict(l, u, n, s, length, path = "./pass.txt"):
    with open(path, 'w') as file:
        r = []
        global count
        count = 0
        global stop 
        stop= False

        if(l == 'y'): r.extend(lChars)
        if(u == 'y'): r.extend(uChars)
        if(n == 'y'): r.extend(nums)
        if(s == 'y'): r.extend(sim)

        for candidate in chain.from_iterable(product(r, repeat=i) for i in range(1, length + 1)):
            if(stop == True):
                return
            
            file.write("".join(candidate) + '\n')
            count += 1


def getCount():
    return count

def stopProcess():
    global stop
    stop = True
