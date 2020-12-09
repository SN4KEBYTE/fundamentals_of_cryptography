from hashlib import md5, sha1, sha256

from typing import Any, Dict

HASH_ALGS: Dict[str, Any] = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256,
}
