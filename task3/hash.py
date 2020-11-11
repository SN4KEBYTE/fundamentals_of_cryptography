from task3.const import CHUNK_SIZE, HASH_ALGS
from task3.types import PathType


def file_hash(path: PathType, hash_alg: str = 'sha256') -> str:
    if hash_alg not in HASH_ALGS.keys():
        raise ValueError(f'Unknown hashing algorithm. Possible values are: {", ".join(HASH_ALGS.keys())}')

    hash_func = HASH_ALGS[hash_alg]()

    with open(path, 'rb') as f:
        while True:
            data = f.read(CHUNK_SIZE)

            if not data:
                break

            hash_func.update(data)

    return hash_func.hexdigest()
