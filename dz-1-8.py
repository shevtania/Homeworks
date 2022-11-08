import  datetime


users = [
    {"name": "Mick", "birsday": datetime.date(2001, 1, 1)},
    {"name": "Barsik", "birsday": datetime.date(2002, 2, 2)},
    {"name": "Simon", "birsday": datetime.date(2003, 3, 3)},
    {"name": "Nick", "birsday": datetime.date(2004,4, 4)},
    {"name": "Barik", "birsday": datetime.date(2005, 11, 5)},
    {"name": "Simona", "birsday": datetime.date(2006, 11, 6)},
    {"name": "Micky", "birsday": datetime.date(2007, 7, 7)},
    {"name": "Barry", "birsday": datetime.date(2008, 8, 8)},
    {"name": "Sily", "birsday": datetime.date(2009, 9, 9)},
    {"name": "Mickel", "birsday": datetime.date(2010, 10, 10)},
    {"name": "Berry", "birsday": datetime.date(2011, 11, 11)},
    {"name": "Lisa", "birsday": datetime.date(2012, 12, 12)},
    {"name": "Nadya", "birsday": datetime.date(1999, 11, 21)},
    {"name": "Natasha", "birsday": datetime.date(1987, 11, 15)},
    {"name": "Serg", "birsday": datetime.date(1967, 11, 29)},
    {"name": "Yana", "birsday": datetime.date(1979, 11, 8)},
    {"name": "Sofi", "birsday": datetime.date(1978, 11, 9)},
    {"name": "Ken", "birsday": datetime.date(1977, 11, 10)},
    {"name": "Vally", "birsday": datetime.date(2000, 11, 11)},
    {"name": "Tom", "birsday": datetime.date(2021, 11, 12)},
    {"name": "John", "birsday": datetime.date(1998, 11, 13)},
    {"name": "Jeck", "birsday": datetime.date(1997, 11, 14)},
    {"name": "Pol", "birsday": datetime.date(1996, 11, 15)},
    {"name": "Dariya", "birsday": datetime.date(1950, 11, 16)}
]
def list_to_string(list_day):
        string = ', '.join(list_day)
        return string

def get_birthdays_per_week(users):
    week = datetime.timedelta(days=7)
    current_date = datetime.date.today() 
    
    current_year = current_date.year
    current_weekday = datetime.date.weekday(current_date) 
    users_current_year = []
    list_mon = []
    list_tue = []
    list_wed = []
    list_thu = []
    list_fri = []
    week_birthday_list = [] 

    week_after_today = current_date + week
    for diction in users:
        value = diction['birsday'].replace(year=current_year)
        diction['birsday'] = value
        users_current_year.append(diction)
    
    for diction in users_current_year:
        value = diction['birsday']
        week_day = value.weekday()


        if week_day == 5 and (value >= (current_date - datetime.timedelta(days=2))    and value < week_after_today):
            value = value + datetime.timedelta(days=2) 
            week_day = value.weekday()
            
        elif week_day == 6 and (value >= (current_date - datetime.timedelta(days=1))    and value < week_after_today):
            value = value + datetime.timedelta(days=1) 
            week_day = value.weekday()

        if week_day == 0 and (value >= current_date    and value < week_after_today):
            list_mon.append(diction['name'])
            
        elif week_day == 1 and (value >= current_date    and value < week_after_today):
            list_tue.append(diction['name'])
           
        elif week_day == 2 and (value >= current_date    and value < week_after_today):
            list_wed.append(diction['name'])
            
        elif week_day == 3 and (value >= current_date    and value < week_after_today):
            list_thu.append(diction['name'])
          
        elif week_day == 4 and (value >= current_date    and value < week_after_today):
            list_fri.append(diction['name'])
          
   

    week_birthday_list = [list_to_string(list_mon), list_to_string(list_tue), list_to_string(list_wed), list_to_string(list_thu), list_to_string(list_fri)]
    week_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednessday', 3: 'Thursday', 4: 'Friday'}

    for i in range(5):
        if current_weekday > 4:
           current_weekday = current_weekday - 5
      
        print(f'{week_days[current_weekday]} : {week_birthday_list[current_weekday]}')
        current_weekday = current_weekday + 1
        



   



