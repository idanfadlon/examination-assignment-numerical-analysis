

def fixed_difference(x_array):
    # pram n: len of x values array
    # pram h: the difference between x1-x0
    # pram htemp: current difference of x[i]-x[i-1]
    # return: h
    # if the value of htemp different form the h value return -1  that  meaning the method cannot be used
    n = len(x_array) - 1
    h = x_array[1] - x_array[0]
    for i in range(1, n):
        htemp = x_array[i + 1] - x_array[i]
        if h != htemp:
            return -1
    return h


def delta(deg, i, y_array):
    # pram y_array: y values array
    # pram deg: the degree of the current delta y0
    # pram i: the current iteration
    # return: delta y0 degrees values

    if deg+i>=len(y_array):
        return None

    if deg == 1 and i + 1 < len(y_array):
        return y_array[i + 1] - y_array[i]

    return delta(deg - 1, i + 1, y_array) - delta(deg - 1, i, y_array)


def factorial(n):
    # pram n: the number that we want his factorial value
    # pram fact: the value of n!
    # return: fact
    fact = 1
    if n == 0 or n == 1:
        return fact
    for i in range(2, n + 1):
        fact *= i
    return fact


def calc_p(p, iter):
    # pram p: calculate p value
    # pram iter: the current iteration by the method used
    # return: the value of p
    if iter == 1:
        return p
    return calc_p(p - 1, iter - 1) * p


def divided_difference_forward_calc(y_array, p):
    # pram sum: the value of y function at xf value by the method
    # return: sum
    sum = 0
    print("y(x)=",end="")
    for i in range(len(y_array)):
        if i == 0:
            print(y_array[i],end="")
            sum += y_array[i]
        else:
            iter_res=(calc_p(p, i) * delta(i, 0, y_array)) / factorial(i)
            print("%+f"%iter_res,end="")
            sum += iter_res
    print('\n')
    return sum


def main():
    # pram x_array: array of x values
    # pram y_array: array of y values
    # pram xf: the value of x that we want calculate with the method
    # pram h: the difference between x1-x0
    # pram p: calculate value of (xf - x0) / h
    # Printing the sub calculations and the value of y function at xf value

    print("how many points would you like to insert?")
    numberofpoint = int(input())
    x_array = [0]*numberofpoint
    y_array = [0]*numberofpoint
    for i in range(numberofpoint):
        print("x{0}= ".format(i), end="")
        x_array[i]=int(input())
        print("y{0}= ".format(i), end="")
        y_array[i] = int(input())
    print("insert an x value which you want to calculate")
    print("x= ", end="")
    xf = int(input())
    print("points valus:")

    for i in range(len(x_array)):
        print("(x{0}={1},y{0}={2})".format(i,x_array[i],y_array[i]),end=""),
        if i !=len(x_array)-1:
            print(",",end="")
    print("\n")


    h = fixed_difference(x_array)
    if h == -1:
        print("can't calculate this")
    else:
        p = (xf - x_array[0]) / h
        print("h = x1-x0 = {0}\np = (xf - x0) / h = {1}\n ".format(h, p))
        for i in range(1,len(y_array)):
            print("delte y0 on degrre {0}  = {1}".format(i , delta(i, 0, y_array)))
        print("\ny(x={0}) = {1}".format(xf, divided_difference_forward_calc(y_array, p)))


main()
