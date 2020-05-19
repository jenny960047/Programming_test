import sqlite3
conn = sqlite3.connect('0000.sqlite')
cursor = conn.cursor()

class ScoreGame:
    
    def __int__(self, c):
        self.id = c
        
    def C(self):
        a = int(input("請輸入欲刪除的成績id?"))
        sqlstr = "delete from Enter_Score where id={}".format(a)
        cursor.execute(sqlstr)
        conn.commit()
        conn.close()
        
pp = ScoreGame()
pp.C()
