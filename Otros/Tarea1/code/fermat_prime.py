import random
 
# Funcion iterativa para calcular
# (a^n)%p en O(logy)
def power(a, n, p):
     
    # Inicializa
    res = 1
     
    # Actualiza 'a' si 'a' >= p
    a = a % p 
     
    while n > 0:
         
        # Si n es impar, multiplicar
        # 'a' con el resultado
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            # n debe ser par ahora.
            n = n // 2
             
    return res % p
     
# Si n es primo, siempre regresa true
# Si n es compuesto, regresa falso, con 
# alta probabilidad, un aumento en el valor de k
# aumenta la probabilidad de obtener una respuesta correcta.
def isPrime(n, k):
     
    # Casos limite
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
    # Try k 
    else:
        for i in range(k):
             
            # Toma un entero aleatorio
            # en [2..n-2]     
            # Sin contar los casos limite,
            # sabemos que n > 4
            a = random.randint(2, n - 2)
             
            # Pequeño teorema de Fermat
            if power(a, n - 1, n) != 1:
                return False
                 
    return True
             
# Driver code
k = 5


def func(n):
    x = (n*n)-(n)+41
    return x

def func2(n):
    x = 1 + (5)**(n) + (5)**(n+1) + (5)**(n+2) + (5)**(n+3)
    return x

for i in range(50):
    x = func(i)
    if(isPrime(x,k)):
        print(i,x, True)
    
        print(i,x, False)



for i in range(20):
    x = func2(i)
    if(isPrime(x,k)):
        print(i,x, True)
    else:
        print(i,x, False)

primos = []
for i in range(1,15):
    if(isPrime(i,k)):
        primos.append(i)
    
print(primos)

n = len(primos)
result = 1
for x in primos:
    result = result * x
result += 1
print(result, isPrime(result,k))
