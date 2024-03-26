#!/usr/bin/env python3
"""Module"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    sch = mongo_collection.find({"topics": topic})
    return list(sch)

