def convert_time(hour, minute, am_pm):
    if hour > 12:
        hour -= 12
        am_pm = 'P'
    elif hour == 12:
        am_pm = 'P'
    elif hour == 0:
        hour = 12
        am_pm = 'A'

    return f"{hour}:{minute:02d} {am_pm}.M."

def main():
    while True:
        hour = int(input("Enter the hour (0-23): "))
        minute = int(input("Enter the minute (0-59): "))
        print(convert_time(hour, minute, 'A'))
        response = input("Do you want to convert another time? (y/n): ")
        if response.lower() != 'y':
            break

main()