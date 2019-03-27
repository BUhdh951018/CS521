# One continuous string


def main():
    file = open("text.txt", "r")
    x_str = ''.join(file.readlines())
    cursor = 0
    print("Print initial file:")
    my_print(x_str, cursor)

    print("COMMAND MENU\ncmd_h cmd_i cmd_j cmd_k cmd_X cmd_D cmd_dd\n"
          "cmd_ddp cmd_n cmd_wq cmd_r cmd_t cmd_plus cmd_insert cmd_sub")
    i = 1

    while i == 1:
        command = input("Command:")
        if command == "cmd_h":
            cursor = cmd_h(cursor)
            my_print(x_str, cursor)
        elif command == "cmd_i":
            cursor = cmd_i(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_j":
            cursor = cmd_j(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_k":
            cursor = cmd_k(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_X":
            x_str, cursor = cmd_X(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_D":
            x_str = cmd_D(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_dd":
            x_str, cursor = cmd_dd(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_ddp":
            x_str = cmd_ddp(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_n":
            s_string = input("Please enter a string:")
            cursor = cmd_n(x_str, cursor, s_string)
            my_print(x_str, cursor)
        elif command == "cmd_wq":
            file1 = open("text.txt", "w")
            x_str = cmd_wq(x_str, cursor)
            file1.write(x_str)
            file1.close()
            print("It has been saved!")
        elif command == "cmd_r":
            r_string = input("Please enter a string:")
            cursor = cmd_r(x_str, cursor, r_string)
            my_print(x_str, cursor)
        elif command == "cmd_t":
            x_str = cmd_t(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_plus":
            cursor = cmd_plus(x_str, cursor)
            my_print(x_str, cursor)
        elif command == "cmd_insert":
            i_string = input("Please enter a string:")
            x_str = cmd_insert(x_str, cursor, i_string)
            my_print(x_str, cursor)
        elif command == "cmd_sub":
            r_string = input("Please enter a character:")
            x_str = cmd_sub(x_str, cursor, r_string)
            my_print(x_str, cursor)


# move cursor one character to the left
def cmd_h(cur):
    if cur > 0:
        return cur - 1
    else:
        return cur


# move cursor one character to the right
def cmd_i(x, cur):
    if cur < len(x):
        return cur + 1
    else:
        return cur


# move cursor vertically up one line
def cmd_j(x, cur):
    # find the previous "\n"
    left = x[:cur]
    re_left = left[::-1]
    temp_left = re_left.find("\n")

    if temp_left == -1:
        print("This is the first line!")
        return cur
    else:
        left_lines = x[:cur - temp_left]
        # calculate the length of the above line
        above_len = left_lines[::-1][1:].find("\n")
        # if the above line is the first line
        if above_len == -1:
            above_len = len(left_lines)
            return cur - above_len
        return cur - above_len - 1


# move cursor vertically down one line
def cmd_k(x, cur):
    # find the distance to the right of this line
    temp_right = x[cur:].find("\n")
    # find the distance to the left of this line
    left = x[:cur]
    re_left = left[::-1]
    temp_left = re_left.find("\n")

    if temp_right == -1:
        print("This is the last line!")
        return cur
    else:
        # if the cursor is on the first line
        if temp_left == -1:
            temp_left = len(re_left)
        return cur + temp_right + temp_left + 1


# delete the character to the left of the cursor
def cmd_X(x, cur):
    if cur < len(x):
        return x[:cur-1] + x[cur:], cur-1


# remove on current line from cursor to the end
def cmd_D(x, cur):
    temp_right = x[cur:].find("\n")
    return x[:cur] + x[cur+temp_right:]


# delete current line and move cursor to the beginning of next line
def cmd_dd(x, cur):
    temp_right = x[cur:].find("\n")
    if temp_right != -1:
        left = x[:cur]
        re_left = left[::-1]
        temp_left = re_left.find("\n")
        return x[:cur - 1 - temp_left] + x[cur + temp_right:], cur - temp_left
    else:
        temp_right = len(x[cur:])
        left = x[:cur]
        re_left = left[::-1]
        temp_left = re_left.find("\n")
        return x[:cur - temp_left] + x[cur + temp_right:], cur - temp_left


# transpose two adjacent lines
def cmd_ddp(x, cur):
    temp_right = x[cur:].find("\n")
    left = x[:cur]
    re_left = left[::-1]
    temp_left = re_left.find("\n")

    # cursor on the last line
    if temp_right == -1:
        print("Nothing to transpose!")
        return x

    # on the first line
    if temp_left == -1:
        current_line = x[:cur+temp_right+1]
        other_str = x[cur+temp_right+1:]
        temp_next = other_str.find("\n")

        next_line = other_str[:temp_next]
        rest_lines = x[cur+temp_right+temp_next+2:]

        return next_line + "\n" + current_line + rest_lines

    # on the middle lines
    else:
        left_lines = x[:cur - temp_left]
        current_line = x[cur-temp_left:cur+temp_right+1]
        other_str = x[cur + temp_right + 1:]
        temp_next = other_str.find("\n")
        if temp_next == -1:
            next_line = other_str[:]
            rest_lines = ""
        else:
            next_line = other_str[:temp_next]
            rest_lines = x[cur+temp_right+temp_next+2:]

        return left_lines + next_line + "\n" + current_line + rest_lines


# search for next occurrence of a string
def cmd_n(x, cur, str):
    cur = x.find(str, cur, len(x)-1)
    return cur


# write your representation as text file and save it
def cmd_wq(x, cur):
    return x[:cur] + "^" + x[cur:] + "\n"


# search backwards for next occurrence of a string
def cmd_r(x, cur, str):
    cur = x.rfind(str, 0, cur)
    return cur


# transpose two characters
def cmd_t(x, cur):
    if cur > 0:
        a = x[cur-1]
        b = x[cur]
        return x[:cur-1] + b + a + x[cur+1:]
    else:
        return x


# go to the beginning of next line
def cmd_plus(x, cur):
    temp_right = x[cur:].find("\n")
    if temp_right != -1:
        return cur + temp_right
    else:
        return cur


# insert a string at the cursor
def cmd_insert(x, cur, str):
    return x[:cur] + str + x[cur:]


# substitute replace the character at the cursor with another one
def cmd_sub(x, cur, str):
    return x[:cur] + str + x[cur+1:]


def my_print(x, cur):
    print(x[:cur] + "^" + x[cur:] + "\n")


if __name__ == '__main__':
    main()
