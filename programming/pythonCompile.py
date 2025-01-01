import dis
### 스택에 값이 저장되는 변수들
#a = 1
#b = "bok"
#c = True
#
### 스택에 주소가 저장되는 변수들
#a = [1,2,3,4,5,6]
#b = {"Name":"bjs","AGE":"28"}
#def function_():
#    print("hello_world")

###
#a = 1
#b = [5,6,7,8]

a= 10
b= 30
c=[1,2,3,4]
def func1():
    a = 10
    b = [1,2,3]
    print(a)
    print(b)
print("test function1:", sep='\t')
dis.dis(func1)

def func2():
    print(a)
    print(b)
print("test function2:", sep='\t')
dis.dis(func2) 

# 호출시 에러
def error():
    print(a)
    print(b)
    a = 30
    b = [1,2,3]
print("error function: ", sep='\t')
dis.dis(error)

def func3():
    # 함수 내부에서 전역스택을 참조할 수 있다.
    global a,b,k
    print(a)
    print(b)

    d = a
    k = 1
    # string은 스택에 저장된 변수
    b = b[::-1]

    # 스택을 바꾸는게 아니므로 global 키워드가 필요 없다.
    c.extend([5,6,7,8])
print("test function3 with global keyword:", sep = '\t')
dis.dis(func3)