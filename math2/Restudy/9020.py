## 골드바흐의 추측

# n 이하의 숫자들 중 소수 찾기
def is_prime(num):
    primes = []
    if num < 2:
        return primes
    for i in range(2, num+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return primes


# is_prime 중 합이 n인 소수 찾기
def hap_is_n(x):
    li = is_prime(x)
    idx = max([i for i in range(len(li)) if li[i] <= x/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            if li[i] + li[j] == n:
                return [li[i], li[j]]

t = int(input())

for _ in range(t):
    n = int(input())
    print(" ".join(map(str, hap_is_n(n))))
    
        
