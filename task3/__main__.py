from task3.const import DATA_DIR, OTHER_BR_DIR, RES_DIR
from task3.hash import file_hash
from task3.key import dump_public_key, dump_private_key, generate_key_pair
from task3.signature import sign_file, verify_sign

if __name__ == '__main__':
    # generate necessary files
    pkey = generate_key_pair()

    dump_public_key(pkey, RES_DIR / 'public_key.cer')
    dump_private_key(pkey, RES_DIR / 'private_key.pem')

    sign_file(DATA_DIR / 'photo1.jpeg', RES_DIR / 'private_key.pem', RES_DIR / 'sign')

    my_hash = file_hash(DATA_DIR / 'photo1.jpeg', 'sha256')

    with open(RES_DIR / 'hash.txt') as f:
        f.write(my_hash)

    # verify sign
    if verify_sign(OTHER_BR_DIR / 'cert.cer', OTHER_BR_DIR / 'sign', OTHER_BR_DIR / 'photo.jpeg'):
        print('Sign is valid')
    else:
        print('Sign is invalid')

    # check hash
    ph_hash = file_hash(OTHER_BR_DIR / 'photo.jpeg')

    with open(OTHER_BR_DIR / 'hash.txt') as f:
        other_br_hash = f.read()

    if other_br_hash == ph_hash:
        print('Correct hash')
    else:
        print('Incorrect hash')
