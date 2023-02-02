import re

num = 0
x = "Hi there my age is 22 years\nHello My Name is Hashem and im 15 years old"
y = re.findall('([0-9]+) years', x)
for value in range(len(y)):
    num += float(y[value])
    print(y[value])
print(num)
# ///////////////////////////////////////////////////////////////////////////////////////////

x= "From : hashem1999.saqqa@gmail.com \nFrom : ahmed-emad2003@whatever.net"
y = re.findall('\s[A-Za-z0-9.]+@.+?\s', x)
print(y)
print(x)
# ///////////////////////////////////////////////////////////////////////////////////////////

x = "today is the sunday 12-2-2022 \nand yesterday was 11-2-2022"
y = re.findall('[0-9-]+', x)
print(y)
# ///////////////////////////////////////////////////////////////////////////////////////////

x = "i live in Gaza \nand my friend parents live in Jordan"
y = re.findall('[A-Z].+', x)
print(y)
# ///////////////////////////////////////////////////////////////////////////////////////////

x = "user: Ahmed ALrayyes \nSalary: 1000$ \nAge: 26 \nuser: Hashem Alsaqqa \nSalary: 1500$ \nAge: 22 \nuser: emad morad \nSalary: 2500$ \nAge: 37"
y = re.findall('user: (.+?)\s', x)
z = re.findall('user: .+?\s(.+?)\s', x)
print(y)
print(z)
# ///////////////////////////////////////////////////////////////////////////////////////////