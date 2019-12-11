# gradient_descent.py
# Gradient descent is a first-order iterative optimization 
# algorithm for finding the minimum of a function f(x).

# Maximum number of iterations
n = 10000

# Start value for the algorithm (x_0)
x_k = 6

# Step length
# Here, it's a static number for simple use. For a more adaptive 
# solution the Armijo conditoin or linesearch (backtracking) can 
# be used. 
alpha = 0.01

# Desired precision of result
epsilon = 0.00001

# Derivative of f(x)
def df(x):
    return 4 * x**3 - 9 * x**2

# Calculate minmum of f(x) with gradient descent algorithm
for i in range(n):
    x = x_k
    x_k = x - alpha * df(x)

    step = x_k - x
    if abs(step) <= epsilon:
        break

# Print result
print("x_min = ", x_k)

