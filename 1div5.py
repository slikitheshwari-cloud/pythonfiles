def div5(n):
    if n[-1] in '05':
        return "div5"
    else:
        return "notdiv5"

n=input('enter n value: ')
print(div5(n))
        
