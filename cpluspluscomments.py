

def print_comments():
    """check if a phrase is correct in respect to parenthesis openings and closings"""
    with open('a_cpp_file.cpp', 'r') as file:
        data = file.read()
    to_print = ''
    should_print = False
    for i, char in enumerate(data):
        if i > 1:
            if data[i-1] == '*' and data[i-2] == '/':
                should_print = True
            if char == '*' and data[i+1] == '/' and should_print:
                should_print = False
                print(to_print)
                to_print = ''
            if should_print:
                to_print += char
    should_print = False
    for i, char in enumerate(data):
        if i > 1:
            if data[i-1] == '/' and data[i-2] == '/':
                should_print = True
            if char == '\n' and should_print:
                should_print = False
                print(to_print)
                to_print = ''
            if should_print:
                to_print += char


print_comments()

