# List of strings where each string represents a line


def main():
    file = open("text.txt", "r")
    x_str = file.readlines()
    line, cursor = 0, 0
    print("Print initial file:")
    my_print(x_str, line, cursor)

    print("COMMAND MENU\ncmd_h cmd_i cmd_j cmd_k cmd_X cmd_D cmd_dd cmd_ddp cmd_n cmd_wq")
    i = 1

    while i == 1:
        command = input("Command:")
        if command == "cmd_h":
            line, cursor = cmd_h(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_i":
            line, cursor = cmd_i(x_str, line, cursor)
            my_print(x_str, line,  cursor)
        elif command == "cmd_j":
            line = cmd_j(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_k":
            line = cmd_k(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_X":
            x_str, cursor = cmd_X(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_D":
            x_str = cmd_D(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_dd":
            x_str, cursor = cmd_dd(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_ddp":
            x_str = cmd_ddp(x_str, line, cursor)
            my_print(x_str, line, cursor)
        elif command == "cmd_n":
            s_string = input("Please enter a string:")
            line, cursor = cmd_n(x_str, line, cursor, s_string)
            my_print(x_str, line, cursor)
        elif command == "cmd_wq":
            file1 = open("text.txt", "w")
            x_str = cmd_wq(x_str, line, cursor)
            file1.write(x_str)
            file1.close()
            print("It has been saved!")


def my_print(x, line, cur):
    left_str = ''.join(x[:line])
    mid_str = x[line][:cur] + '^' + x[line][cur:]
    right_str = ''.join(x[line+1:])
    print(left_str + mid_str + right_str + '\n')


# move cursor one character to the left
def cmd_h(x, line, cur):
    if cur > 0:
        return line, cur - 1
    else:
        if line == 0:
            return line, cur
        else:
            line = line - 1
            cur = len(x[line]) - 1
            return line, cur


# move cursor one character to the right
def cmd_i(x, line, cur):
    if cur < len(x[line])-1:
        return line, cur + 1
    else:
        if line == 3:
            return line, cur
        else:
            line = line + 1
            cur = 0
            return line, cur


# move cursor vertically up one line
def cmd_j(x, line, cur):
    if line == 0:
        print("This is the first line!")
        return line
    else:
        return line-1


# move cursor vertically down one line
def cmd_k(x, line, cur):

    if line == len(x)-1:
        print("This is the last line!")
        return line
    else:
        return line+1


# delete the character to the left of the cursor
def cmd_X(x, line, cur):
    if cur > 0:
        left_list = x[:line]
        current = x[line][cur:]
        right_list = x[line+1:]
        return left_list + [current] + right_list, cur-1


# remove on current line from cursor to the end
def cmd_D(x, line, cur):
    left_list = x[:line]
    current = x[line][:cur] + '\n'
    right_list = x[line+1:]
    return left_list + [current] + right_list


# delete current line and move cursor to the beginning of next line
def cmd_dd(x, line, cur):
    left_list = x[:line]
    right_list = x[line+1:]
    temp_len = len(x[line][:cur])
    return left_list + right_list, cur-temp_len


# transpose two adjacent lines
def cmd_ddp(x, line, cur):
    if line == len(x)-1:
        print("This is the last line!")
    else:
        left_list = x[:line]
        current = x[line+1]
        next = x[line]
        right_list = x[line+2:]
        return left_list + [current] + [next] + right_list


# search for next occurrence of a string
def cmd_n(x, line, cur, str):
    for i in range(line, len(x)-1):
        current = x[i]
        if current.find(str, cur, len(x[i])) != -1:
            return i, current.find(str, cur, len(x[i]))
        else:
            cur = 0
    return line, cur


# write your representation as text file and save it
def cmd_wq(x, line, cur):
    left_str = ''.join(x[:line])
    mid_str = x[line][:cur] + '^' + x[line][cur:]
    right_str = ''.join(x[line + 1:])
    return left_str + mid_str + right_str + '\n'


if __name__ == '__main__':
    main()
