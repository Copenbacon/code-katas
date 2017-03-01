"""The sort cards kata from CodeWars."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """
    cards = sorted(list(cards))
    acount = cards.count('A')
    tcount = cards.count('T')
    jcount = cards.count('J')
    qcount = cards.count('Q')
    kcount = cards.count('K')
    for numa in range(acount):
        cards.remove('A')
    for numa in range(acount):
        cards.insert(0, 'A')
    for numt in range(tcount):
        cards.remove('T')
    for numt in range(tcount):
        cards.insert(len(cards), 'T')
    for numj in range(jcount):
        cards.remove('J')
    for numj in range(jcount):
        cards.insert(len(cards), 'J')
    for numq in range(qcount):
        cards.remove('Q')
    for numq in range(qcount):
        cards.insert(len(cards), 'Q')
    for numk in range(kcount):
        cards.remove('K')
    for numk in range(kcount):
        cards.insert(len(cards), 'K')
    return cards
