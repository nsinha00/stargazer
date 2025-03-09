"""
This file contains utilities that (differently from those in utils.py) are only
meant for internal use.
"""
from itertools import groupby

def _extract_feature(obj, feature):
    """
    Just return obj.feature if present and None otherwise.
    """
    try:
        return getattr(obj, feature)
    except AttributeError:
        return None


# Unneeded as soon as we drop support for Python 3.8 - Python 3.9 has d1 | d2:
def _merge_dicts(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

def _find_duplicates(iterable):
    unique = set()
    dups = set()
    for el in iterable:
        if el in unique:
            dups.add(el)
        unique.add(el)

    return dups

def _group_items(lst):
    '''
    Group consecutive items in a list, returning a shorter list of tuples with items and their consecutive appearances.
    '''
    return [(key, len(list(group))) for key, group in groupby(lst)]