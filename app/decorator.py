from datetime import datetime
import json


def logger1(file_path):
    def logger(function):
        def wrapper(*args, **kwargs):
            data = []
            time_start = datetime.now()

            function(*args, **kwargs)

            func_name = function.__name__
            arguments = f'{args}, {kwargs}'
            result = function(*args, **kwargs)
            data.append(
                {
                    'Время вызова -': time_start,
                    'Имя функции -': func_name,
                    'Аргументы функции -': arguments,
                    'Результат -': result
                }
            )

            with open(file_path, 'a', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False, default=str)

            return result

        return wrapper

    return logger
