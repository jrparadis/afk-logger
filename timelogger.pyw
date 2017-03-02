import time
import pymouse
import sqlite3


sql = sqlite3.connect('afk.db')
cur = sql.cursor()
#should seconds be float or int? not sure if sqlite3 cares or not. 
cur.execute('CREATE TABLE IF NOT EXISTS posts(timeleft TEXT, timeback TEXT, seconds TEXT)')
sql.commit()
cur.execute('SELECT * FROM posts')

mouse = pymouse.PyMouse()
oldpos = ((()))
pos = ((()))
afk = 0.00
afk1 = 0.000
starttime = time.time()
away = 0

while 1:

    oldpos = pos
    pos = mouse.position()
    if away == 1:
        if not oldpos == pos:
            away = 0
            #log back time in database
            cur.execute('INSERT INTO posts VALUES(?, ?, ?)', [afktime, time.strftime('%c'), time.time() - afkat])
            sql.commit()
            afk1 = 0
            starttime = time.time()
            #print ('back')
            
    else:       
        if afk1 >= 300:
            afkat = time.time()
            afktime = time.strftime('%c')
            away = 1
            #put time in database
            #print ('away')
        if oldpos == pos:
            afk1 = time.time() - starttime

        
            

        
    
