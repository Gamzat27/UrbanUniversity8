


def test_function():

    def inner_function(a):
        print(a)
        return a

    inner_function(a = 'Я в области видимости функции test_function. ')   # Не возвращает ничего

#inner_function(a='Я в области видимости функции test_function ') - Выдает ошибку, если вызвать таким образом.
test_function()    # Возвращает значение функции  inner_function




