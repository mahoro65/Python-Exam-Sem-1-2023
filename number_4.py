#number 4(i)
#1
print(1)

print(12)

print(1234)

print(12345)


#(ii)
def myfunction(n):
    if n==0 or n==1:
        return 1
    else:
        return n* myfunction(n-1)
    
#testing my function with n=5
output=myfunction(5)
print(f" The function of 5 is{output}")    
    


#(iii)
def sum_of_numbers(a,b):
     output =a + b
print(f"sum of {3} and {4} is {3+4}")



#iv
class my_car:
    def __init__(self, brand, year):
        self.year = year
        self.brand = brand

    def display_information(self):
        print(f"Information about the car: {self.year} {self.brand}")


my_car = my_car( year=2000,brand="Benz")
my_car.display_information()






     
     #v
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# Creating instance of the Car class
my_car= Car(brand="bens", year=2000)

# Displaying the information
print(f"My car is a {my_car.year} {my_car.brand}.")


