import string

def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    down_part = []
    up_part = []
    count = 0
    for i in range(size, 0, -1):
        right_string = [alphabet[s] for s in range(count, size)]

        full = (((size - i) * 2) - 1) * '-'
        right_string.append(full)

        left_string = right_string[:0:-1]
        complete_string = left_string + right_string

        down = '-'.join(complete_string)
        if size == i:
            down = down[1:-1]

        down_part.append(down)
        count = count + 1
    up_part = down_part[::-1]
    print("\n".join(up_part))

    print("\n".join(down_part[1:]))


if __name__ == '__main__':
    n = 10
    print_rangoli(n)

