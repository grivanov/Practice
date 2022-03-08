class Temperature:
    # Write your code here
    min_temperature = 0
    max_temperature = 1000

    @classmethod
    def update_min_temperature(cls, num):
        if num >= cls.max_temperature:
            raise Exception("Invalid temperature.")

        cls.min_temperature = num
    
    @classmethod 
    def update_max_temperature(cls, num):
        if num <= cls.min_temperature:
            raise Exception("Invalid temperature.")

        cls.max_temperature = num

    def __init__(self, temper):
        self.kelvin = temper
        if temper < Temperature.min_temperature or temper > Temperature.max_temperature:
            raise Exception("Invalid temperature.")
