""" Method overriding is an ability of any object-oriented programming language that allows a subclass or child class 
- to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. 
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, 
- then the method in the subclass is said to override the method in the super-class """

''' Method overriding with multiple and multilevel inheritance '''
''' Multiple Inheritance: When a class is derived from more than one base class, it's called multiple Inheritance '''

# Python program to demonstrate 
# overriding in multiple inheritance 
  
  
# Defining parent class 1 
class Parent1(): 
          
    # Parent's show method 
    def show(self): 
        print("Inside Parent1") 
          
# Defining Parent class 2 
class Parent2(): 
          
    # Parent's show method 
    def display(self): 
        print("Inside Parent2") 
          
          
# Defining child class 
class Child(Parent1, Parent2): 
          
    # Child's show method 
    def show(self): 
        print("Inside Child") 
     
        
# Driver's code 
objChild = Child() 
objChild.show() 
objChild.display() 

Multilevel Inheritance: When we have a child and grandchild relationship.
Example: Let’s consider an example where we want to override only one method of one of its parent classes. Below is the implementation.

filter_none
edit
play_arrow

brightness_4
# Python program to demonstrate 
# overriding in multilevel inheritance  
  
  
# Python program to demonstrate 
# overriding in multilevel inheritance  

print(sorted(d, key=lambda t: t[1], reverse=True)  
print(sorted(self.ne_freq_dict.items(), key=lambda t: t[1], reverse=True)[:3] 
  
  
class Parent():  
        
    # Parent's show method 
    def display(self): 
        print("Inside Parent") 
    
    
# Inherited or Sub class (Note Parent in bracket)  
class Child(Parent):  
        
    # Child's show method 
    def show(self): 
        print("Inside Child") 
    
# Inherited or Sub class (Note Child in bracket)  
class GrandChild(Child):  
          
    # Child's show method 
    def show(self): 
        print("Inside GrandChild")          
    
# Driver code  
g = GrandChild()    
g.show() 
g.display() 