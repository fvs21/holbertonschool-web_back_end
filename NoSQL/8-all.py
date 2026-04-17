#!/usr/bin/env python3
""" Module for using PyMongo """

def list_all(mongo_collection):
    """
        List all docs
    """
    documents = []
    if mongo_collection is not None:
        cursor = mongo_collection.find()
        for doc in cursor:
            documents.append(doc)
    return documents
