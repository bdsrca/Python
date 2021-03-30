def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    # Your code here
    # part create a dict
    dicts = {}
    if len(map_from) != len(map_to):
        return
    if code == "":
        return
    #for loop to assign the dicts
    # loop code, translate
    for i in range(len(map_from)):
        key = map_from[i]
        values = map_to[i]
        dicts[key] = values
    # for loop to do the translate
    values = ""
    for j in code:
        a = dicts[j]
        values += a

    #return tuple
    result = (dicts,values)
    return result

print(cipher("abcd", "dca", "dab"))