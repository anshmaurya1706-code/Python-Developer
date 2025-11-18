def lcm_numnbers(a,b):
    if a>b:
        greater=a
    else:
        greater=b   
    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("LCM of", num1, "and", num2, "is:", lcm_numnbers(num1, num2))