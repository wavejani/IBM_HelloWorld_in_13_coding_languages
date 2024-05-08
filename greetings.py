import datetime

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Morning"
    elif 12 <= current_hour < 17:
        return "Day"
    elif 17 <= current_hour < 20:
        return "Evening"
    else:
        return "Night"

def main():
    name = input("Enter your name: ")
    time_of_day = get_time_of_day()
    print(f"Hello {name}! Good {time_of_day}!")

if __name__ == "__main__":
    main()


