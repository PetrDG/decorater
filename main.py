from datetime import datetime
import requests


def get_log(func):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('logs.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата/время: {str_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Возвращеное значение: {result}\n')
        return result
    return foo


@get_log
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code

@get_log
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


if __name__ == '__main__':
    get_status('https://habr.com/ru/')
