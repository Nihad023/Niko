n = int(input())
say = 0
arr = []
while n > 0:
    if say % 2 != 0 and say % 3 != 0 and say % 5 != 0:
        arr.append(say)
        n -= 1 
    say += 1

print(*arr)

#'geleceyin proqramcisi sen ol!'

