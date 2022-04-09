class Calculator():
    def __init__(self,a=0,b=0):
        """
           this is the constructor function
           which is containing the variables

           >>> cal = Calculator(a=10,b=5)
        """
        self.a = a
        self.b = b

    def add(self):
        """
        This code is for addition

        >>> add = cal.add()


        Returns:
            _type_: _description_
        """
        return self.a + self.b

    def sub(self):
        return self.a - self.b 

    def multiplication(self):
        return self.a * self.b

