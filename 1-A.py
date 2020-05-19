import sqlite3
conn = sqlite3.connect('0000.sqlite')
cursor = conn.cursor()

class ScoreGame:
    
    def __int__(self, c, d):
        self.id = c
        self.score = d
        
    def A(self):
        a = int(input("請輸入成績id?"))
        b = int(input("請輸入成績?"))
        sqlstr = "insert into Enter_Score values ({},{})".format(a,b)
        cursor.execute(sqlstr)
        conn.commit()
        conn.close()
        
pp = ScoreGame()
pp.A()
