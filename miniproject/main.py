from checkmate import checkmate

def main():
    # กรณี1 ไม่มีศัตรู King รอด (Fail)
    board1 = """\
..
.K\
"""

    # กรณี2 โดนRookแนวตรง (Success)
    board2 = """\
R...
.K..
..P.
....\
"""

    # กรณี3 โดนQueenแนวทแยง แต่Pawnบัง(Fail)
    board3 = """\
Q.....
......
..P...
...K..
......
......\
"""

    # กรณี4 King 2 ตัว (ไม่printอะไรเลย)
    board4 = """\
K.
.K\
"""

    # กรณี5 โดนPawnแนวทแยง (Success)
    board5 = """\
....
.K..
..P.
....\
"""

    # กรณี6 บอร์ดไม่ใช่สี่เหลี่ยมจัตุรัส (ไม่printอะไรเลย)
    board6 = """\
...
.K.\
"""

    board7 = """\
xxxxx
xxxxx
RxxxK
xxxxx
xxxxx\
"""

    board8 = """\
B????
?????
?????
?????
????K\
"""

    board9 = """\
nnQnn
nnnnn
nnnnn
nnnnn
nnKnn\
"""

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