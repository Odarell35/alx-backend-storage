#!/usr/bin/env python3
"""Writing strings to Redis"""

import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
        """docs"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """doc"""
            k = method.__qualname__
            self._redis.incr(k)
            return method(self, *args, **kwargs)

        return wrapper

class Cache():
    """create class cache"""

    def __init__(self) -> None:
        """init method"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data:Union[str, bytes, int, float]) -> str:
        """generate a random key """
        ran_key = str(uuid.uuid4())
        self._redis.set(ran_key, data)

        return ran_key

    def get(self, key: str, fn: Optional[Callable[[bytes], any]] = None) -> any:
        """create a get method that take a key string argument"""
        data = self._redis.get(key)

        if data is None:
            return None
        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        """docs"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[str]:
        """docs"""
        return self.get(key, fn=int)
