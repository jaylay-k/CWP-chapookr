import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]

    if keyword not in string:
        print("none")
    else:
        print(string.count(keyword))