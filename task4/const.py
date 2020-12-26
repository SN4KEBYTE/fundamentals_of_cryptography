from hashlib import md5, sha1, sha256
from pathlib import Path

from typing import Any, Dict

from task4.types import PathType

HASH_ALGS: Dict[str, Any] = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256,
}

_CWD: PathType = Path(__file__).parent.absolute()
IMAGE_DIR: PathType = _CWD / 'images'
ENC_DIR: PathType = _CWD / 'encrypted'
DEC_DIR: PathType = _CWD / 'decrypted'
