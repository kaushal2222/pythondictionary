days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = {}
for day in days:
    temperature = float(input(f"Enter the average temperature for {day}: "))
    avg=temperature/len(days)
    
    print(temperature)
    print(avg)


    

    
