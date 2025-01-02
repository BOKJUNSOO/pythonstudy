from pprint import pprint

### local namespace - fuction
def outer():
    def inner():
        pass
    print("enclosed scope에서 inner 함수에 할당 된 주소:",inner)
    return inner
A = outer()
print("호출된 outer로 리턴된 inner의 주소:",A)

def outer():
    name="BOKJUNSOO"
    name2="BOKHYUNSOO"
    print("name의 주소 :",hex(id(name)).upper())
    print("name2의주소 : ",hex(id(name2)).upper())
    def inner():
        nonlocal name, name2
        name = name + " is me"
        name2 = name2 + " my brother"
    return inner
closure = outer()
print(f"closure 객체 생성시 : {closure.__closure__[0].cell_contents}이 저장되어 있는 주소 {closure.__closure__[0]}")
print(f"closure 객체 생성시 : {closure.__closure__[1].cell_contents}가 저장되어 있는 주소 {closure.__closure__[1]}")
closure()
print(f"closure 객체로 호출시 : {closure.__closure__[0].cell_contents}가 저장되어 있는 주소 {closure.__closure__[0]}")
print(f"closure 객체로 호출시 : {closure.__closure__[1].cell_contents}가 저장되어 있는 주소 {closure.__closure__[1]}")

import gc

def outer():
    name = "BOKJUNSOO"
    def inner():
        nonlocal name
        name += " is me"
        return name
    return inner

A = outer()
print(A)

address = id(A)  # 객체의 메모리 주소

# 모든 객체를 순회하면서 주소와 매칭
for obj in gc.get_objects():
    if id(obj) == address:
        print("Found object at address:", obj)
        break
else:
    print("Object not found.")