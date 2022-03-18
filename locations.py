class Location:
    def __init__(self, name):
        self.name = name
        self.base_rate = 0
        self.two_diff = 0
        self.three_diff = 0
        self.weekend_diff = 0
        # do the diffs stack?
        self.stack = False
        self.tax_withholding = 0
        # default shift times
        self.first = (7, 15)
        self.second = (15, 23)
        self.third = (23, 7)

    def change_shift_times(self, shift, start, stop):
        if shift == 1:
            self.first = (start, stop)
        elif shift == 2:
            self.second = (start, stop)
        else:
            self.third = (start, stop)


    def set_rates(self, base, two, three, WE,stack):
        if stack:
            self.stack = True
        self.base_rate = base
        self.two_diff = two
        self.three_diff = three
        self.weekend_diff = WE
        
    def set_tax(self, tax_estimate):
        # this is just to estimate what will be witheld. 
        # the estimate should just be the total % witheld estimate.
        self.tax_withholding = tax_estimate

    # def estimate_pay_block(self, workdays):
    #     gross_sum = 0
    #     for day in workdays:
    #         gross_sum += self.get_daily_pay(day)
    #     net_sum = gross_sum * (1-self.tax_withholding)
    #     return net_sum
    
    # def get_daily_pay(self, day):



class Workday:
    def __init__(self, location_name, start_time, end_time):
        self.location = location_name
        self.start_time = start_time
        self.end_time = end_time