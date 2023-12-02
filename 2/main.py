from collections import defaultdict

with (open('./input.txt', 'r') as file):
    all = []
    for line in file:
        l = line.split(':')
        game_id = int(l[0].split(' ')[1].strip())
        all.append(game_id)
        games = l[1].strip().split(';')
        d = defaultdict(bool)
        for game in games:
            for ball in game.split(','):
                n,c = ball.strip().split(' ')
                n = int(n)
                if (c=='red' and n > 12) or (c=='blue' and n > 14) or (c=='green' and n > 13):
                    if game_id in all:
                        all.remove(game_id)
    print(sum(all))