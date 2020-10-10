def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i: int = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def are_mutually_prime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def multiplicative_inverse(a: int, mod: int) -> int:
    a0, a1 = a, mod
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while a1 != 0:
        q = a0 // a1
        a0, a1 = a1, a0 - a1 * q
        x0, x1 = x1, x0 - x1 * q
        y0, y1 = y1, y0 - y1 * q

    return x0 % mod


def fast_pow_mod(a: int, n: int, mod: int) -> int:
    if n == 0:
        return 1

    if n % 2 == 1:
        return a * fast_pow_mod(a, n - 1, mod) % mod

    d: int = fast_pow_mod(a, n // 2, mod)

    return d * d % mod
