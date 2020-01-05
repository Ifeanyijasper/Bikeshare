import time
import calendar
import numpy as np
import pandas as pd


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs   
    while True:
        city = str(input("Which city data would you like to see for 'Chicago, New York City, or Washington'?\n")).lower()
        if city in ['chicago','new york city','washington']:
            print("Looks like you selected {}.".format(city))
            break
        print('Please enter a valid city')
        # To DO: Get user choice of filter(The way the user wish to filter the data)
    while True:
        data = str(input("Do wish to filter the data by Month, Day, Both or 'none' for no filter?\n")).lower()
        if data in ['month','day','both','none']:
            break
        print("please choose correctly")

    while True:
        # TO DO: get user input for month (all, january, february, ... , june)
        if data == 'month':
            month = str(input("Which month? January, February, March, April, May, June \n")).lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june']:
            # Set day to all
                day = 'all'
                break
            print('Please enter a valid month')
        elif data == 'day':
            # set Month to all
            month = 'all'
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = str(input("Please type out the day name in full\n")).lower()
            if day in ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]:
                break
            print('Please enter a valid day')

        elif data == 'both':
            # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                month = str(input("Which month? January, February, March, April, May, June \n")).lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june']:              
                    break
                print('Please enter a valid month')
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = str(input("Please type out the day name in full \n")).lower()
            if day in ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]:
                break
            print('Please enter a valid day name...... Repeat')
        elif data == 'none':
            # set month and day to all
            month = day = 'all'
            break
    print('-'*40)
    return city,month,day


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nCalculating the first statistic....')
    df['month'] = df['month'].apply(lambda x: calendar.month_name[x])
    print('Most common month:', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nCalculating the next statistic....')
    print('Most common day of the week:',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\nCalculating the next statistic....')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    print('Most common start hour:',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nCalculating the first statistic....')
    print('Most common used start station:',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nCalculating the next statistic....')
    print('Most common used End station:',df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('\nCalculating the next statistic....')
    df['start_end_station'] = (df['Start Station'] + ' ' + df['End Station'])
    print('Most frequent combination of start and end station:',df['start_end_station'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nCalculating the first statistic....')
    print('Total travel time:',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nCalculating the first statistic....')
    print('Mean travel time:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCalculating the first statistic....')
    print('User Type classification:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('\nCalculating the next statistic....')
    try:
        print('Gender distribution:\n',df['Gender'].value_counts())
    except:
        print("We're sorry! There is no data of user genders for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating the next statistic....')
    try:
        birth_year = df['Birth Year'].min()
        print('\nThe earliest birth year:',birth_year)
        birth_year = df['Birth Year'].max()
        print('\nThe most recent birth year :',birth_year)
        birth_year = df['Birth Year'].mode()[0]
        print('\nThe most common birth year :',birth_year)
    except:
        print("We're sorry! There is no data of user birth_year for this city")
# Try and Except Method is used to prevent Data set with no data for Gender and birth year from creating errors

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # TO DO: Display 5 lines of raw data in a given city 
    x = 1
    while True:
        raw = input('\nDo you wish to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        #Unpack the raw data input from the user
        city ,month, day = get_filters() 
        #Load the data to the dataframe
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()