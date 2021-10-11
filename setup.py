from distutils.core import setup
import glob
import os
import re
import sqlite3
from pathlib import Path
from random import randrange
from time import sleep


import py2exe



setup(zipfile=None, 
      options={'py2exe':{"bundle_files":1}},
      windows=["hackescript.py"])
