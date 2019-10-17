

def check_if_correct(phrase):
    """check if a phrase is correct in respect to parenthesis openings and closings"""
    ends_to_expect = 0
    for letter in phrase:
        if letter is '(':
            ends_to_expect += 1
        elif letter is ')' and ends_to_expect == 0:
            return False
        elif letter is ')' and ends_to_expect > 0:
            ends_to_expect -= 1

    if ends_to_expect is 0:
        return True
    else:
        return False


print(check_if_correct(')(  () ('))
print(check_if_correct('()(())(()())'))
print(check_if_correct('((('))



