class Person:
    def __init__(self, name, index, prefs, isMatched=False, currentMatch=None, proposes=0):
        self.name = name
        self.index = index
        self.prefs = prefs
        self.isMatched = isMatched
        self.currentMatch = currentMatch
        self.proposes = proposes


people = ["Ross", "Monica", "Chandler", "Phoebe", "Joey", "Rachel"]
prefs = [(6, 4, 2), (3, 5, 1), (2, 6, 4), (5, 1, 3), (6, 4, 2), (1, 5, 3)]

freeMen = [Person("Ross", 1, [3, 2, 1]), Person("Chandler", 2, [1, 3, 2]), Person("Joey", 3, [3, 2, 1])]
Women = [Person("Monica", 1, [2, 3, 1]), Person("Phoebe", 2, [3, 1, 2]), Person("Rachel", 3, [1, 3, 2])]
Men = [Person("Ross", 1, [3, 2, 1]), Person("Chandler", 2, [1, 3, 2]), Person("Joey", 3, [3, 2, 1])]


m = freeMen[0].prefs
m.pop(0)
print(m)
i = 0
counter = 0

while len(freeMen) > 0:

    print(counter)
    m = freeMen[0]
    print("m.prefs", m.prefs)
    w = Women[m.prefs[0] - 1]
    counter = counter + 1

    if not w.isMatched:
        w.isMatched = True
        m.isMatched = True
        m.currentMatch = w
        w.currentMatch = m
        m.prefs.pop(0)
    else:
        # hvis hun er matched, så skal vi se om m er bedre
        WcurrentMatchIndex = w.currentMatch.index
        Wprefs = w.prefs
        if Wprefs.index(WcurrentMatchIndex) < w.prefs.index(m.index):
            m.prefs.pop(0)
            continue
        else:
            freeMen.pop(0)
            freeMen.append(w.currentMatch)
            w.isMatched = True
            m.isMatched = True
            m.currentMatch = w
            w.currentMatch = m
            m.prefs.pop(0)
    i = i + 1
