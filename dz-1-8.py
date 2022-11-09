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

def print_from_dict(current_weekday, week_birthday):
    name_list = []
    week_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednessday', 3: 'Thursday', 4: 'Friday'}

    for i in range(5):

        if current_weekday in (5,6):
           current_weekday = 0

        name_list = week_birthday[current_weekday]
        string = ', '.join(name_list)
        
        print(f'{week_days[current_weekday]} : {string}')
        current_weekday = current_weekday + 1
                    
       
    return 

def get_birthdays_per_week(users):
   
    users_week_birthday = []
    
    week_congratulated = {0: [], 1: [], 2: [], 3: [], 4: []}

    
    current_date = datetime.date.today()
    current_year = current_date.year
    current_weekday = datetime.date.weekday(current_date) 
    
# for monday we have to include 2 dey before - saturday, sunday, other days - (today + week)
    if current_weekday == 0:
        first_day_interval = current_date - datetime.timedelta(days=2)
    else:
        first_day_interval = current_date   
    last_day_interval = first_day_interval + datetime.timedelta(days=7)

    
#  new list of dict with new value of year    
    for dictionary in users:
        current_birthday = dictionary['birsday'].replace(year=current_year)
        
        if current_birthday >= first_day_interval and current_birthday < last_day_interval:
            dict_curr_year = dictionary.copy()
            dict_curr_year['birsday'] = dict_curr_year['birsday'].replace(year=current_year)
            users_week_birthday.append(dict_curr_year)
    
        
        
    for user in users_week_birthday:
        value = user['birsday']
        week_day = value.weekday()
        name = user['name']
        
        if week_day in (5,6):
            week_day = 0
        
        if week_day in week_congratulated.keys():
            week_congratulated[week_day].append(name)
        
  
    print_from_dict(current_weekday, week_congratulated)   
        
        
        
    
# get_birthdays_per_week(users)


   



