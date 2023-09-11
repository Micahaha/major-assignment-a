def main():

    day_selection = int(input('Please enter a number (1 - 12): '))
    translated_day = change_day(day_selection)
    print_mantra(day_selection, translated_day)



def print_mantra(day, day_translated):
    if day >= 0 and day <= 12:
        print(f'On the {day_translated} of Christmas, my true love gave to me ...')


        # made a list I can access to correspond to the value the user selected
        
        days_of_christmas = ['A partridge in a pear tree', 
                        'Two turtledoves', 
                        'Three French hens',
                        'Four calling birds',
                        'Five golden rings',
                        'Six geese a-laying',
                        'Seven swans a-swimming',
                        'Eight maids a-milking',
                        'Nine ladies dancing',
                        'Ten lords a-leaping',
                        'Eleven pipers piping',
                        'Twelve drummers drumming']
    
        # iterate value by 1 so its the true value the user selected
        day-=1
        i=day
        while (i >= 0):
            print(days_of_christmas[i])
            i-=1 

    else:
        print('Invalid Number')
   

# match and case selection 

def change_day(day):
    match day:
        case 1:
            return 'first'
        case 2:
            return 'second'
        case 3:
            return 'third'
        case 4:
            return 'fourth'
        case 5:
            return 'fifth'
        case 6:
            return 'sixth'
        case 7:
            return 'seventh'
        case 8:
            return 'eighth'
        case 9:
            return 'ninth'
        case 10:
            return 'tenth'
        case 11:
            return 'eleventh'
        case 12:
            return 'tweleth'
            

main()