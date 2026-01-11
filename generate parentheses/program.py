# n=3
# ()()() ()(()) (())() ((())) (()()) 

# res = []
# stack = []

# backtracking fn:  
#   recursively go and add one parenthese at once
# if number of open p. = number of cl. p. = n: add to result
# if number of open p. > number of cl. p.: call fn w. +1 cl. p. 
# if number of open p. = number of cl. p.: call fn w. +1 op. p.


def generateParentheses(n: int) -> list[str]:
    #return []

    res = []
    stack = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        if openN > closedN:
            stack.append(")")
            backtrack(openN, closedN + 1)i
            stack.pop()                 # stack is global
        if openN == closedN:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()                 # stack is global

    backtrack(0,0)


print(generateParentheses(3))
