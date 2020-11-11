from hashlib import md5, sha1, sha256
from pathlib import Path
from typing import Any

from OpenSSL import crypto

# for key generation
KEY_TYPE: Any = crypto.TYPE_RSA
KEY_BITS: int = 2048

# for hashing
HASH_ALGS = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256,
}

CHUNK_SIZE: int = 65536

# for demo
_CWD = Path(__file__).parent.absolute()
DATA_DIR = _CWD / 'data'  # my raw data (photos)
RES_DIR = _CWD / 'result'  # for my generated files
OTHER_BR_DIR = _CWD / 'other_brigade'  # for other brigade's stuff
