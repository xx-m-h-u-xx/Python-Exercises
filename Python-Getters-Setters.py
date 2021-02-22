class MyClass:
    def __init__(self, lst):
        self.my_list = lst

    @property
    def my_list(self):  # getter
        return self._my_list

    @my_list.setter
    def my_list(self, value):  # setter
        self._my_list = value
        
 
 ''' Different approach '''
class MyProperty:
    def __set__(self, instance, value):
          instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
          if instance is None:
              return self
          
          return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
          self.name = name

class MyClass:
    my_list = MyProperty()
    def __init__(self, lst):
        my_list = lst 