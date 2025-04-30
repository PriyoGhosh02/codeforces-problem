import pyperclip

s = input()
split = s.split()

s="_".join(split)

pyperclip.copy(s)  # pip install pyperclip
print("\033[31mText copied to clipboard!\033[0m")


# git add .
# git commit -m "commit"
# git push -u origin desktop

# create a new branch
# git checkout -b new_branch_name