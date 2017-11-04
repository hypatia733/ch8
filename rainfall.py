import math

rainfalls = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

def get_rainfall():
    while len(rainfalls) < 11:
        rain = int(input('Enter rainfall:'))
        rainfalls.append(rain)
        print(rainfalls)

def stats():
    total = sum(rainfalls)
    average = total / len(rainfalls)
    high = max(rainfalls)
    low = min(rainfalls)
    print('Total rainfall:', total)
    print('Average rainfall:', average)
    print('Month with the most rain:', months[high])
    print('Month with the least rain:', months[low])

get_rainfall()
stats()
