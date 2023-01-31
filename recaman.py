import math as ma
def recaman(max_terms):
    exist = set()
    seq=list()
    n = 0 
    a = 0
    while n < max_terms:
        diff=a-n
        if diff > 0 and diff not in exist:
            a = diff
        else:
            a = a + n
        exist.add(a)
        seq.append(a)
        n += 1
    return seq

def qsolver(a,b,c):
    return -b/2-((b*b-4*a*c)**0.5)/2, -b/2+((b*b-4*a*c)**0.5)/2

def des_sorting(a:list):
  return sorted(a)[::-1]

def intersec(l1,l2):
  s1=set(l1)
  s2=set(l2)
  l3=list(s1.intersection(s2))
  return l3

def factors(val):
    return [(i, int(val / i)) for i in range(1, int(val**0.5)+1) if val % i == 0]
  
def divisibles(n,step):
  l=list(range(0,n,step))
  return l

def checkPalindrome(s):
    s="".join(s.split())
    s=s.lower()
    return s == s[::-1]

def find_max_occ(s):
    return max([(i, s.count(i)) for i in set(s.lower())], key=lambda x: x[1])

def number_primes(n):
  data = {i:True for i in range(2,n)}
  init = 2
  primes = []
  for i in range(2,int(n**(0.5))+1):
    if data[i]:
      for j in [i**2+x*i for x in range(n) if i**2+x*i<n]:
        data[j]=False
  for i in data.keys():
    if data[i]:
      primes.append(i)
  return primes
