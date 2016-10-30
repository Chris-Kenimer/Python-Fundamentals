x = [4,6,1,3,5,7,25]

def draw_stars(x):
    s = ''
    while x > 0:
        s += '*'
        x -= 1
    print s
for count in x:
    draw_stars(count)
