def process_case(w, p):
    price = [ord(char) - ord('a') + 1 for char in w]
    
    total_price = sum(price)
    
    if total_price <= p:
        return w
    
    char_price_pairs = [(price[i], w[i]) for i in range(len(w))]
    
    char_price_pairs.sort(reverse=True, key=lambda x: x[0])
    
    remaining_price = total_price
    result = list(w)
    for i in range(len(char_price_pairs)):
        if remaining_price - char_price_pairs[i][0] >= p:
            remaining_price -= char_price_pairs[i][0]
            result[result.index(char_price_pairs[i][1])] = ''  
    
    return ''.join(result)

t = int(input()) 
for _ in range(t):
    w = input().strip() 
    p = int(input())  
    
    print(process_case(w, p))
