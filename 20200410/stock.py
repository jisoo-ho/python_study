def cal_upper(price): #상한가 구해주는 함수
    increment = price * 0.3 
    upper_price = price + increment 
    return upper_price

def cal_lower(price): #하한가 구해주는 함수
    decrement = price * 0.3 
    lower_price = price - decrement 
    return lower_price 

author = "pystock"

if __name__ == "__main__":
    print(cal_upper(10000)) 
    print(cal_lower(10000)) 
    print(__name__)
