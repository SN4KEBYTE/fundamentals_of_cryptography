from task2.rsa.rsa import RSA

if __name__ == '__main__':
    # p, q = [int(x) for x in input().split()]
    p = 3557
    q = 2579
    rsa = RSA(p, q)

    print(f'Public key: {rsa.public_key}')
    print(f'Private key: {rsa.private_key}')

    msg_int = 123456
    msg_int_enc = rsa.encrypt(msg_int)
    print(f'Encrypted int: {msg_int_enc}')
    msg_int = rsa.decrypt(msg_int_enc)
    print(f'Decrypted int: {msg_int}')

    msg_str = 'Hello, world!'
    msg_str_enc = rsa.encrypt(msg_str)
    print(f'Encrypted str: {msg_str_enc}')
    msg_str = rsa.decrypt(msg_str_enc)
    print(f'Decrypted str: {msg_str}')
