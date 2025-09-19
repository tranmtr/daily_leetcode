# ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# class Spreadsheet:

#     def __init__(self, rows: int):
#         self.sheet = dict()
#         self.rows = rows
#         for x in ALPHABET:
#             self.sheet[x] = [0 for _ in range(rows + 1)]

#     def setCell(self, cell: str, value: int) -> None:
#         col = cell[0]
#         row = int(cell[1:])
#         self.sheet[col][row] = value

#     def resetCell(self, cell: str) -> None:
#         col = cell[0]
#         row = int(cell[1:])
#         self.sheet[col][row] = 0

#     def getValue(self, formula: str) -> int:
#         x, y = formula[1:].split("+")
#         num1, num2 = 0, 0
#         if (x[0] in ALPHABET):
#             col1 = x[0]
#             row1 = int(x[1:])
#             if (row1 > self.rows):
#                 num1 = 0
#             else:
#                 num1 = self.sheet[col1][row1]
#         else:
#             num1 = int(x)
#         if (y[0] in ALPHABET):
#             col2 = y[0]
#             row2 = int(y[1:])
#             if (row2 > self.rows):
#                 num2 = 0
#             else:
#                 num2 = self.sheet[col2][row2]
#         else:
#             num2 = int(y)
#         return num1 + num2

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")
        num1, num2 = 0, 0
        if x in self.sheet:
            num1 = self.sheet[x]
        else:
            if (x[0] not in ALPHABET):
                num1 = int(x)
            else:
                num1 = 0
        
        if y in self.sheet:
            num2 = self.sheet[y]
        else:
            if (y[0] not in ALPHABET):
                num2 = int(y)
            else:
                num2 = 0
        return num1 + num2