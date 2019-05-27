import string

def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    for i in range(size-1,0,-1):
        right_string = ['-' + alphabet[s] for s in range(0,i)]
        left_string = right_string[:0:-1]
        porcoddio = left_string  + right_string
        print(''.join(porcoddio))

if __name__ == '__main__':
    n = 10
    print_rangoli(n)

