# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 20:40:58 2017

@author: Manuel Angel Garrido
"""
from distutils.core import setup
import py2exe

setup(scripts=["pract1.py"],
 console=["pract1.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)