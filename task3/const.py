from hashlib import md5, sha1, sha256
from pathlib import Path
from typing import Any, Dict

from OpenSSL import crypto

from task3.types import PathType

# for key generation
KEY_TYPE: Any = crypto.TYPE_RSA
KEY_BITS: int = 2048

# for hashing
HASH_ALGS: Dict[str, Any] = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256,
}

CHUNK_SIZE: int = 65536

# for demo
_CWD: PathType = Path(__file__).parent.absolute()
DATA_DIR: PathType = _CWD / 'data'  # my raw data (photos)
RES_DIR: PathType = _CWD / 'result'  # for my generated files
OTHER_BR_DIR: PathType = _CWD / 'other_brigade'  # for other brigade's stuff
