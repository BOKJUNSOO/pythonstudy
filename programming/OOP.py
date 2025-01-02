### dir 함수와 객체의의 속성
name="bokjunsoo"

def test():
    pass

### 함수 객체체의 속성성
test.name = name
print(test.name)
print(dir(test))

### 함수 속성을 정의하는 방법
def test():
    pass
test.hello = "hello"

def introduce(name):
    print(name)
introduce.name = "BOKJUNSOO"
print(dir(introduce))

### self 는 인스턴스 객체 자신을 가르킨다
class Person:
    def __init__(self,name:str):
        print(self)
        self.name = name
this_is_instance = Person("BOKJUNSOO")
print(this_is_instance)
print(this_is_instance.name)

### class 객체의 속성에 introduce가 포함되어 있다.
print(dir(Person))
### __init__ 메서드는 인스턴스가 생성되어야 멤버변수로 참여한다
print(dir(this_is_instance))

### OOP의 특징중 은닉화가 있다.
class Person:
    def __init__(self,name:str):
        self.name = name
    def introduce(self):
        print(self.name)
this_is_instance = Person("BOKJUNSOO")
this_is_instance.introduce()

### 객체가 생성되고 나서 속성에 접근되는 문제를 막아야함.
this_is_instance.name = "BOKHYUNSOO"
this_is_instance.introduce()

### 캡슐화
class Person:
    def __init__(self,name):
        self.__name = name
    def introduce(self):
        print(self.__name)
this_is_instance = Person("BOKJUNSOO")

### 해당 class 객체속성에 직접 접근하지 못한다.
print(dir(this_is_instance))
this_is_instance.__name = "BOKHYUNSOO"
this_is_instance.introduce()
