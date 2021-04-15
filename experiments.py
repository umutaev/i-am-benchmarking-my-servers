import hashlib
import json
import random
import string
from os import urandom
from time import time
from sys import argv


def cycle_cipher(times: int, payload: bytes):
    for i in range(times):
        payload = hashlib.sha512(payload).digest()
    return payload


def serialization(json_payload: str):
    parsed_json = json.loads(json_payload)
    if not type(parsed_json) == dict:
        raise TypeError("This test only works with dict jsons.")
    return " ".join(parsed_json.keys())


if __name__ == "__main__":
    test_number = 0
    if len(argv) >= 3 and argv[1] == '--test' and argv[2].isdigit():
        test_number = int(argv[2])
    elif len(argv) >= 2 and argv[1] == '--help':
        print(f"Usage {argv[0]} --test <test number>:\n"
              f"0 - sha256 test - 1.000.000\n"
              f"1 - json serialization test - about 14.000.000 symbols\n")
        exit(0)
    if test_number == 0:
        random_bytes = bytes(urandom(256))
        start = time()
        a = cycle_cipher(1000000, random_bytes)
        end = time()
        print("Time: ", end - start, "s", sep="")
    elif test_number == 1:
        json_data = json.dumps({''.join(random.choices(string.ascii_letters, k=128)): random.randint(0, 1000000)
                                for i in range(100000)})
        start = time()
        a = serialization(json_data)
        end = time()
        print("Time: ", end - start, "s", sep="")
    else:
        print(f"{argv[0]} --help")
