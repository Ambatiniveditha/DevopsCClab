def calculate_electricity_cost(power, time, rate):
    """
    Calculate the cost of electricity.
    
    Parameters:
    power (float): Power consumption in kilowatts (kW)
    time (float): Time of use in hours
    rate (float): Cost per kilowatt-hour (kWh) in your currency

    Returns:
    float: Total electricity cost
    """
    energy_consumed = power * time  # in kWh
    cost = energy_consumed * rate     # in currency
    return cost

def main():
    print("Electricity Cost Calculator")
    
    try:
        power = float(input("Enter power consumption (in kW): "))
        time = float(input("Enter time of use (in hours): "))
        rate = float(input("Enter cost per kWh: "))

        total_cost = calculate_electricity_cost(power, time, rate)

        print(f"\nTotal electricity cost: {total_cost:.2f} (currency)")
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == '__main__':
    main()
