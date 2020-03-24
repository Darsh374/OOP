[![Build Status](https://travis-ci.com/Darsh374/OOP.svg?branch=master)](https://travis-ci.com/Darsh374/OOP)

#Object Oriented Programming

#Encapsulation
In the program below we use the Calculator class in order to call functions within that class. We can use the test_calculator file in order to instantiate the object in the Calculator class. From here we create a Calculator object with uses random numbers that we pass to get a result.
    
    def Sum(self, a, b):
        self.Result = Addition.sum(a,b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a,b)
        return self.Result

#Abstraction
For abstraction when we run code, or have a user input, the only thing we see is what we input and the output. However what we don't see is how the function manipulates our input in order to produce the correct output. When using the addition and subtraction class you can see how to input is manipulated inorder to produce an output. All of this is imported into the calculator file.

    class Addition:
        @staticmethod
        def sum(augend, addend):
            return augend + addend

#Inheritance
Inheritance is the ability to have objects that have the same or inherit the traits of the class it is inside. For example the childcare calculator has all the traits of the regular calculator inside with other features.

    class ChildCalculator(Calculator):

#Polymorphism
ChildCalculator class inherits everything from the parent Calculator class. The child class can do things differently from the parent class. For example in the child class you can take a list and add or subtract, but in the parent class you can't.

    class ChildCalculator(Calculator):
        def sumList(self, valueList):
            self.Result = AddList.sumLists(valueList)
            return self.Result
       


