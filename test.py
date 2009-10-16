# -*- coding: utf-8 -*-
import urllib
import urllib2
import string
import time
import md5
import re
import types
import logging
import sip
from xml.dom import minidom


from taotao import IeThread

ie = IeThread()
ie.setUrl("google.com")
ie.start()
ie.wait()
