#coding:utf-8
'''
Created on 2009-5-26

@author: wjt
'''
from distutils.core import setup
import py2exe      
import urllib
import urllib2
import string
import time
import md5
import re
import types
import logging
import simplejson
from PyQt4 import QtCore, QtGui
from taotao_ui import Ui_MainWindow
import dbutils as db


includes = ["encodings", "encodings.*",'PyQt4','sip','decimal']    
#要包含的其它库文件

options = {"py2exe":
        {"compressed": 1, #压缩
         #"optimize": 2,
         #"ascii": 1,
         "includes":includes,
         "bundle_files": 1 #所有文件打包成一个exe文件 }
        }
    }

setup(options=options,
      zipfile=None,
      windows=[{"script": "taotao.py", "icon_resources": [(1, "icon.ico")]}]
      )
