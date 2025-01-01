import sys
from pprint import pprint

### closure
def outer():
    name = "hi"
    name2 = "good"
    def inner():
        nonlocal name,name2
        name += "world"
        name2 += "good bye"
        print(hex(id(name)))
        print(hex(id(name2)))
    # GC 이전 주소 확인
    # print(inner)
    return inner

check_clo = outer()

### inner 함수의 주소와 동일
#print(check_clo)

### str만 재할당되고, closure 객체는 같은 주소를 포인팅한다.
check_clo()
pprint(check_clo.__closure__)
check_clo()
pprint(check_clo.__closure__)

### 클로져 원소 확인
print(check_clo.__closure__[0].cell_contents)
print(check_clo.__closure__[1].cell_contents)

