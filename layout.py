#CAPITAL LETTERS are black
#lowercase letters are white
#- are empty

def layout():
    return (
"""RNBQKBNR
PPPPPPPP
--------
--------
--------
--------
pppppppp
rnbqkbnr
""")

def test_layout():
    return (
"""K-------
B-------
-q------
--------
--------
--------
--------
r---k--r
""")
