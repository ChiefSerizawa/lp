class A:
    def __init__(self, name):
        self.name = name

    def disp(self, to_display):
        print(to_display)

class B(A):
    def __init__(self, name, c_list):
        super(B, self).__init__(name)
        self.c_list = c_list

class C:
    def __init__(self):
        pass


