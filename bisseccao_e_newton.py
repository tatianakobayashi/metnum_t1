# Bissecção
def bissecao(f, a, b, parada, N):  
    i = 1  
    p = 0
    while (i <= N):  
        fa = f(a)  

        p = (a + b)/2  
        fp = f(p) 

        fb = f(b)

        if (fa == 0):
            return a
        elif (fp == 0 or abs(b - a) <= parada):
            return p
        elif (fb == 0):
            return b

        if (fa > 0 and fp < 0) or (fa < 0 and fp < 0):
            b = p
        elif (fb > 0 and fp < 0) or (fb < 0 and fp < 0):
            a = p
        i += 1  
    return p

# Newton
def newton(f, f_x0, N, E):  
    x = [0 for i in range(N)]
    x[0] = x0
    for k in range(0, N):
        x[k + 1] = x[k] - (f(x[k])/f_(x[k]))
        if(abs(x[k+1]-x[k])/abs(x[k+1]) <= E and abs(f(x[k+1])) <= E):
            return x[k+1]
