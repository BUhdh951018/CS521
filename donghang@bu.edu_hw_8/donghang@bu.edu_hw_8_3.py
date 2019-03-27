# each line in a separate node with n_ptr pointing to the node with the next line,
# p_ptr pointing to the node with a previous line.
data = 0
n_ptr = 1
p_ptr = 2


def main():
    cursor = 0
    line = 0
    file = open("text.txt", "r")
    x_str = file.readlines()
    start, end = double_link(x_str)
    line = start
    print("Print initial file:")
    my_print(start, line, cursor)

    print("COMMAND MENU\ncmd_h cmd_i cmd_j cmd_k cmd_X cmd_D cmd_dd\n"
          "cmd_ddp cmd_n cmd_wq cmd_r cmd_t cmd_plus cmd_insert cmd_sub")
    i = 1
    while i == 1:
        command = input("Command:")
        if command == "cmd_h":
            line, cursor = cmd_h(line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_i":
            line, cursor = cmd_i(end, line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_j":
            line, cursor = cmd_j(start, line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_k":
            line, cursor = cmd_k(end, line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_X":
            line, cursor = cmd_X(line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_D":
            line = cmd_D(line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_dd":
            start, line, cursor = cmd_dd(start, end, line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_ddp":
            start, line, end = cmd_ddp(start, end, line)
            my_print(start, line, cursor)
        elif command == "cmd_n":
            n_string = input("Please enter a string:")
            line, cursor = cmd_n(line, cursor, n_string)
            my_print(start, line, cursor)
        elif command == "cmd_wq":
            file1 = open("text.txt", "w")
            x_str = cmd_wq(start, line, cursor)
            file1.write(x_str)
            file1.close()
            print("It has been saved!")
        elif command == "cmd_r":
            r_string = input("Please enter a string:")
            line, cursor = cmd_r(line, cursor, r_string)
            my_print(start, line, cursor)
        elif command == "cmd_t":
            line = cmd_t(start, line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_plus":
            line, cursor = cmd_plus(end, line, cursor)
            my_print(start, line, cursor)
        elif command == "cmd_insert":
            i_string = input("Please enter a string:")
            line = cmd_insert(line, cursor, i_string)
            my_print(start, line, cursor)
        elif command == "cmd_sub":
            s_string = input("Please enter a character:")
            line = cmd_sub(line, cursor, s_string)
            my_print(start, line, cursor)


def double_link(x_str):
    start = None
    end = None
    for x in x_str:
        next_node = getNode(x)
        if start is not None:
            end[n_ptr] = next_node
            next_node[p_ptr] = end
            end = next_node
        else:
            start = next_node
            end = next_node
    # print(start)
    return start, end


def getNode(data1):
    return [data1, None, None]


def my_print(s, line, cur):
    result = ""
    while s is not None:
        if s == line:
            result = result + s[data][:cur] + "^" + s[data][cur:]
        else:
            result = result + s[data]
        s = s[n_ptr]
    print(result + "\n")


# move cursor one character to the left
def cmd_h(line, cur):
    if cur > 0:
        return line, cur-1
    else:
        if line == 0:
            return line, cur
        else:
            line = line[p_ptr]
            cur = len(line[data])-1
            return line, cur


# move cursor one character to the right
def cmd_i(e, line, cur):
    if cur < len(line[data])-1:
        return line, cur+1
    else:
        if line == e:
            return line, cur
        else:
            line = line[n_ptr]
            cur = 0
            return line, cur


# move cursor vertically up one line
def cmd_j(s, line, cur):
    if line == s:
        return line, cur
    else:
        if len(line[data][:cur]) > len(line[p_ptr][data])-1:
            cur = len(line[p_ptr][data])-1
        line = line[p_ptr]
        return line, cur


# move cursor vertically down one line
def cmd_k(e, line, cur):
    if line == e:
        return line, cur
    else:
        if len(line[data][:cur]) > len(line[n_ptr][data])-1:
            cur = len(line[n_ptr][data])-1
        line = line[n_ptr]
        return line, cur


# delete the character to the left of the cursor
def cmd_X(line, cur):
    if cur > 0:
        line[data] = line[data][:cur-1] + line[data][cur:]
        cur = cur - 1
        return line, cur
    else:
        return line, cur


# remove on current line from cursor to the end
def cmd_D(line, cur):
    line[data] = line[data][:cur] + "\n"
    return line


# delete current line and move cursor to the beginning of next line
def cmd_dd(s, e, line, cur):
    cur = 0
    if line == e:
        line[data] = ""
        return s, line, cur
    elif line == s:
        line[n_ptr][p_ptr] = None
        line = line[n_ptr]
        s = line
        return s, line, cur
    else:
        line[p_ptr][n_ptr] = line[n_ptr]
        line[n_ptr][p_ptr] = line[p_ptr]
        line = line[n_ptr]
        return s, line, cur


# transpose two adjacent lines
def cmd_ddp(s, e, line):
    if line == e:
        return s, e, line
    else:
        if line == s:
            line[p_ptr] = line[n_ptr]
            line[n_ptr] = line[n_ptr][n_ptr]
            line[n_ptr][p_ptr] = None
            line[n_ptr][n_ptr] = line
            line = line[n_ptr]
            s = line
            return s, e, line
        else:
            temp = line[data]
            line[n_ptr][p_ptr] = line[p_ptr]
            line[p_ptr] = line[n_ptr]
            line[n_ptr] = line[n_ptr][n_ptr]
            line[n_ptr][n_ptr] = line
            line[data] = line[n_ptr][data]
            line[n_ptr][data] = temp
            line = line[n_ptr]
            return s, e, line


# search for next occurrence of a string
def cmd_n(line, cur, str):
    temp_line = line
    while temp_line is not None:
        if temp_line == line:
            temp_cur = temp_line[data].find(str, cur, len(temp_line[data]))
            if temp_cur != -1:
                return line, cur+temp_cur
        else:
            temp_cur = temp_line[data].find(str)
            return temp_line, temp_cur
        temp_line = temp_line[n_ptr]
    return line, cur


# write your representation as text file and save it
def cmd_wq(s, line, cur):
    result = ""
    while s is not None:
        if s == line:
            result = result + s[data][:cur] + "^" + s[data][cur:]
        else:
            result = result + s[data]
        s = s[n_ptr]
    return result


# search backwards for next occurrence of a string
def cmd_r(line, cur, str):
    temp_line = line
    while temp_line is not None:
        if temp_line == line:
            temp_cur = temp_line[data].rfind(str, 0, cur)
            if temp_cur != -1:
                cur = cur - temp_cur
                return line, cur
        else:
            temp_cur = temp_line[data].rfind(str)
            return temp_line, temp_cur
        temp_line = temp_line[p_ptr]
    return line, cur


# transpose two characters
def cmd_t(s, line, cur):
    if line == s and cur == 0:
        return line
    else:
        if cur == len(line[data])-1:
            return line
        else:
            line[data] = line[data][:cur-1] + line[data][cur+1] + line[data][cur-1] + line[data][cur+1:]
            return line


# go to the beginning of next line
def cmd_plus(e, line, cur):
    if line == e:
        return line, cur
    else:
        return line[n_ptr], 0


# insert a string at the cursor
def cmd_insert(line, cur, str):
    line[data] = line[data][:cur] + str + line[data][cur:]
    return line


# substitute replace the character at the cursor with another one
def cmd_sub(line, cur, str):
    line[data] = line[data][:cur] + str + line[data][cur+1:]
    return line


if __name__ == '__main__':
    main()
