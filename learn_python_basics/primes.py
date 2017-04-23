noprimes = [j for i in range(2,8) for j in range(i*2,50,i)]
primes = [l for l in range(2,50) if l not in noprimes]
print primes