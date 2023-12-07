#!/usr/bin/env python3

import unittest

import time

import random

import phnaw.hnapi as hnapi
import phnadb.db as hndb

import hn




def main():
    hndb.create_database()
    # hn.cache_all_items()
    hn.cache_posts('top')
    #hn.cache_posts('best')
    # hn.cache_all_items()
#end

if __name__ == "__main__":
    # unittest.main()
    main()
#end