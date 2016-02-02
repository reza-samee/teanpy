# in the name of ALLAH

class Result():
  def isOk(self): raise NotImplementedError("Result::isOk")
  def isErr(self): raise NotImplementedError("Result::isErr")
  def get(self): raise NotImplementedError("Result::get")
  def getError(self): raise NotImplementedError("Result::getError")
  # maybeOk() or 'something-else'
  def maybeOk(self): raise NotImplementedError("Result::maybeOk")
  def maybeErr(self): raise NotImplementedError("Result::maybeErr")
  def flatmap(self,f):
    if self.isOk(): return f(self.get())
    else: return self
  def map(self,f): return self.flatmap(lambda i: Ok(f(i)))
  def asList(self):
    if self.isOk() : return [self.get()]
    else : return []
  def debug(self):
    print(self)
    return self
  
    

class Ok(Result):
  val=None  
  def __init__(self,val):
    self.val = val
  def isOk(self): return True
  def isIter(self): return False 
  def isErr(self): return False
  def get(self): return self.val
  def getError(self): raise BaseException("{}; try Ok::get not getError!".format(self))
  def maybeOk(self): self.get()
  def maybeErr(self): None
  def __str__(self): return "Ok({}):Result".format(self.get())

# http://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable

class Err(Result):
  val=None  
  def __init__(self,val):
    self.val = val
  def isOk(self): return False
  def isErr(self): return True
  def get(self): raise BaseException("{}; try Error::getError not get!".format(self))
  def getError(self): return self.val
  def maybeOk(self): None
  def maybeErr(self): self.getError()
  def __str__(self): return "Err({}):Result".format(self.getError())
