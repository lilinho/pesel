import datetime

# counters
total = correct = male = female = 0
invalid_length = invalid_digit = invalid_date = invalid_checksum = 0

# date variables
day = month = year = 0

PESEL_length = 11
PESEL_weigths= (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)

def make_year(m, y):

    if m - 80 > 0:
        y = "18" + y
    elif m - 60 > 0:
        y = "22" + y
    elif m - 40 > 0:
        y = "21" + y
    elif m - 20 > 0:
        y = "20" + y
    else:
        y = "19" + y

    return int(y)

def last_day(m, y):
    m += 1
    if m == 13:
        m = 1
        y += 1


    first_of_next_month = datetime.date(y, m, 1)
    last_of_month = first_of_next_month - datetime.timedelta(days=1)
    return last_of_month


file = open("1e3.dat", 'r')

# main processing loop
for PESEL in file:
    PESEL = PESEL.strip()
    total +=1
    if len(PESEL) != PESEL_length:
        invalid_length += 1
        continue
    elif not PESEL.isnumeric():
        invalid_digit += 1
        continue
    
    day = int(PESEL[4:6])
    month = int(PESEL[2:4])%20 #modulo!!
    year = make_year(month, PESEL[0:2])
    print(type(day))
    #if datetime(day) > last_day(month, year):
     #   invalid_date += 1

    
