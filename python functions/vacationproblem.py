import math
vacation = [{
    'City':'Paris',
    'Return_Flight':200,
    'Hotel_Per_Day':20,
    'Weekly_Car_Rental':200
},{
    'City':'London',
    'Return_Flight':250,
    'Hotel_Per_Day':30,
    'Weekly_Car_Rental':120
},{
    'City':'Dubai',
    'Return_Flight':370,
    'Hotel_Per_Day':15,
    'Weekly_Car_Rental':80
},
{
    'City':'Mumbai',
    'Return_Flight':450,
    'Hotel_Per_Day':10,
    'Weekly_Car_Rental':70
}]

# Least Amount 1 week trip
def calculate_budget(number_of_days):
    city_spend = []
    for cities in range(0,len(vacation)):
        total_cost = 0 
        hotel_cost = vacation[cities]['Hotel_Per_Day'] * number_of_days
        car_cost = vacation[cities]['Weekly_Car_Rental'] * math.ceil(number_of_days/7)
        total_cost += vacation[cities]['Return_Flight'] + hotel_cost + car_cost
        city_spend.append(total_cost)
    
    index_number = city_spend.index(min(city_spend))
    return('The Least Expensive City To Visit is {}, with a budget of {}'
           .format(vacation[index_number]['City'],city_spend[index_number]))

print('For 7 Days, ',calculate_budget(7))
print('For 4 Days, ',calculate_budget(4))
print('For 10 Days, ',calculate_budget(10))
print('For 14 Days, ',calculate_budget(14))


def Calculate_Stays(spending_budget):
    staying_days_list = []
    for cities in range(0,len(vacation)):
        staying_days=0
        remaining_budget = spending_budget - vacation[cities]['Return_Flight']
        Weekly_Car_Hotel_Cost = vacation[cities]['Weekly_Car_Rental'] + (7*vacation[cities]['Hotel_Per_Day'])
        while remaining_budget>0:
            if remaining_budget>Weekly_Car_Hotel_Cost:
                remaining_budget -= Weekly_Car_Hotel_Cost
                staying_days +=7
            else:
                remaining_budget -= vacation[cities]['Weekly_Car_Rental']
                if remaining_budget >= vacation[cities]['Hotel_Per_Day']:
                    remaining_budget -= vacation[cities]['Hotel_Per_Day']
                    staying_days += 1
        staying_days_list.append(staying_days)
    index_number1 = staying_days_list.index(max(staying_days_list))
    index_number2 = staying_days_list.index(min(staying_days_list))
    return ('For {} budget maximum you can stay in {} for {} days and minimum you can stay in {} for {} days'
            .format(spending_budget,vacation[index_number1]['City'],staying_days_list[index_number1],
                    vacation[index_number2]['City'],staying_days_list[index_number2]))

print(Calculate_Stays(1000))
print(Calculate_Stays(600))
print(Calculate_Stays(2000))
print(Calculate_Stays(1500))



    
