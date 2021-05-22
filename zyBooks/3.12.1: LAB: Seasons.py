#Start of Code
#Input for month and day
input_month = str(input())
input_day = int(input())
#If/or month = between range print spring
if input_month == 'March' and 20 <= input_day <= 31\
or input_month == 'April' and 1 <= input_day <= 30\
or input_month == 'May' and 1 <= input_day <= 31\
or input_month == 'June' and 1 <= input_day <= 20:
    print('Spring')
#If/or month = between range print Spring
elif input_month == 'June' and 21 <= input_day <= 30\
or input_month == 'July' and 1 <= input_day <= 31\
or input_month == 'August' and 1 <= input_day <= 31\
or input_month == 'September' and 1 <= input_day <= 30:
    print('Summer')
#If/or month = between range print Summer
elif input_month == 'September' and 22 <= input_day <= 30\
or input_month == 'October' and 1 <= input_day <= 31\
or input_month == 'November' and 1 <= input_day <= 30\
or input_month == 'December' and 1 <= input_day <= 20:
    print('Autumn')
#If/or month = between range print Autumn
elif input_month == 'December' and 21 <= input_day <= 31\
or input_month == 'January' and 1 <= input_day <= 31\
or input_month == 'February' and 1 <= input_day <= 28\
or input_month == 'March' and 1 <= input_day <= 19:
    print('Winter')
 #If/or month = between range print Winter - else = invalid input   
else:
    print('Invalid')
#End of code
