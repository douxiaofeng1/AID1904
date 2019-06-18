# class A():
#     v = 100
#     def __init__(self):
#         self.v = 200
# class B(A):
#     v = 300
#     def __init__(self):
#
#         super().__init__()
#         self.v = 400
# a = B()
# print(a.v)
# class A:
#     def new(self):
#         print(self.__init__())
#     pass
#
# a=A()
# a.__init__()
# a.new()
class A():
    def b(self):
        print("aaaa")
a=A()
A.b(a)