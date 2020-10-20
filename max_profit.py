### Max Profit ###

def MaxProfit(A):
    """ Given a list of A of stock prices, find the buy and sell times that max profit"""

    best,buy,sell = 0,0,-1
    n=len(A)
    for i in range(0,n):
        for j in range(i,n):
            profit = A[j] - A[i]
            if profit > best:
                best,buy,sell = profit, i, j
    return best, buy, sell

## Has complexity class: T(n) = theta(n^2)
A= [50,30,66,19,345,89]
print(MaxProfit(A))
