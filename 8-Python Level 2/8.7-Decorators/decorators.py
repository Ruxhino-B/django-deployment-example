# def hello(name = 'ruxhino'):
#     return 'hello ' + name
# print(hello())
# newhello = hello
# print(newhello())


# def hello(name = 'Ruxhino'):
#     print("The hello function has been run!")
#     def greet():
#         return "This string is inside Greet()"
#     def wellcome():
#         return "This string is inside wellcome"
#     print(greet())
#     wellcome()
# hello()

def new_decorator(func):
    def wrap_func():
        print("Code here before executing func")
        func()
        print('func() has been called')
    return wrap_func
@new_decorator
def func_need_decotator():
    print('this func is in need of a decorator!')
#func_need_decotator = new_decorator(func_need_decotator) = @new_decorator
func_need_decotator()
