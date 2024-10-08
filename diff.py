import difflib


def diff_substrings(str1, str2):
    added, removed = get_diff_substrings(str1, str2)
    return display(added, removed)


def get_diff_substrings(str1, str2):
    diff = difflib.ndiff(str2, str1)  # Get character differences
    added = []
    removed = []

    temp_add = []
    temp_rem = []

    for char in diff:
        # Track added characters (present in str2 but not in str1)
        if char.startswith('+ '):
            temp_add.append(char[2])
        elif temp_add:
            added.append(''.join(temp_add))
            temp_add = []

        # Track removed characters (present in str1 but not in str2)
        if char.startswith('- '):
            temp_rem.append(char[2])
        elif temp_rem:
            removed.append(''.join(temp_rem))
            temp_rem = []

    # Append remaining collected substrings
    if temp_add:
        added.append(''.join(temp_add))
    if temp_rem:
        removed.append(''.join(temp_rem))

    return added, removed


def display(removed, added):
    if added == [] and removed == []:
        return ''
    elif added != [] and removed != []:
        return f"{display1(removed)} → {display1(added)}"
    elif removed != []:
        return f"⊖{display1(removed)}"
    elif added != []:
        return f"⊕{display1(added)}"


def display1(item):
    if len(item) == 1:
        s = item[0]
        return f"'{s}'" if s and ' ' == s else s
    else:
        return '|'.join([f"'{s}'" if s and ' ' == s else s for s in item])


def main():
    examples = (
        ("abcdefg", "abxefyz"),
        ("abcdefg", "abcdefg"),

        ('you', 'ou'),
        ('ou', 'you'),
        ('you', 'wou'),

        ('you', 'yu'),
        ('yu', 'you'),

        ('you', 'yo'),
        ('yo', 'you'),

        ('you', 'yau'),
        ('you', 'yow'),
        ('you', 'ou'),
        ('ou', 'you'),
        ('you', 'wou'),

        (':-(and :-)', ':-( and :-)'),
        ("is anybody here", "is anybady here"),
        ("do you smoke", "do you smake"),
        ("do you smoke", "do yu smake"),
        ("do you smoke", "do you smoke"),
        (':-(and :-) are emoticons', ':-( and :-) are emoticons'),
        ("If we could see far into the future, …", "If we could see far into the future"),
        ("I've had plenty, thanks (`plenty´ is nonstandard).", "(`plenty´ is nonstandard) I've had plenty, thanks"),
        ("If you ever get married, which seems to be extremely problematic, …", "If you ever get married, which seems to be extremely problematic"),
        ("The men cased the house.", "The men cased the housed"),
        ("Thou art careful and troubled about many things.", ";Thou art careful and troubled about many things"),
        ("as the saying goes, …", "as the saying goes …"),
        ("a social gossip column", "a social gossip colum"),
        ("If I had my way, …", "if I had my way"),
        ("Consider the following, just as a hypothetical possibility.", "Consider the following, just as a hypothetical"),
        ("as they say in the trade, … ", "as they say in the trade"),
        (".", "The patriciate regarded patronage of the arts as a moral and social duty.."),
    )
    for pair in examples:
        str1 = pair[0]
        str2 = pair[1]
        added, removed = get_diff_substrings(str1, str2)
        print(f"{str1}/{str2}= ⊖{removed} ⊕{added}")
        print(f"{str1}/{str2}= {display(removed, added)}\n")


if __name__ == '__main__':
    main()
