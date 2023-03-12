import random
def quicksort(s):
   if len(s) <= 1:
       return s
   else:
       q = random.choice(s)
   l_s = [n for n in s if n < q]
 
   e_s = [q] * s.count(q)
   b_s = [n for n in s if n > q]
   return quicksort(l_s) + e_s + quicksort(b_s)