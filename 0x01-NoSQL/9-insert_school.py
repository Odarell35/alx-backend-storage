#!/usr/bin/env python3
"""module"""


def insert_school(mongo_collection, **kwargs):
    """ïnsert new doc"""
    addition = mongo_collection.insert_one(kwargs).inserted_id
    return addition
