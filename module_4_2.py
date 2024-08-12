def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    print(locals())

    inner_function()

    return "ОК"


#result1 = inner_function() # - NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                            #  не находит функцию inner_function() в глобальном пространстве т.к -
                            #  она в локальном простанстве -  test_function
result2 = test_function()
print(result2)
