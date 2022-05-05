input_month = input()
input_day = int(input())
season = ''
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']
short_months = ['February', 'April', 'June', 'September', 'November']
if (input_month not in months):
    print("Invalid")
elif (input_day <= 0) or (input_day > 31):
    print("Invalid")
elif input_month in ('April', 'May'):
    season = 'Spring'
elif input_month in ('July', 'August'):
    season = 'Summer'
elif input_month in ('October', 'November'):
    season = 'Autumn'
elif input_month in ('January', 'February'):
    season = 'Winter'
elif input_month in ('March'):
    if input_day > 19:
        season = 'Spring'
    else:
        season = 'Winter'
elif input_month in ('June'):
    if input_day > 20:
        season = 'Summer'
    else:
        season = 'Spring'
elif input_month in ('September'):
    if (input_day > 21):
        season = 'Autumn'
    else:
        season = 'Summer'
elif input_month in ('December'):
    if (input_day > 20):
        season = 'Winter'
    else:
        season = 'Autumn'
elif input_month in ('March'):
    if (input_day > 19):
        season = 'Winter'
    else:
        season = 'Spring'
if (input_month in months) and (input_month in short_months):
    if (input_month in ('February')) and (input_day > 28):
        print("Invalid")
    elif (input_month in short_months[1:5]) and (input_day > 30):
        print("Invalid")
    else:
        print(season)
if (input_month in months) and (input_month not in short_months):
    print(season)
