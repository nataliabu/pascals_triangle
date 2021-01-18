import os

width = os.get_terminal_size().columns

line = [1]

line_view = ""

# Clean screen and move cursor to the top
print("\033[2J\033[0;0H")

def new_line(old):
    new_line = []
    a = 0
    b = 1
    new_line.append(old[0])
    for i in range(len(old) - 1):
        new_line.append(old[a] + old[b])
        a += 1
        b += 1
    new_line.append(old[-1])
    return new_line

while width >= len(line_view):
    print(line_view.center(width))
    line_str = [str(num) for num in line]
    line_view = "   ".join(line_str)
    line = new_line(line)
