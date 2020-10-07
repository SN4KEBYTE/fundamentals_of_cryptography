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


def are_mutually_simple(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def multiplicative_inverse():
    # TODO
    pass
