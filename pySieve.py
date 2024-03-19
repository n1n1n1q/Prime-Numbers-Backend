"""
...
"""
def eratosthenes_sieve_py(n: int):
    """
    Sieve 
    """
    is_prime=[True for i in range(n+1)]
    i: int = 2
    while i*i<=n:
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False
        i+=1
    return [i for i,boo in enumerate(is_prime) if boo]
