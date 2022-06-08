import textwrap

def wrap(string, max_width):
    l = list()
    for i in range(len(string)):
        if i%max_width==0 :
            l.append(string[i:max_width+i])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
