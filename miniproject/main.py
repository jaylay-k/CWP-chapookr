from checkmate import checkmate

def main():
    #(Fail)
    board1 = """\
..
.K\
"""

    #(Success)
    board2 = """\
R...
.K..
..P.
....\
"""

    #(Fail)
    board3 = """\
Q.....
......
..P...
...K..
......
......\
"""

    #(ไม่printอะไรเลย)
    board4 = """\
K.
.K\
"""

    #(Success)
    board5 = """\
....
.K..
..P.
....\
"""

    #(ไม่printอะไรเลย)
    board6 = """\
...
.K.\
"""

    #(Success)
    board7 = """\
xxxxx
xxxxx
RxxxK
xxxxx
xxxxx\
"""

    #(Success)
    board8 = """\
B????
?????
?????
?????
????K\
"""
    
    #(Success)
    board9 = """\
nnQnn
nnnnn
nnnnn
nnnnn
nnKnn\
"""

    #(Success)
    board10 = """\
BYvx2N7
f-+x19E
*qkgx9&
D--s$5#
iGlV1y*
783rvZA
jFN8q9K\
"""

    #checkmate(board1)
    #checkmate(board2)
    #checkmate(board3)
    #checkmate(board4)
    #checkmate(board5)
    #checkmate(board6)
    #checkmate(board7)
    #checkmate(board8)
    #checkmate(board9)
    #checkmate(board10)

if __name__ == "__main__":
    main()