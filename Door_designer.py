import math

def door_build(c, r):
    row=[]
    b = math.ceil(r/2 - 1)

    for i in range(0, math.ceil(r/2)):
        if i==b:
            row.append(''.join(central_row(c)))
        else:
            row.append(''.join(build_row(i, c)))
    x = row[0:b]
    x.reverse()
    for z in x:
        row.append(z)
    for e in row:
        print(e)

def central_row(n):
    x = int(n/2)
    row = ['-'] * (x - 3)
    row.append('WELCOME')
    row = row + ['-'] * (x-3)
    return row

def build_row(rownumber, n):
    x = int(n / 2)
    row = ['-'] * (x - rownumber*3-1)
    row=row+['.|.']
    row=row+['.|.']*int(rownumber)*2
    row = row + ['-'] * (x - rownumber*3-1)
    return row


if __name__ == '__main__':
    print('Dammi la grandezza della porta: ')
    n=int(input())
    m=n*3
    x = int(m)
    door_build(m, n)

