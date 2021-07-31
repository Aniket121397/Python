from tempe import Temperature
if __name__ == "__main__":
    celcious=float(input("Enter the value of celcious : "))
    fahrenheit=int(input("Enter the value of fahre:"))
    A=Temperature(celcious,fahrenheit)
    print("The value of Fahrenheit is:-" ,A.get_fahrenheit())
    print("The value of Celcious is :-",A.get_celcious())
    
    


    