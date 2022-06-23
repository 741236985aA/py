a,b = 0,1
#cishu = int(input(计算次数: ))
print("基础数值为'a=0,b=1'")

for i  in range(9):
    a,b = b,a + b
    print(f"{a+b}",end="   ")