def exception_handler(number1, number2, operator):
    try:
        int(number1)
    except:
        return "Error: Numbers must only contain digits."

    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."

    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."

    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."

    return ""


def arithmetic_arranger(problems, displayMode=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    start = True
    separation = " " * 4
    line1 = line2 = line3 = line4 = ""

    for prob in problems:
        separated_problem = prob.split()
        n1 = separated_problem[0]
        operator = separated_problem[1]
        operator_length = len(operator + ' ')
        n2 = separated_problem[2]

        exp = exception_handler(n1, n2, operator)
        if exp != "":
            return exp

        number1 = int(n1)        
        number2 = int(n2)   

        space = max(len(n1), len(n2))
        arithmetic_arragement_length = space + operator_length

        if start == True:
            # only first arragement
            line1 += n1.rjust(arithmetic_arragement_length)
            line2 += operator + ' ' + n2.rjust(space)
            line3 += '-' * (arithmetic_arragement_length)
            if displayMode == True:
                if operator == '+':
                    line4 += str(number1 + number2).rjust(arithmetic_arragement_length)
                else:
                    line4 += str(number1 - number2).rjust(arithmetic_arragement_length)
            start = False
        else:
            line1 += n1.rjust(space + 6) # is 6 because separation + operator_length
            line2 += operator.rjust(5) + ' ' + n2.rjust(space)
            line3 += separation + '-' * (arithmetic_arragement_length)
            if displayMode == True:
                # displayMode == True then make the operation
                if operator == '+':
                    line4 += separation + str(number1 + number2).rjust(arithmetic_arragement_length)
                else:
                    line4 += separation + str(number1 - number2).rjust(arithmetic_arragement_length)    

    if displayMode == True:
        # displayMode == True then return the result line (line4)
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

    return line1 + '\n' + line2 + '\n' + line3