# 

# https://en.wikipedia.org/wiki/Euler%27s_totient_function
#print(str(28433*2**7830457+1)[-10:])
#print(pow(2, 7830457, mod=10**10)*28433+1)

from eulerlib import modpow

print(modpow(2, 7830457, 10**10)*28433+1)