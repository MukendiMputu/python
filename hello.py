print("Hello, world!")

def greet():
    name = input("What's your name? ")

    print("Hi {x}! Nice to meet you,".format(name))
    answer = input("So {}, are you enjoying learning python? ".format(name))

    if answer:
        print("Awesome!")
    else:
        print("Oh ok. You should think about alternatives then!")

def say_hello(x):
    print("x ist {}".format(x))
    print(type(x))

numb = [1, 2, 3, 4, 5]

############# Loops ################
while False:
    print('Infinity')


############# End Loops ############

x = """
    Multi-line
    string
"""

if __name__ == '__main__' : say_hello(x)