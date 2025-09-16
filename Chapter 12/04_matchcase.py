def day_activity(day: str):
    match day:
        case "Monday":
            print("Start of the week, time to work!")
        case "Friday":
            print("Almost weekend, finish strong!")
        case "Saturday" | "Sunday":
            print("Weekend! Time to relax!")
        case _:
            print("Just another day.")

# Example usage
day_activity("Monday")   # Output: Start of the week, time to work!
day_activity("Sunday")   # Output: Weekend! Time to relax!
day_activity("Wednesday")# Output: Just another day.
