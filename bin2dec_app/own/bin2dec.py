def bin2dec(num):
    num_len = len(num)
    num_pw = int(2 ** (num_len - 1))
    dec = 0
    
    for x in num:
        if x == '1':
           dec += num_pw
        num_pw //= 2
    return dec
    

# num = input("Enter a binary number: ")    
# bin2dec(num)    