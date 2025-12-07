# Message: "Hello! :-)) Weather is bad :-(" -> need to get rid of smiles
# Base smiles: ":-)" ":-(" Variants ":-))" ":-(((" etc. (arbitrary number of braces)

def cleanMsgFromSmileys(msg: str) -> str:
    res = ""
    prefix = ":-" 
    endings = { ")", "(" } 
    MIN_LEN = len(prefix) + 1
    i = 0
    while (i < len(msg)):
        c = msg[i]
        brace_ix = i + MIN_LEN - 1
        # check for smiley. if found, forward to end of smiley sequence
        if (brace_ix  < len(msg) 
            and msg[i : brace_ix] == prefix 
            and msg[brace_ix] in endings):
            i += MIN_LEN
            # advance to the last brace 
            while i < len(msg) and msg[i] == msg[brace_ix]:
                i += 1
        else:
            res += c
            i += 1
    return res

inputs = [ ":-)", "Hello! :-) :-))) Weather is bad :-(((", ":-", ":-|" ]
for text in inputs:
    print(cleanMsgFromSmileys(text))

