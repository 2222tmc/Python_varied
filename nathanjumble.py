# Cambridge study got me interested in this :)
# cnduo't
# you?
# period.
# hey!
# comma,
# end: of; 'inside' "stuff"

# ignored_symbols = [':',';','.',"'",'?','!','"']
# for symbol in ignored_symbols:
#     if w.endswith(symbol):
#         # special handling
#         pass

import random

def jumbledup(phrase):
    words = phrase.split()
    nwords = []
    for w in words:
        nwords.append(jumble_word(w))
    return ' '.join(nwords)

### helper function
##def jumble_word(w):
##    if len(w) > 3:
##        nw = w[0]
##        end = len(w) - 1
##        indexes = range(1,end)
##        for j in range(1,end):
##            i = random.choice(indexes)
##            nw += w[i]
##            indexes.remove(i)
##        nw += w[end]
##        return nw
##    else:
##        return w
        

if __name__ == '__main__':
    a = "Every morning Claire has her morning nursing session"
    b = "An overwhelming rush of thankfulness pushed through my being"
    print jumbledup(a)
    
    
