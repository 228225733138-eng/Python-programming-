class Demo:
    school = "KPRIT"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

    def instance_method(self):
        print("Name:", self.name)

    @classmethod
    def class_method(cls):
        print("School:", cls.school)

    @staticmethod
    def static_method():
        print("Static method called")

obj = Demo("Ravi")
obj.instance_method()
Demo.class_method()
Demo.static_method()
