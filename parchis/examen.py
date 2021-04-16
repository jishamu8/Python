def p(x, y):
    n = len(x)
    for i in range (n):
        if x[i] == y:
            return i
    
    return -1


def main():
    p(1,2)

main()           
