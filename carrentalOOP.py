

import datetime

class CarRental:
    
    def __init__(self,stock=0):
              
    def displaystock(self):

        """Displays the carss currently available for rent in the shop."""
        
         print("We currently have {} cars available to rent.".format(self.stock))
        return self.stock

    def rentCarOnHourlyBasis(self, i):
          # reject invalid input
        if i <= 0:
            print("Number of cars to be positive!")
            return None        # do not rent car is stock is less than requested cars
        
        elif i > self.stock:
            print("Sorry! We currently have {}cars available to rent.".format(self.stock))
            return None        # rent the cars
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} car(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged Ksh.5000 an hour per car.")
            print("Hope you enjoy our service.")            
            self.stock -=i 
            return now      
     
     def rentCarOnDailyBasis(self, i):

                if i <= 0:
            print("Number of cars should be positive!")
            return None        
        elif i > self.stock:
            print("Sorry! We currently have {} cars available to rent.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} cars) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged Ksh.200000 for each day per car.")
            print("Hope you enjoy our service.")            
            self.stock -= i
            return now
        
    def rentCarOnWeeklyBasis(self, i):
        
        if i <= 0:
            print("Number of cars should be positive!")
            return None
        elif i > self.stock:
            print("Sorry! We currently have {} cars available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} cars(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged Ksh.500000 for each week per car.")
            print("Hope that you enjoy our service.")
            self.stock -= i
            return now
        
    def returnCars(self, request):
        
        # extract the tuple and initiate bill        rentalTime, rentalBasis, numOfCars = request
          bill = 0        
        # issue a bill only if all three parameters are not null!        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            #the hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5000 * numOfCars
                
            #the daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20000 * numOfCars
                
            #the weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 50000 * numOfCars
            
            #the family discount calculation            if (3 <= numOfCars <= 5):
                print("You are eligible to Family rental promotion of 30% discount")
                bill = bill * 0.7
                print("Thanks for returning your car. Hope you enjoyed our service!")
                print("That would be Ksh{}".format(bill))
                return bill
        
           else:
               print("You sure you rented a car with us?")
               return Noneclass Customer: 
            
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0    
    def requestCars(self):
        """
        Takes a request from the customer for the number of cars.
        """
                      
        cars = input("How many cars would you like to rent?")
        
        # to implement logic for invalid input
        try:
            cars = int(cars)
        except ValueError:
            print("Not a positive integer!")
            return -1        
        if cars < 1:
            print("Invalid input. Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
        return self.cars
     
    def returnCar(self):
        """
        Allows customers to return their cars to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars  
        else:
            return 0,0
