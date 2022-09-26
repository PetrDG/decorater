from datetime import datetime
import requests


def log_decorator(path):
    def get_log(func):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open('logs2.txt', 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {str_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Возвращеное значение: {result}\n')
            return result
        return foo
    return get_log


@log_decorator('D:\project python\Decoration')
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://habr.com/ru/all/')