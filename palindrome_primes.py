import math

def primes_below(limit):
  valid_primes = set(range(limit))
  max_factor = math.ceil(math.sqrt(limit))
  i = 2
  while i < max_factor:
    k = i*2
    while k < limit:
      valid_primes.discard(k)
      k += i
    i += 1
    while i not in valid_primes:
      i += 1

  return valid_primes

def is_palindrome(number):
  return str(number) == str(number)[::-1]

#print(primes_below(1000))
print(list(filter(is_palindrome, primes_below(100000))))
