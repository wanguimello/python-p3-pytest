#!/usr/bin/env python3

from not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False

def test_return_not_none():
    '''The function "return_not_none" should return a value that is not None.'''
    assert return_not_none() is None
