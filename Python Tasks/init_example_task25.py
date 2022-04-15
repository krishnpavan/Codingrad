print("                               ** Task 25 **                            ")
print("Laptop purchase program using __init__ constructor")

class Laptop_purchase(): # class declaration or definition
    # brand,laptop_purpose,processor_brand,
    # processor_type,graphics_card,price all are parameters
    def __init__(self,brand,laptop_purpose,processor_brand,processor_type,graphics_card,price):
        # Always remember left side is attribute or variable
        # right side is called value
        # so in self.a = brand. brand known as value
        # so a,b,c,d,e,f are attributes or data members
        # self.a,self.b,self.c is used to access
        # a,b,c attributes through out program using
        # self keyword
        self.a = brand
        self.b = laptop_purpose
        self.c = processor_brand
        self.d = processor_type
        self.e = graphics_card
        self.f = price
    def Pavan_laptop(self): # member function declaration
        print(self.a)
        print(self.b) 
        print(self.c) 
        print(self.d) 
        print(self.e) 
        print(self.f)
brand = input('Enter Laptop Brand Name: ')
laptop_purpose = input('Enter for what purpose you are purchasing laptop: ')
processor_brand = input('Enter processor brand name you want to purchase: ')
processor_type = input('Enter processor type: ')
graphics_card = input('Enter grahic card name: ')
price = float(input('Enter price of the laptop: '))

# declaring the object laptop_obj
laptop_obj = Laptop_purchase(brand,laptop_purpose,processor_brand,processor_type,graphics_card,price)

# calling the object using member function Pavan_laptop
laptop_obj.Pavan_laptop()







