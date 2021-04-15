import hashlib
import json
from os import urandom
from time import time


def cycle_cipher(times: int, payload: bytes):
    for i in range(times):
        payload = hashlib.sha512(payload).digest()
    return payload


def json_serialization(json_payload: str):
    ...


if __name__ == "__main__":
    start = time()
    a = cycle_cipher(1000000, bytes(urandom(256)))
    end = time()
    print(end - start)
    print(a)
