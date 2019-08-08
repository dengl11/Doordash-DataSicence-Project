import sys

def parse_jsons_no_split(fpath, encoding="utf-8"):
    """parse a 'json' file where objects are concatenated to each other with no splits 
    :fpath: file path
    :returns: iterator of a dictionary object

    """
    stack = [] # stack to keep track of pairing {}
    with open(fpath, "r", encoding=encoding) as f:
        s = f.read()
    for i, ch in enumerate(s):
        if ch == '{':
            stack.append(i)
        elif ch == '}':
            pre = stack.pop()
            if not stack:
                yield eval(s[pre : i+1])


def parse_jsons_by_line(fpath, encoding="utf-8"):
    """parse a 'json' file where each line is an object

    :fpath: file path
    :returns: iterator of a dictionary object

    """
    stack = [] # stack to keep track of pairing {}
    with open(fpath, "r", encoding=encoding) as f:
        lines = f.readlines()
        for l in lines:
            try:
                yield(eval(l))
            except Exception as e:
                err = "cannot parse this line in file {}:\n{}".format(fpath, l)
                print(err, sys.stderr)
                ls = l.replace("}{", "}\n{").split('\n')
                for cl in ls:
                    try:
                        yield(eval(cl))
                    except Exception as e:
                        continue
