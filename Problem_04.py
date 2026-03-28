def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
    
    return fine


data = input().rsplit(" ", 2)

book_title = data[0]
days_overdue = int(data[1])
daily_rate = float(data[2])

fine = calculate_fine(book_title, days_overdue, daily_rate)

print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")
