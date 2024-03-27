#!/usr/bin/env python3

import uuid
import redis
from typing import Union, List

class Cache:
    def __init__(self):
        # Store an instance of the Redis client as a private variable
        self._redis = redis.Redis()
        # Flush the instance using flushdb
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key
        key = str(uuid.uuid4())
        # Store the input data in Redis using the random key
        self._redis.set(key, data)
        # Return the key
        return key

# Example usage:
if __name__ == "__main__":
    cache = Cache()
    keys = []
    # Store data and collect keys
    inputs = [b"('first',)", b"('secont',)", b"('third',)"]
    for data in inputs:
        key = cache.store(data)
        keys.append(key)
    print("inputs:", inputs)
    print("outputs:", [cache._redis.get(key) for key in keys])
