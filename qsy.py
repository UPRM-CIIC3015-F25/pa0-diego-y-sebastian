def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(5))

def sqrt(number):
    if number < 0:
        print("error")
        return -1

    n = number
    x0 = n / 2
    xi = x0
    for i in range(10):
        xi = 0.5 * (xi + n / xi)
    return xi

print(sqrt(5))


def is_palindrome(x):
    t = x
    r = 0
    while t > 0:
        r = r * 10 + (t % 10)
        t //= 10
    if r == x:
        return True
    else:
        return False


print(is_palindrome(121))
True
True
print(is_palindrome(123))
False
False
print(is_palindrome(10))
False
False
print(is_palindrome(9))
True
True

1) Sum 1…n
def sum_to_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

2) Sum of even numbers 1…n
def sum_evens(n):
    s = 0
    for i in range(2, n + 1, 2):
        s += i
    return s

3) Product 1…n (factorial)
def factorial(number):
    r = 1
    for i in range(1, number + 1):
        r *= i
    return r

4) Count digits of a positive int
def count_digits(x):
    if x == 0:
        return 1
    c = 0
    while x > 0:
        c += 1
        x //= 10
    return c

5) Sum of digits
def sum_digits(x):
    s = 0
    while x > 0:
        s += (x % 10)
        x //= 10
    return s

6) Reverse integer
def reverse_int(x):
    r = 0
    while x > 0:
        r = r*10 + (x % 10)
        x //= 10
    return r

7) Palindrome integer (explicit True/False at end)
def is_palindrome(x):
    t = x
    r = 0
    while t > 0:
        r = r*10 + (t % 10)
        t //= 10
    if r == x:
        return True
    else:
        return False

8) Integer square root via Newton (10 iters, your lab style)
def sqrt(number):
    if number < 0:
        print("error")
        return -1
    n = number
    x0 = n / 2
    xi = x0
    for i in range(10):
        xi = 0.5 * (xi + n / xi)
    return xi

9) Power a^b (b ≥ 0)
def power(a, b):
    r = 1
    for _ in range(b):
        r *= a
    return r

10) Check prime (n ≥ 2)
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


If they expect a small optimization: loop to int(n**0.5)+1, but the simple full loop is safer for your lab.

11) Count primes up to n
def count_primes(n):
    c = 0
    for x in range(2, n + 1):
        ok = True
        for d in range(2, x):
            if x % d == 0:
                ok = False
                break
        if ok:
            c += 1
    return c

12) GCD (Euclid but written with a loop)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

13) Fibonacci n-th (iterative, n starts at 0)
def fib(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(1, n):
        a, b = b, a + b
    return b

14) Count vowels in a string (basic for-loop)
def count_vowels(s):
    v = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            v += 1
    return v

15) String reverse using loop (no slicing)
def reverse_str(s):
    t = ""
    for ch in s:
        t = ch + t
    return t

16) Count occurrences of a target in a list
def count_occ(a, target):
    c = 0
    for x in a:
        if x == target:
            c += 1
    return c

17) Max in list (no built-ins)
def max_in_list(a):
    m = a[0]
    for x in a[1:]:
        if x > m:
            m = x
    return m

18) Min positive divisor (>1) or say “prime”
def min_divisor(n):
    for d in range(2, n):
        if n % d == 0:
            return d
    return -1  # means none found (prime)

19) Multiplication table 1…n (basic nested loop)
def mult_table(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row += str(i*j) + " "
        print(row.strip())

20) Average of n numbers from input (if they force input())
def avg_n(n):
    s = 0.0
    for _ in range(n):
        x = float(input())
        s += x
    return s / n


If your lab auto-tests, they might not want input() inside functions. Only use this if they explicitly say “read from input”.

21) Count how many numbers are > 0 from input
def count_positive(n):
    c = 0
    for _ in range(n):
        x = float(input())
        if x > 0:
            c += 1
    return c

22) Factor count (how many divisors)
def count_divisors(n):
    c = 0
    for d in range(1, n + 1):
        if n % d == 0:
            c += 1
    return c

23) Perfect number check
def is_perfect(n):
    s = 0
    for d in range(1, n):
        if n % d == 0:
            s += d
    if s == n:
        return True
    else:
        return False

24) Armstrong (narcissistic) 3-digit
def is_armstrong_3(x):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    s = a**3 + b**3 + c**3
    if s == x:
        return True
    else:
        return False

25) Approximate e^x with first k terms (optional if they cover series)
def exp_series(x, k):
    term = 1.0
    s = 1.0
    for i in range(1, k):
        term = term * (x / i)
        s += term
    return s

