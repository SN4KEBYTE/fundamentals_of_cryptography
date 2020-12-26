from task2.rsa.rsa import RSA

if __name__ == '__main__':
    print('<1> - key generation demo')
    print('<2> - encryption demo')
    print('<3> - decryption demo')

    opt = input()

    while opt not in ['1', '2', '3']:
        opt = input()

    if opt == '1':
        print('DEMO 1. Key generation.')

        p, q = [int(x) for x in input('Enter p and q: ').split()]
        rsa = RSA(p, q)

        print(f'Public key: {rsa.public_key}')
        print(f'Private key: {rsa.private_key}')
    elif opt == '2':
        print('DEMO 2. Encryption.')

        n, e = [int(x) for x in input('Enter n and e: ').split()]
        rsa = RSA(3, 5)  # using some dummy values
        rsa.n = n
        rsa.e = e

        m = input('Enter raw message (int or some text): ')

        try:
            m = int(m)
        except ValueError:
            pass

        print(rsa.encrypt(m))
    else:
        print('DEMO 3. Decryption.')

        n, d = [int(x) for x in input('Enter n and d: ').split()]
        rsa = RSA(3, 5)  # using some dummy values
        rsa.n = n
        rsa.d = d

        m = input('Enter encrypted message (single integers or integer separated by space): ')

        try:
            m = int(m)
        except ValueError:
            m = list(int(x) for x in m.split())

        print(rsa.decrypt(m))
