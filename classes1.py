class  Restaurant:
    def __init__ (self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name + " - " + self.cuisine)
    def open_restaurant(self):
        print(self.name + " is open for business")



burger= Restaurant("Bobs Burgers", "American Comfort")   


print(burger.name)
print(burger.cuisine)

burger.describe_restaurant()
burger.open_restaurant()


chinese = Restaurant("Yantse", "Asian")

chinese.describe_restaurant()
#chinese.open_restaurant()


yummy= Restaurant("Beaux's", "Cajun Mystery Meat" )

yummy.describe_restaurant()


#print(burger.decscribe_restaurant)  

#describe_restaurant()

#dont use = when starting a class
class  User:
    def __init__ (self,first_name,last_name):
        self.first = first_name
        self.last = last_name
        self.address = ""
        self.gender = ""
        self.age = ""
        self.login_attempts = 0

    def describe_user(self):
        print(self.first +" " + self.last + " " + self.address + " " + self.gender + " " + self.age)

    def greet_user(self):
        print("Hello " + self.first + " I hope all is well with you today" )

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        #print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0

steve = User("Steve", "Catt")

steve.gender = "Male" 
steve.age = "Young at heart"
steve.increment_login_attempts()
steve.increment_login_attempts()
steve.increment_login_attempts()
steve.increment_login_attempts()
steve.increment_login_attempts()
steve.increment_login_attempts()
steve.increment_login_attempts()
steve.increment_login_attempts()


steve.describe_user()
print(steve.first + " You attemped to login " + str(steve.login_attempts) + " times")

steve.reset_login_attempts()
print (steve.login_attempts)
mary = User("Mary","Lamb")




mary.describe_user()

mary.greet_user()
steve.greet_user()


mary.increment_login_attempts()
mary.increment_login_attempts()
mary.increment_login_attempts()


print(mary.first + " You attemped to login " + str(mary.login_attempts) + " times")