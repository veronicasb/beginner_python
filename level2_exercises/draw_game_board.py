def request_dimensions():
    rows = ""
    cols = ""
    while not rows:
        try:
            rows = int(input("Enter the number of rows: "))
        except ValueError:
            print("Entry must be a number!")
    while not cols:
        try:
            cols = int(input("Enter the number of columns: "))
        except ValueError:
            print("Entry must be a number!")
    return rows, cols

def draw_board(rows, cols):
    top_border = ("-" * 3)
    side_border = "|" + (" " * len(top_border))
    count = rows
    while count != 0:
        print(f' {top_border}' * cols)
        print(side_border * cols, end="|\n")
        count -= 1
    print(f' {top_border}' * cols)

rows, cols = request_dimensions()
draw_board(rows, cols)