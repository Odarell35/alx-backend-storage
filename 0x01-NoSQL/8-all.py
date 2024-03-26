#!/usr/bin/env python3 
"""list all docs"""


def list_all(mongo_collection):
	"""list all"""
	doc = mongo_collection.find()
	doc_list = list(doc)
	return doc_list
