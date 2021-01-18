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
        c = old[a] + old[b]
        new_line.append(c)
        a += 1
        b += 1
    new_line.append(old[-1])
    return new_line

while width >= len(line_view):
    print(line_view.center(width))
    line_str = [str(num) for num in line]
    line_view = "   ".join(line_str)
    line = new_line(line)

explanation = """
Let's start with 1 and imagine (invisible) 0s on each side of it.
If we add them together in pairs, we get 0 + 1 = 1 and 1 + 0 = 1, which is
how the second row is created.
We do that again with the second row: 0 + 1 = 1, 1 + 1 = 2, and 1 + 0 = 1;
and so we generate the third row.
We can keep doing this as long as we want!
"""

print(explanation)
