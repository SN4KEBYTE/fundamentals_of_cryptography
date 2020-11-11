from task3.const import DATA_DIR, OTHER_BR_DIR, RES_DIR, HASH_ALGS
from task3.hash import file_hash
from task3.key import dump_public_key, dump_private_key, generate_key_pair
from task3.signature import sign_file, verify_sign

if __name__ == '__main__':
    # generate keys
    pkey = generate_key_pair()

    dump_public_key(pkey, RES_DIR / 'public_key.cer')
    dump_private_key(pkey, RES_DIR / 'private_key.pem')

    # sign file using private key
    sign_file(DATA_DIR / 'br4_1.jpg', RES_DIR / 'private_key.pem', RES_DIR / 'sign.txt')

    # calculate SHA256 hash and dump it to file
    my_hash = file_hash(DATA_DIR / 'br4_1.jpg', 'sha256')

    with open(RES_DIR / 'hash.txt', 'w') as f:
        f.write(my_hash)

    # read other brigade's hash
    with open(OTHER_BR_DIR / 'hashed.txt', 'r') as f:
        other_br_hash = f.read()

    # verify sign
    for photo in ['brigada8.jpg', 'brigada8_1.jpg']:
        # try to verify sign
        if verify_sign(OTHER_BR_DIR / 'cert.cer', OTHER_BR_DIR / 'signed.txt', OTHER_BR_DIR / photo):
            print(f'Sign is valid for {photo} file')

            # check all hash algorithms
            for h in HASH_ALGS.keys():
                ph_hash = file_hash(OTHER_BR_DIR / photo, h)

                print(f'Correct {h} hash for {photo}' if other_br_hash == ph_hash else f'Wrong {h} hash for {photo}')
        else:
            print(f'Sign is invalid for {photo} file')

        print()
