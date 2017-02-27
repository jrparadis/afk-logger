import sqlite3
sql = sqlite3.connect('afk.db')
cur = sql.cursor()
x = cur.execute('SELECT sum(seconds) FROM posts')
y = 0
for each in x:
    print each
    y = str(each)
    

y1 = str(y).strip('(),')
y2 = float(y1) / 60
y3 = y2 / 60
y4 = y3 / 24

print y1 + ' seconds idle'
print str(y2) + ' minutes idle'
print str(y3) + ' hours idle'
print str(y4) + ' days idle'
raw_input()
