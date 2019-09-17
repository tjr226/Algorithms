# recursive fibonnaci

# gives the fibonnaci 
def fibonnaci_recursive(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci_recursive(n - 1) + fibonnaci_recursive(n - 2)

# print(fibonnaci_recursive(10))
# print(fibonnaci_recursive(11))
# print(fibonnaci_recursive(25))

cache = {0: 0, 1: 1}

def fibonnaci_guided_project(n):
    print(cache)

    if n < 0:
        print("ERROR")
        return 0
    elif n in cache:
        return cache[n]
    else:
        result = fibonnaci_guided_project(n - 1) + fibonnaci_guided_project(n - 2)
        cache[n] = result
        return result

print(fibonnaci_guided_project(2))

print(fibonnaci_guided_project(4))





def fibonnaci_dynamic_tjr(n):
    if n < 1: 
        print("ERROR")
        return 0

    fib_array = [1, 1]

    while len(fib_array) < n:
        fib_array.append(fib_array[-1] + fib_array[-2])
        
    return fib_array[-1]    
    

 