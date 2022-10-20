from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Функция работает не правильно!')

if capitalize('') != '':
    raise Exception('Функция работает не правильно!')


print('Все тесты пройдены!')