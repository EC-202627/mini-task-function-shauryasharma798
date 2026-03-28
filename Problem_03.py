def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
    
    return fine


data = input().rsplit(" ", 1)

book_title = data[0]
days_overdue = int(data[1])

fine = calculate_fine(book_title, days_overdue)

print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")

if fine == 150.0:
    print("You have accumulated the maximum fine of INR: 150.0")
