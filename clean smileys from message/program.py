# "Hello! :-) Weather is bad :-("

# ":-)"

def cleanMsgFromSmileys(msg: str) -> str:
    res = ""
    smileLen = 3     # smiles: ":-)" ":-("
    i = 0
    while (i < len(msg)):
        c = msg[i]
        # check for smiley. if yes, forward to end of smiley sequence
        if i+2 < len(msg) and c == ":" and msg[i+1] == "-" and (msg[i+2] == ")" or msg[i+2] == "("):
            cntAdd = 0 # additional braces count
            brace = msg[i+2]
            j = i+2
            while j+1 < len(msg) and msg[j+1] == brace:
                cntAdd += 1
                j += 1
            i += smileLen + cntAdd
        else:
            res += c
            i += 1
    return res


inputs = [ ":-)", "Hello! :-) :-))) Weather is bad :-(((" ]
for text in inputs:
    print(cleanMsgFromSmileys(text))

