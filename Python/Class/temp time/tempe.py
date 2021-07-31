class Temperature:
    def __init__(self,celcious,fahrenheit):
        self.fahrenheit=fahrenheit
        self.celcious=celcious
    def get_fahrenheit(self):
         fahre=(self.celcious*(9/5))+32
         return fahre

    def get_celcious(self):
        cel= (self.fahrenheit-32)*(5/9)
        return cel

