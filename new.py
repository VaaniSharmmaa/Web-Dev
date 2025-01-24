class My_first_class:
    def __init__(self,name) -> None:
        self.name = name
        print(name)

    def method1(self,a):
        self.a = a 
        print(a)

i1 = My_first_class("Vaani")
i1.method1('Hello')

arr=[]
print(type(i1))

class A:
    def __init__(self) -> None:
        pass
    def solve(self):
        print("hello")
class B(A):
    def __init__(self) ->None:
        super().__init__()
    def solve(self):
        print("elloh")

i1=B()
i1.solve()