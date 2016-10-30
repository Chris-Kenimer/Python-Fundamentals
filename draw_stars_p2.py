x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars(x):

    if type(value) is str:
        s = ''
        x = len(value)
        while x > 0:
            s += value.lower()[:1]
            x -= 1
        print s
    else:
        s = ''
        while x > 0:
            s += '*'
            x -= 1
        print s
for value in x:
    draw_stars(value)
