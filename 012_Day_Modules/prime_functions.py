## Trying to get a prime numbers upto a number

def is_prime(x):
    # for a number to be prime, it should have only two factors, one and itself,
    # no factors between two and one less the number, hence:
    if len([ i for i in range(2,x) if x % i == 0]) == 0:
        Prime = 'Prime'
    else:
        Prime = 'Not Prime'
    return Prime





def all_primes_upto(x):
    # using the already declared primes functions
    Primes = [i for i in range(x+1) if is_prime(i)== 'Prime']
    return Primes





