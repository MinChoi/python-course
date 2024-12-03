# march-case - switch
# available after 3.10

def day_of_week(day):
    match day:
        case 1:
            return 'Sunday'
        case 2:
            return 'Monday'
        case 3:
            return 'Tuesday'
        case 4:
            return 'Wednesday'
        case 5:
            return 'Thursday'
        case 6:
            return 'Friday'
        case 7:
            return 'Saturday'
        case _:
            return 'not valid'


print(day_of_week(1))


##

def is_weekend(day):
    match day:
        case 'Sunday' | 'Saturday':
            return 'it is weekend!'
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            return 'not weekend..'
        case _:
            return 'not specified'

print(is_weekend('Sunday'))
print(is_weekend('Tuesday'))
print(is_weekend('today? '))
