# GCD of 2 Numbers :-
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("The First Number: "))
b=int(input("The Second Number: "))
print("The GCD of 2 numbers is: ",gcd(a,b))

"""
Input : 48,18
Output : 6

# DRY RUN :-

(48,18)
   ↓
(18,12)
   ↓
(12,6)
   ↓
(6,0) → answer = 6

🔁 Step 1
gcd(48, 18)
b != 0 → go to else
→ gcd(18, 48 % 18)
→ gcd(18, 12)
🔁 Step 2
gcd(18, 12)
b != 0
→ gcd(12, 18 % 12)
→ gcd(12, 6)
🔁 Step 3
gcd(12, 6)
b != 0
→ gcd(6, 12 % 6)
→ gcd(6, 0)
🛑 Step 4 (Base Case Hit)
gcd(6, 0)
b == 0 → return 6
"""

