def count_substring(string, sub_string):
    sub_step = len(sub_string);
    sub_counter = 0; 
    for check in range(len(string)):
        if string[check:sub_step+check] == sub_string:
            sub_counter = sub_counter + 1;
    return sub_counter;

if __name__ == '__main__':
