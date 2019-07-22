""" 1.3 URLify: Write a method to replace all spaces in a string with '%20'."""

string = 'ab c'
def urlify(string):
    counter = 0
    for i in string:
        counter += 1
        if i == ' ':
            s2 = string[:counter-1] + '%20' + string[counter:]
    print(s2)

urlify(string)
