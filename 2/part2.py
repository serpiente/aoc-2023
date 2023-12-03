from collections import defaultdict

with (open('./input.txt', 'r') as file):
    all = []
    for line in file:
        l = line.split(':')
        game_id = int(l[0].split(' ')[1].strip())
        games = l[1].strip().split(';')
        d = defaultdict(bool)
        mr, mb, mg = 0,0,0
        for game in games:
            for ball in game.split(','):
                n,c = ball.strip().split(' ')
                n = int(n)
                if c == 'red':
                    mr = max(mr, n)
                if c == 'blue':
                    mb = max(mb, n)
                if c == 'green':
                    mg = max(mg, n)
        all.append(mr*mb*mg)
    print(sum(all))