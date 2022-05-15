# # Many documents use a specific format for a person's name. Write a program whose input is:

# firstName middleName lastName

# and whose output is:

# lastName, firstInitial.middleInitial.

# Ex: If the input is:

# Pat Silly Doe
# the output is:

# Doe, P.S.
# If the input has the form:

# firstName lastName

# the output is:

# lastName, firstInitial.

# Ex: If the input is:

# Julia Clark
# the output is:

# Clark, J. ##////////////////////////////////////

user_input = input()
splits = user_input.split(" ")
if(len(splits)==3):
    fn = splits[0]
    mn = splits[1]
    ln = splits[2]
    print(ln + ", " + fn[0] + "." + mn[0] + ".")
elif(len(splits)==2):
    fn = splits[0]
    mn = splits[1]
    print(mn + ", " + fn[0]+".")
else:
    print("The input does not have the correct form")

