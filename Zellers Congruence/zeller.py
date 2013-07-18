#Zeller Method project
# We'll be using Zeller's congruence, which is an algorithm devised by Christian Zeller to 
# calculate the day of the week for any Julian or Gregorian calendar date:
#h = ( ( q +( (m+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
#... all of which translates to this:
#dayOfWeek = (dayOfMonth + ((month + 1) * 26 // 10) + year + (year // 4) +
#   6 * (year/ / 100) + (year // 400)) % 7)
# Note that in this algorithm, January and February are counted as
# months #13 & #14 of the previous year, which will need to factor into your method.

def zeller(q, m, Y):
    month=['January','February','March','April','May','June','July','August','September','October','November','December']
    weekDay=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for i in range(0,12):
        if(month[i]==m):
            m=i+1
            break
    if (m<3):
        m = m+12
        Y -=  1
    h = ( ( q +( (m+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
    return weekDay[h-1]