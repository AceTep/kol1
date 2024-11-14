t = int(input())

for _ in range(t):
    n = int(input())  
    s = input() 

    balance = 0
    min_balance = 0
    
    for char in s:
        if char == '(':
            balance += 1
        else:  
            balance -= 1
        
        min_balance = min(min_balance, balance)
    
    print(-min_balance)
