inFile = open('names.txt', 'r')

nameStr = f.readlines()[0]
nameStr = nameStr.replace(',', ' ')
nameStr = nameStr.replace("\"", '')
nameList = sorted(nameStr.split())

def nameScore(name):
    score = 0
    for c in name:
        score += getCharVal(c)
    position = 0
    for s in nameList:
        position += 1
        if s == name:
            break
    return score * position
    
print(sum([nameScore(s) for s in nameList]))

# Output: 871198282
