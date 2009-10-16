# -*- coding: utf-8 -*-
import bsddb

DB_NAME = 'taotao.data'

#----------------------------------------------------------------------
def add(key,value):
    """"""
    db = bsddb.hashopen(DB_NAME, "c")
    db[key] = value
    db.close()    
    
    
#----------------------------------------------------------------------
def get(key):
    """"""
    db = bsddb.hashopen(DB_NAME, "c")
    value = db[key]
    db.close()  
    return value
    
    
if __name__ == "__main__":
    
    add("aa","123")
    print get("aa")