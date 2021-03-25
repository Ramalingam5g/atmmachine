class Car:
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print("starting")
        
    def stop(self):
        print("stopping")
        
    def accelerator(self):
        a=8.5+4.5
        print(a)
        if a==float:
            print("done well")
        else:
            print("nothing")

    def gear(self):
        print("first gear is done")
        
obj=Car("audi","black","audi",33.8)
obj.start()
obj.stop()
obj.accelerator()
obj.gear()


    