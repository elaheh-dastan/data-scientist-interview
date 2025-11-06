# function that takes a string of length 5 containing only letters R, G and Y print "nakhor lite" if the string has
# at least three R or at least two R and at least two Y at the same time or no G at all otherwise print "rahat baash"
def nakhor_lite(s):
    if s.count('R') >= 3 or (s.count('R') >= 2 and s.count('Y') >= 2):
        print("nakhor lite")
    elif s.count('G') == 0:
        print("nakhor lite")
    else:
        print("rahat baash")

input_string = input()
nakhor_lite(input_string)
# nakhor_lite("RRRRG")
# nakhor_lite("RRRRY")
# nakhor_lite("RRRRY")
# nakhor_lite("YYYYY")
# nakhor_lite("GGGGG")
# nakhor_lite("RYRYR")