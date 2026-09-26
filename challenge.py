#Factorial calculator - takes one input (integer) and returns that number's factorial.

def facto(numb):
    try:
        if numb == 0:
            return 1
        elif numb > 0:
            initial = numb
            while numb > 1:
                numb -= 1
                initial = initial * numb
            return initial
        else:
            return "Cannot factorialize negative numbers."
    except TypeError:
        return "Bad data type, please enter a whole number."