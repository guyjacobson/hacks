text = '''
c	o	o	t	i	h	n	h	a
r	n	n	e	p	d	t	u	r
c	o	r	i	l	a	o	a	r
i	e	w	n	n	e	h	w	l
g	n	y	u	q	g	i	a	s
o	i	s	d	e	u	e	r	i
i	u	r	s	o	e	s	v	a
u	n	h	d	h	i	s	o	e
a	i	d	t	i	a	n	i	c
i	v	d	e	a	r	l	t	a
n	i	e	c	n	g	o	m	e
f	y	o	a	o	d	e	v	e
r	i	u	i	i	n	m	n	e
b	a	n	g	s	n	n	t	s
i	i	h	s	d	d	a	n	e
e	s	l	t	t	t	r	m	e
i	n	h	a	b	a	e	c	e
e	w	o	r	r	k	o	r	b
a	d	r	w	t	w	n	r	o
t	s	b	y	l	w	h	a	d
r	t	f	i	e	l	e	o	i
s	a	n	v	t	o	r	r	e
'''

lines = [x.split('\t') for x in text.split('\n')[1:-1]]

strands = [[x[n:n+3] for x in lines] for n in range(0, 9, 3)]   # Split into list of lists of lists

seq = ['L', 'L', 'H', 'R', 'R', 'H']       # Sequence of where a strand appears in a braid; Left, Right, or Hidden


# Do the braiding and return a list of pairs that appear (braidout) and the hiddens
def braid(st):
    braidout = []
    hidden = ''
    for n, trio in enumerate(st):
        showing = ''
        for j in range(3):
            letter = trio[j]
            state = seq[(n + 2 * j) % 6]   # Magic formula giving the state of one strand
            if state == 'L':
                showing = letter + showing
            elif state == 'R':
                showing = showing + letter
            else:
                hidden += letter
        braidout.append(showing)
    return braidout, hidden


bos = [[], [], []]

for i in range(3):
    bo, h = braid(strands[i])
    print(f'Message: didyouknow{"".join(bo)}\nHidden: {h}\n')
    bos[i] = bo

startrow = 16    # Row 17, except Python is 0-based

restrand = [[bos[j][i] for j in range(3)] for i in range(startrow, len(lines))]  # Transpose bos and start at startrow

# Braid the braids
bo, h = braid(restrand)
print(f'Message: {"".join(bo)}\nHidden: {h}\n')
