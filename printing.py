
# @uthor: Nitin Kaundun
# FileName: printing.py
# Version 1.0
# Purpose: Show the running of code regarding printing


def printing_code(pcodes):
    for code in pcodes:
        print(">>>", code)
        try:
            exec(code)
        except Exception as e:
            print(e)
        print()


codes = ["""print("the result of" + "2" + "9" + "is", 11) """,
         """print(3 + "*" + 7 + "is equal to", 18 + 3) """,
         """print(7 "+" 3)""" ,
         """print(7 + "+" + 3) """,
         """print(7, "+", 3) """,
         """print("7" + " + " + "3") """,
         """print(int(12.3))""",
         """print(float(12)) """,
         """print(int('7') + str(12)) """,
         """x = 7
y = 4
x = y
y = x
print(x, y)"""
         ]
printing_code(codes)
