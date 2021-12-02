def calculate_annual_consumption(montly_consumption,month,consumption):
    months=["ianuarie","februarie","martie","aprilie","mai","iunie","iulie","august","septembrie","octombrie","noiembrie","decembrie"]
    month=month.lower()
    index_month=months.index(month)
    return int(consumption*(100/montly_consumption[index_month]))

#Popa Iulia