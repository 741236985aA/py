year = int(input('enter a year:'))

if year % 4 == 0 or year % 400 == 0 :
    print(f"{year} is runyear")
elif year % 4 == 1 or year % 100 == 0:
 print(f"{year} is pingyear")
else:
    print(f"{year} is pingyear")