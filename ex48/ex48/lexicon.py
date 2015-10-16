def scan(s):
    lexicon = {
               'direction': ['north', 'south', 'east', 'west'],
               'verb': ['eat', 'go', 'kill'],
               'stop': ['the', 'in', 'of'],
               'noun': ['princess', 'bear']
               }

    s_list = s.split(' ')

    ret = []
    for word in s_list:
        appended = False
        for key in lexicon:
            if word.lower() in lexicon[key]:
                ret.append((key, word.lower()))
                appended = True
                break
        if appended:
            continue
        else:
            try:
                ret.append(('number', int(word)))
            except:
                ret.append(('error', word))
    return ret


