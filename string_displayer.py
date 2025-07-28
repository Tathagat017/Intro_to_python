#%s formatting
name = "Tathagat"
age = 20
hobby = "Coding"

def display_info():
    print(f"Hello {name}, you are {age} years old and your hobby is {hobby}.")

def display_using_format():
    print("Hello {}, you are {} years old and your hobby is {}.".format(name, age, hobby))
    
def display_using_old_format():
    print("Hello %s, you are %d years old and your hobby is %s." % (name, age, hobby))