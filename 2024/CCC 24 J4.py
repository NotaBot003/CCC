og = input()
new = input()
wletter = 0
wrongletterlist = []
diff = len(og) - len(new)

if len(og) == len(new):
    for i in range(len(og)):
        if og[i] != new[i] and og[i] != new[i]:
            silly1 = og[i]
            silly2 = new[i]
    print(silly1, silly2)
    print('-')
else:
    silly2 = []
    og = og + 'X' * 8
    new = new + 'X' * (8 + diff)
    oga = og.count('a')
    newa = og.count('a')
    ogb = og.count('b')
    newb = og.count('b')
    ogc = og.count('c')
    newc = og.count('c')
    ogd = og.count('d')
    newd = og.count('d')
    oge = og.count('e')
    newe = og.count('e')
    ogf = og.count('f')
    newf = og.count('f')
    ogg = og.count('g')
    newg = og.count('g')
    ogh = og.count('h')
    newh = og.count('h')
    ogi = og.count('i')
    newi = og.count('i')
    ogj = og.count('j')
    newj = og.count('j')
    ogk = og.count('k')
    newk = og.count('k')
    ogl = og.count('l')
    newl = og.count('l')
    ogm = og.count('m')
    newm = og.count('m')
    ogo = og.count('o')
    newo = og.count('o')
    ogp = og.count('p')
    newp = og.count('p')
    ogq = og.count('q')
    newq = og.count('q')
    ogr = og.count('r')
    newr = og.count('r')
    ogs = og.count('s')
    news = og.count('s')
    ogt = og.count('t')
    newt = og.count('t')
    ogu = og.count('u')
    newu = og.count('u')
    ogv = og.count('v')
    newv = og.count('v')
    ogw = og.count('w')
    neww = og.count('w')
    ogx = og.count('x')
    newx = og.count('x')
    ogy = og.count('y')
    newy = og.count('y')
    ogz = og.count('z')
    newz = og.count('z')
    if og.count('a') > new.count('a'):
        wrongletterlist.append('a')
    elif og.count('b') > new.count('b'):
        wrongletterlist.append('b')
    elif og.count('c') > new.count('c'):
        wrongletterlist.append('c')
    elif og.count('d') > new.count('d'):
        wrongletterlist.append('d')
    elif og.count('e') > new.count('e'):
        wrongletterlist.append('e')
    elif og.count('f') > new.count('f'):
        wrongletterlist.append('f')
    elif og.count('g') > new.count('g'):
        wrongletterlist.append('g')
    elif og.count('h') > new.count('h'):
        wrongletterlist.append('h')
    elif og.count('i') > new.count('i'):
        wrongletterlist.append('i')
    elif og.count('j') > new.count('j'):
        wrongletterlist.append('j')
    elif og.count('k') > new.count('k'):
        wrongletterlist.append('k')
    elif og.count('l') > new.count('l'):
        wrongletterlist.append('l')
    elif og.count('m') > new.count('m'):
        wrongletterlist.append('m')
    elif og.count('o') > new.count('o'):
        wrongletterlist.append('o')
    elif og.count('p') > new.count('p'):
        wrongletterlist.append('p')
    elif og.count('q') > new.count('q'):
        wrongletterlist.append('q')
    elif og.count('r') > new.count('r'):
        wrongletterlist.append('r')
    elif og.count('s') > new.count('s'):
        wrongletterlist.append('s')
    elif og.count('t') > new.count('t'):
        wrongletterlist.append('t')
    elif og.count('u') > new.count('u'):
        wrongletterlist.append('u')
    elif og.count('v') > new.count('v'):
        wrongletterlist.append('v')
    elif og.count('w') > new.count('w'):
        wrongletterlist.append('w')
    elif og.count('x') > new.count('x'):
        wrongletterlist.append('x')
    elif og.count('y') > new.count('y'):
        wrongletterlist.append('y')
    elif og.count('z') > new.count('z'):
        wrongletterlist.append('z')
    elif og.count('n') > new.count('n'):
        wrongletterlist.append('n')
    if og.count('a') < new.count('a'):
        silly2.append('a')
    elif og.count('b') < new.count('b'):
        silly2.append('b')
    elif og.count('c') < new.count('c'):
        silly2.append('c')
    elif og.count('d') < new.count('d'):
        silly2.append('d')
    elif og.count('e') < new.count('e'):
        silly2.append('e')
    elif og.count('f') < new.count('f'):
        silly2.append('f')
    elif og.count('g') < new.count('g'):
        silly2.append('g')
    elif og.count('h') < new.count('h'):
        silly2.append('h')
    elif og.count('i') < new.count('i'):
        silly2.append('i')
    elif og.count('j') < new.count('j'):
        silly2.append('j')
    elif og.count('k') < new.count('k'):
        silly2.append('k')
    elif og.count('l') < new.count('l'):
        silly2.append('l')
    elif og.count('m') < new.count('m'):
        silly2.append('m')
    elif og.count('o') < new.count('o'):
        silly2.append('o')
    elif og.count('p') < new.count('p'):
        silly2.append('p')
    elif og.count('q') < new.count('q'):
        silly2.append('q')
    elif og.count('r') < new.count('r'):
        silly2.append('r')
    elif og.count('s') < new.count('s'):
        silly2.append('s')
    elif og.count('t') < new.count('t'):
        silly2.append('t')
    elif og.count('u') < new.count('u'):
        silly2.append('u')
    elif og.count('v') < new.count('v'):
        silly2.append('v')
    elif og.count('w') < new.count('w'):
        silly2.append('w')
    elif og.count('x') < new.count('x'):
        silly2.append('x')
    elif og.count('y') < new.count('y'):
        silly2.append('y')
    elif og.count('z') < new.count('z'):
        silly2.append('z')
    elif og.count('n') < new.count('n'):
        silly2.append('n')



