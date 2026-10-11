# Sean Beckford
def writish(A):
    B = []
    for i in range(0, len(A)):
        # Check if next index is number, if so then repeat string that many times
        if i + 1 < len(A) and isinstance(A[i + 1], int):
            for _ in range(0, A[i + 1]): # Use '_' since we don't need a variable
                B.append(A[i])
        elif not isinstance(A[i], int):
            B.append(A[i])

    return B

def modsetsize(N):
    X_N = {1}
    x_i = 1
    while True:
        x_i = (x_i * x_i + x_i + 1) % N

        # Check if repeated
        if x_i in X_N:
            return len(X_N)

        X_N.add(x_i)

def convert(amt, curFrom, curTo):
    # Define our currency rates (Dictionary)
    Currency = {
        "Dollars US" : 1.00,
        "Euros" :  0.9018,
        "Pounds" : 0.7614,
        "Dollars Canadian" : 1.3156
    }

    return amt * Currency[curTo] / Currency[curFrom]
