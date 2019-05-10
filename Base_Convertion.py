def print_formatted(number):
    number_len = len(str(bin(number))) - 2
    for n in range(1, number + 1):
        n_hex = str(hex(n))[2:]
        n_oct = str(oct(n))[2:]
        n_bin = str(bin(n))[2:]
        n_spaces = ' ' * (number_len - (len(str(n))))
        oct_spaces = ' ' * (number_len - (len(n_oct) - 1))
        hex_spaces = ' ' * (number_len - (len(n_hex)-1))
        bin_spaces = ' ' * (number_len - (len(n_bin) - 1))
        n_string = n_spaces + str(n) + oct_spaces + str(n_oct) + hex_spaces + str(n_hex).upper() + bin_spaces + str(n_bin)
        print(n_string)

if __name__ == '__main__':
    n=63
    print_formatted(n)
