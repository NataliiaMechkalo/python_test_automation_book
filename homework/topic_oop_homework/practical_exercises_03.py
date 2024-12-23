# Home task 3

class BaseClass1:
    def test(self):
        print("Method from BaseClass1")

    def common_method(self):
        print("Common method from BaseClass1")


class BaseClass2:
    def test(self):
        print("Method from BaseClass2")

    def common_method(self):
        print("Common method from BaseClass2")


class DerivedClass(BaseClass1, BaseClass2):
    pass

obj = DerivedClass()

obj.test()
obj.common_method()

print(DerivedClass.__mro__)