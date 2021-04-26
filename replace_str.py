import sys

oldtext = open(sys.argv[1]).read()
oldtext = oldtext.replace(sys.argv[3], sys.argv[4])

f2 = open(sys.argv[2], 'w')
f2.write(oldtext)
f2.close()