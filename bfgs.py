# bfgs.py
# 1-D BFGS optimization algorithm
from time import time
from math import sqrt

# Function f(x) 
def f(x):
    return -5.0 * x + 10.0 * x**2

# Derevative of f(x)
def df(x):
    return -5.0 + 2.0 * 10.0 * x

# Line search algorithm
def line_search(df, x_0, alpha, epsilon):
    x_k = x_0
    while sqrt(df(x_k)**2) > epsilon:
        p_k = -df(x_k)
        x_k = x_k + alpha * p_k
        #print("Line search df = ", df(x_k))
    return x_k

# Initialize parameters
alpha_ls = 0.000001
epsilon = 1e-10
x_0 = -5.0
B_0 = 1.0

t1 = time ()
for k in range(100):

    B_k = B_0
    x_k = x_0

    # Step 1.: 
    p_k = -1.0 * df(x_k) / B_k

    # Step 2.:
    alpha_k = line_search(df, (x_k + alpha_ls * p_k), alpha_ls, epsilon)

    # Step 3.:
    s_k = alpha_k * p_k
    x_k_prime = x_k + s_k

    # Step 4.
    y_k = df(x_k_prime) - df(x_k)

    # Step 5.:
    B_k = B_k + (y_k * y_k) / (y_k * s_k) - (B_k * s_k * s_k * B_k) / (s_k * B_k * s_k)
    x_k = x_k_prime

    #print("x_k = ", x_k)
    print("k = ", k, " x_min = ", x_k, " df = ", df(x_k), " a = ", alpha_k)

    B_0 = B_k
    x_0 = x_k

t2 = time()
print("Minimum found at x_min = ", x_k, " with f(x_min) = ", f(x_k))
print("Runtime: ", t2 - t1)
