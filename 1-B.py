import sqlite3
conn = sqlite3.connect('0000.sqlite')
cursor = conn.cursor()

class ScoreGame:
    
    def __int__(self, c, d):
        self.id = c
        self.score = d
        
    def B(self):
        a = int(input("請輸入修改成績id?"))
        b = int(input("請輸入修改成績?"))
        sqlstr = "update Enter_Score set score={} where id={}".format(b,a)
        cursor.execute(sqlstr)
        conn.commit()
        conn.close()
        
pp = ScoreGame()
pp.B()
