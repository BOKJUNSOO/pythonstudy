### 가까운 name space (스택)에 있는 객체를 참조한다.
### print 함수는 로컬스택에 존재하지 않으므로 built-in scope 를 참조한다

name="bok june soo"

def func():
    name = "BOKJUNSOO"
    ### local scope 참조
    print(name)
func()

### global scope 참조
# print(name) 

def func():
    ### global scope 참조
    print(name)
#func()


### global scope
name = "BOK SI YEON"
def outer():
    ### enclosed scope
    name = "BOK HYUN SOO"
    print(name)
    def inner():
        ### local scope
        name = "BOK HYE YEON"
        print(name)
    inner()
outer()

### closure
def outer():
    name="BOKJUNSOO"
    print("outer:",name)
    def inner():
        name = "JUNSOOBOK"
        print("inner",name)
    return inner
A = outer()
A()
print()
### 통제 밖의 scope에 대해서 쓰기는 굉장히 제한적이다.
def outer():
    name="BOKJUNSOO"
    print("outer:",name)
    def inner():
        nonlocal name # 해당줄이 없으면 name 을 local에서 찾아서 오류
        name = name + "is me" # name에 값을 할당하는 것이므로
        print("inner",name)
    inner()
outer()

### 
def outer():
    name="BOKJUNSOO"
    print("outer:",name)
    def inner():
        nonlocal name
        name = name + " is me"
        print("inner:",name)
    return inner
A = outer()
B = outer()
A()
A()

B()