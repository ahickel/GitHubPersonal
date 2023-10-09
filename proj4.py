def computepay(rate,hours):
    print("Pay", rate*hours)

def computepay_exth():
    overtime_rate = sh
    return print("Pay", overtime_rate)

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
rtes = float(rte)
if h > 40:
    eh = h-40
    ehw = 1.5 * rtes * eh
    sh = (40 * rtes)+ ehw
    #sh = seperate hours with regular hours total pay, eh = extra hours, ehw = extra hours worked
    #rtes= float rate h = float hours
else: rate = 1.0 * rtes
if h <= 40:
    computepay(rtes,h)
else: computepay_exth()
