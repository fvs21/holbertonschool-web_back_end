#!/usr/bin/env python3
""" Module for using PyMongo """

def insert_school(mongo_collection, **kwargs):
    """ Inserts new doc in collection """

    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id