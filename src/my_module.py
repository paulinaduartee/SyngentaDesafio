from datetime import datetime,date
from src.module.hotels import Hotels

def get_lower_value(hotels_value: list):
    result = []
    lower_value=0
    for hotel in hotels_value:
        if lower_value == 0:
            lower_value=hotel['value']
            result.append(hotel)
        elif hotel['value'] < lower_value:
            lower_value=hotel['value']
            result = []
            result.append(hotel)
        elif lower_value == hotel['value']:
            result.append(hotel)
    return max(result, key=lambda x: x['classification'])['name']

def get_cheapest_hotel(number):   #DO NOT change the function's name

    Lakewood = Hotels(name='Lakewood',classification=3,regular_weekday=110,regular_weekend=90,rewards_weekday=80,rewards_weekend=80)
    Bridgewood = Hotels(name='Bridgewood',classification=4,regular_weekday=160,regular_weekend=60,rewards_weekday=110,rewards_weekend=50)
    Ridgewood = Hotels(name='Ridgewood',classification=5,regular_weekday=220,regular_weekend=150,rewards_weekday=100,rewards_weekend=40)

    hotels = [Lakewood,Bridgewood,Ridgewood]
    [client, days_without_editing] =  number.split(':')

    days = days_without_editing.split(',')

    formated_days = []

    for day in days:
        date_formated = date(int(day[6:10]),datetime.strptime(day[3:6], "%b").month,int(day[1:3]))
        formated_days.append(date_formated)

    hotel_values = []

    for hotel in hotels:
        value = 0 
        for day in formated_days:
            if day.isoweekday() <= 5:
                value+=hotel.get_weekday(client)
            else:
                value+=hotel.get_weekend(client)
        hotel_values.append({'name': hotel.name,'classification': hotel.classification, 'value': value})

    cheapest_hotel = get_lower_value(hotel_values)

    return cheapest_hotel
