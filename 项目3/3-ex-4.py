for x in range(2,51):
    is_prime=True
    for j in range(2,x-1):
        if x%j==0:
            is_prime=False
            continue
    if is_prime:
        print(x)    
        