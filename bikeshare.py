## TODO: import all necessary packages and functions
import csv, time, datetime
from collections import Counter

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    city = city.strip().lower()

    valid_cities = ['chicago','new york', 'washington']

    while city not in valid_cities:
        city = input('\nSorry, I don\'t know that city. Try again.\n'
            'Would you like to see data for Chicago, New York, or Washington?\n')

    if city == 'chicago':
        return chicago
    elif city == 'new york':
        return new_york_city
    elif city == 'washington':
        return washington

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) month, day, or none for time_period filter.
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    time_period = time_period.strip().lower()
    
    valid_time_periods = ['month','day','none']

    while time_period not in  valid_time_periods:
        time_period = input('\nI don\'t understand that.'
                            '\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')

    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) month
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    month = month.strip().lower()

    valid_months = ['january','february','march','april','may','june']

    while month not in valid_months:
        month = input('\nI don\'t have data for that month\n'
                      'Which month? January, February, March, April, May, or June?\n')

    return month

def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    while True:
        try:
            day = int(input('\nWhich day? Please type your response as an integer.\n'))
    # TODO: handle raw input and complete function
        except ValueError:
            print('\nI don\'t know what that is.')
            continue
        else: 
            break

    return day

    ## day of month? 

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    with open(city_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        months = []
        for row in reader:
            date = row['Start Time'].split(' ')[0]
            month = date.split('-')[1]
            months.append(month)

    count = Counter(months)
    popular_month = count.most_common(1)[0][0]

    if popular_month == '01':
        return 'January'
    if popular_month == '02':
        return 'February'
    if popular_month == '03':
        return 'March'
    if popular_month == '04':
        return 'April'
    if popular_month == '05':
        return 'May'
    if popular_month == '06':
        return 'June'

def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    with open(city_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dates = []
        for row in reader:
            date = row['Start Time'].split(' ')[0]
            dates.append(date) # days is list of dates as lists (not datetime objects)
            
        # list comprehension for datetime objects
        # https://stackoverflow.com/questions/30487870/
    
    days = [datetime.datetime.strptime(date, '%Y-%m-%d').date().weekday() for date in dates]
    
    count = Counter(days)
    popular_day = count.most_common(1)[0][0] 

    if popular_day == 0:
        return 'Monday'
    if popular_day == 1:
        return 'Tuesday'
    if popular_day == 2:
        return 'Wednesday'
    if popular_day == 3:
        return'Thursday'
    if popular_day == 4:
        return 'Friday'
    if popular_day == 5:
        return 'Saturday'    
    if popular_day == 6:
        return 'Sunday'
    

def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    with open(city_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        hours = []
        for row in reader:
            time = row['Start Time'].split(' ')[1]
            hour = time.split(':')[0]
            hours.append(hour) # days is list of dates as lists (not datetime objects)

    count = Counter(hours)
    popular_hour = int(count.most_common(1)[0][0])

    if popular_hour == 0:
        return '12 a.m.'
    elif popular_hour == 12:
        return '12 p.m.'
    elif popular_hour <= 11:
        return '{} a.m.'.format(popular_hour)
    elif popular_hour > 12:
        popular_hour -= 12
        return '{} p.m.'.format(popular_hour)


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    with open('chicago.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        totaL_duration = 0
        rows = 0
        for row in reader:
            totaL_duration += int(row['Trip Duration'])
            rows += 1

    return (totaL_duration, totaL_duration/rows)

def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    with open(city_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        starts = []
        ends = []
        for row in reader:
            starts.append(row['Start Station'])
            ends.append(row['End Station'])

    start_count = Counter(starts)
    end_count = Counter(ends)

    popular_start = start_count.most_common(1)[0][0]
    popular_end = end_count.most_common(1)[0][0]

    return(popular_start,popular_end)



def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        print(popular_month(city, time_period) + " is the most popular month.")
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        print(popular_day(city, time_period) + " is the most popular day.")        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    print(popular_hour(city,time_period) + " is the most popular hour of the day.")
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    durations = trip_duration(city, time_period)
    print("The total duration is {} seconds.\nThe average duration is {} seconds.".format(durations[0],durations[1]))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    stations = popular_stations(city, time_period)
    print("The most popular start station is {}.\nThe most popular end station is {}".format(stations[0],stations[1]))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()