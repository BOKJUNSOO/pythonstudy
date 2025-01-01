#### 래퍼런스 카운팅
#a = "hello"
##print(sys.getrefcount(a))
#b = [a]
##print(sys.getrefcount(a))
#c = {"first":a}
##print(sys.getrefcount(a))
#
#### 
#def hi():
#    return "hello"
#k = hi()
#print(sys.getrefcount(k))
#
#def hi():
#    def inner():
#        return "hello"
#    inner()
#k = hi()
#print(sys.getrefcount(k))
#
#
#print("#####")
#
#c = "hihi"
#print(sys.getrefcount(c))
#import gc
#print(gc.get_count())