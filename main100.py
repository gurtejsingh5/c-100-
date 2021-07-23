class Car(object):

    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.speed_limit=speed_limit
        self.company=company  

    def start(self):
        print ("started")
    def stop(self): 
        print("stopped")
    def accerlate(self):
        print("accerlated")   
    def change_gear(self,gear_type):
        print(" gear changed")


audi=Car("A6","black","audi",80)

print(audi.change_gear(2))         #call function