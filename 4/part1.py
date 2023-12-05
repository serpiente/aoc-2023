with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    scores = []
    for line in lines:
        gameid, numbers = line.split(':')
        hand, winning = numbers.split('|')
        hand =set([h for h in hand.split(' ') if h != ''])
        winning = set([w for w in winning.split(' ') if w != ''])

        score = None
        for number in hand:
            if number in winning:
                if not score:
                    score = 1
                else:
                    score *= 2

        if score:
            scores.append(score)

    print(sum(scores))