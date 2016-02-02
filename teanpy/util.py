# in the name of ALLAH

from result import *
from functools import wraps
from collections import Iterable

def forIter(f):
  
  # return lambda itr : [f(i) for i in itr] # unnamed function ( fn.__name__ => <lambda> )
  # def x(itr): return map(f,itr) # return a map... ?!
  
  # https://docs.python.org/2/library/functools.html#functools.update_wrapper
  @wraps(f)
  def tmp(itr) : return [f(i) for i in itr]
  return tmp

def toPair(l,first=0,second=1): return l[first],l[second]

@forIter
def toPairAll(l): return toPair(l)

def bin2str(i): return i.decode().strip()


def __collect(buf,item):
  if isinstance(item,Iterable): [__collect(buf,i) for i in item]
  else: buf.append(item)

def unsafe_flat(*args):
  buf = []
  __collect(buf,args)
  return buf

# =============================================

import subprocess as sp

def run(args):
  proc = sp.Popen(
      args
    , stderr = sp.PIPE
    , stdout = sp.PIPE
  )
  rc = proc.wait()
  if rc == 0 : return Ok(proc.stdout.readlines())
  else : return Err(proc.stderr.readlines())

# =============================================

from math import floor

def asLong(str): return long(float(str)+1)  
