import datetime
import csv
import pandas as pd

while True:

    Name = input('Enter your name: ')

    Year = int(input('Enter the year that you were born (e.g 2001):'))
    if Year % 4 == 0:
            print ('It is a leap year')
    else:
            print ('It is a common year')

    Month = input ('Enter the month that you were born: ')


    if Month == 'January' or Month == 'january' or Month == 'Jan' or Month == 'jan' or Month == '1' or Month == '01':
        month_number = 1
    elif Month == 'February' or Month == 'february' or Month == 'Feb' or Month == 'feb' or Month == '2' or Month == '02':
        month_number = 2
    elif Month == 'March' or Month == 'march' or Month == 'Mar' or Month == 'mar' or Month == '3' or Month == '03':
        month_number = 3  
    elif Month == 'April' or Month == 'april' or Month == 'Apr' or Month == 'apr' or Month == '4' or Month == '04':
        month_number = 4
    elif Month == 'May' or Month == 'may' or Month == '5' or Month == '05':
        month_number = 5
    elif Month == 'June' or Month == 'june' or Month == 'Jun' or Month == 'jun' or Month == '6' or Month == '06':
        month_number = 6
    elif Month == 'July' or Month == 'july' or Month == 'Jul' or Month == 'jul' or Month == '7' or Month == '07':
        month_number = 7
    elif Month == 'August' or Month == 'august' or Month == 'Aug' or Month == 'aug' or Month == '8' or Month == '08':
        month_number = 8   
    elif Month == 'September' or Month == 'september' or Month == 'Sept' or Month == 'sept' or Month == '9' or Month == '09':
        month_number = 9
    elif Month == 'October' or Month == 'october' or Month == 'Oct' or Month == 'oct' or Month == '10':
        month_number = 10
    elif Month == 'November' or Month == 'november' or Month == 'Nov' or Month == 'nov' or Month == '11':
        month_number = 11
    elif Month == 'December' or Month == 'december' or Month == 'Dec' or Month == 'dec' or Month == '12':
        month_number = 12
    else:
        print ('Invalid Month')
        break


    Day = int(input ('Enter the date that you were born (Date is between 1 and 31): '))
    if Day < 0 or Day >31:
        print ('Invalid Date!')
        break
    
    else:
        print(Day)

    Date_of_birth = datetime.date(Year, month_number, Day)
    print ('Your date of birth is ', Date_of_birth)


    if month_number==12:
        zodiac_sign='Sagitarius' if (Day < 22) else 'Capricorn'
    elif month_number==1:
        zodiac_sign='Capricorn' if (Day < 20) else 'Aquarius'
    elif month_number==2:
        zodiac_sign='Aquarius' if (Day < 19) else 'Pisces'
    elif month_number==3:
        zodiac_sign='Pisces' if (Day < 21) else 'Aries'
    elif month_number==4:
        zodiac_sign='Aries' if (Day < 20) else 'Taurus'
    elif month_number==5:
        zodiac_sign='Taurus' if (Day < 21) else 'Gemini'
    elif month_number==6:
        zodiac_sign='Gemini' if (Day < 21) else 'Cancer'
    elif month_number==7:
        zodiac_sign='Cancer' if (Day < 23) else 'Leo'
    elif month_number==8:
        zodiac_sign='Leo' if (Day < 23) else 'Virgo'
    elif month_number==9:
        zodiac_sign='Virgo' if (Day < 23) else 'Libra'
    elif month_number==10:
        zodiac_sign='Libra' if (Day < 23) else 'Scorpio'
    elif month_number==11:
        zodiac_sign='Scorpio' if (Day < 22) else 'Sagitarius'
    else:
        print ('Error \n Please re-try')

    print ('Hello', Name + '\n Your Zodiac Sign is', zodiac_sign)

    New_operation = input ('Do you want to check for another zodiac sign (yes/no):')
    if New_operation == 'no':
        break

User_Data = {Name, Date_of_birth, zodiac_sign}
print (User_Data)

df=pd.DataFrame(data=User_Data)
file_name = input ('Please enter the file name:')
Saved_Data = df.to_csv(file_name+'.csv', index=True)


