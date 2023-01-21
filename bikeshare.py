import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    cities = ['chicago', 'new york', 'washington']
    months = [ ' january', 'febraury', 'march', 'april', 'may', 'june','all']
    days = ['saturday', 'sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday','all'
           
           ]
    city = input('Enter city name:').title()
    while city not in cities:
        print('invalid input')
       
        city = input('Enter city name:')
    print('the city name is' , city) 
    month = input('Enter month name:').lower()
    while month not in months:
        month = input('Enter month name:'). lower()
    day = input('Enter day name:').lower()
    while day not in days:
        day = input('Enter day name:').lower()
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load data file
    df = pd.read_csv(CITY_DATA[city])
    # covert the start time column to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
    #extract month and day from Start Time to creat new columns
    df['month']=df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if aplicable 
    if month != 'all':
        months =['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by months to creat the new dataframe
        df = df[df['month'] ==month]
        print(df)
        
    # filter by day of week if aplicable
    if day != 'all':
        # filter by day of wek to creat the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print(df)
    
        
    
        
      

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print('the most common month is:', common_month) 


    # TO DO: display the most common day of week
    common_day_of_week= df['day_of_week'].mode()
    print('the most common day of week is :', common_day_of_week)


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()
    print('the most common start houris:',common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()


    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()
    print('the most common used end station:', most_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_end_station_trip = (df['Start Station']+ df['End Station']).mode()
    print('the most frequent combination is:', most_frequent_combination_of_start_end_station_trip) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean of the travel time is:',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types= df['User Type'].value_counts()
    print(' the counts of user types are:', counts_of_user_types)


    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of gender:', counts_of_gender)
    except:
        print(' the gender column is not available')
              


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].max()
        print('earlist year of birth:', earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].min()
        print('most recent year of birth:', most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()
        print('most common birth year:', most_common_birth_year)
    except:
        print('the birth year column is not available')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(city):
    sample_question = input('Enter the answer is:')
    while sample_question == 'yes':
        df = pd.read_csv(CITY_DATA[city])
        print(df.sample(n=5))
        sample_question = input('Enter the answer is:').lower()      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
