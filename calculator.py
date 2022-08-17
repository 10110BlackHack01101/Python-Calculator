import time
import sys
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')
    
def calc():
    first = input("First: ")
    if first == " ":
        delete_last_line()
        print("An error has occured. Diagnosing...")
        delete_last_line()
        time.sleep(3)
        print("An input box was left blank. Please rerun the program.")
    elif first == "":
        delete_last_line()
        print("An error has occured. Diagnosing...")
        delete_last_line()
        time.sleep(3)
        print("An input box was left blank. Please rerun the program.")        
    else:
        second = input("Second: ")
        if second == " ":
            delete_last_line()
            print("An error has occured. Diagnosing...")
            delete_last_line()            
            time.sleep(3)
            print("An input box was left blank. Please rerun the program.")
        elif second == "":
            delete_last_line()
            print("An error has occured. Diagnosing...")
            delete_last_line()
            time.sleep(3)
            print("An input box was left blank. Please rerun the program.")
        else:
            answer = float(first) + float(second)
            print("Calculating.")
            delete_last_line()
            time.sleep(1)
            print("Calculating..")
            delete_last_line()
            time.sleep(1)
            print("Calculating...")
            delete_last_line()
            time.sleep(1)
            print("Calculating.")
            delete_last_line()
            time.sleep(1)
            print("Calculating..")
            delete_last_line()
            time.sleep(1)
            print("Calculating...")
            delete_last_line()
            time.sleep(1)
            print("Answer is: " + str(answer))
skip = input("Welcome to Python-Calculator. Enter to continue. Y and enter to skip rules.")
if skip == "Y":
    delete_last_line()
    calc()
elif skip == "y":
    delete_last_line()
    calc()
else:
    delete_last_line()
    input("To use subtraction insert a - at the beginning of your second number. Enter to continue")
    delete_last_line()
    input("Addition is the default operator. Therefore there is no need to use an +. Enter to continue")
    delete_last_line()
    input("Currently multiplication and division are not supported. Enter to begin")
    delete_last_line()
    calc()
