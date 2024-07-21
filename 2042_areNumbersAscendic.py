def areNumbersAscendic(s: str):
    s_list = s.split() 
    digit_list = [int(i) for i in s_list if i.isdigit()]
    for i in  range(1, len(digit_list)):
        if digit_list[i] <= digit_list[i-1]:
            return False
    return True
            
            
            
print(areNumbersAscendic("hello world 5 x 5"))            
print(areNumbersAscendic("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))            
print(areNumbersAscendic("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))            

    
