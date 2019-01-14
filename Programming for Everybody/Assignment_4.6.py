def computepay(h,r):
    if h> 40:
        return 40*r+(h-40)*r*1.5
    else:
        return h*r

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
p = computepay(h,r)
print(p)
