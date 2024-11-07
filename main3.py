#Activity3
def divide(dividend,divisor):
    sign=(-1 if ((dividend<0)^(divisor<0))else 1);
    dividend=abs(dividend)
    divisor=abs(divisor)
    quotientnum=0
    tempnum=0
    for i in range(31,-1,-1):
        if (tempnum+(divisor<<i)<=dividend):
            tempnum+=divisor<<i
            quotientnum|=1<<i
    if sign==-1:
        quotientnum=-quotientnum
    return quotientnum
a=int(input("Enter number: "))
b=int(input("Enter number: "))
print(divide(a,b))