def mutate_string(string, position, character):
    change = list(string);
    change[position] = character;
    string = ''.join(change);
    return string;

if __name__ == '__main__':
