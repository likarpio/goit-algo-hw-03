import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.datetime.today().date()
        result = current_date - date_obj
        return result.days
    except ValueError:
        return "Неправильний формат дати"
