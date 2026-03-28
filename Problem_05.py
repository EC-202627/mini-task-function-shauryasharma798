def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


book_title = input()
days_overdue = int(input())
daily_rate = float(input())
max_fine = float(input())

fine = calculate_fine(book_title, days_overdue, daily_rate, max_fine)

print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")

if fine == max_fine:
    print(f"You have accumulated the maximum fine of INR: {max_fine}")
