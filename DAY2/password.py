import re
password =input("ENTER THE PASSWORD...")
pattern = r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}'
if re.match(pattern, password):
    print(f"{password} is a strong password.")
else:
    print(f"{password} is not a strong password.")


'''
(?= is the start of a look-ahead group — the question mark does not mean the same as a ? elsewhere
.*? is a non-greedy match against anything or nothing. The question-mark here also does not mean 'optional'.
[A-Z] is a character set containing the upper case ASCII letters A through to Z.
) is the end of the look-ahead group

So the net result is:

"Look ahead and see if, after maybe some characters, there is an upper case letter."
'''