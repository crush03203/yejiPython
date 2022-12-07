import psycopg2
import select
from envs.workspace_python.Lib.tkinter.tix import Form
from sphinx.ext.autodoc import member_order_option
from astropy.units.quantity_helper.function_helpers import where

class DaoMem :
    #db연동
    def __init__(self) :
        self.conn = psycopg2.connect(host="127.0.0.1", dbname="python", user="postgres", password="python")
        self.cur = self.conn.cursor()
        
    ###############################
    
    ###selects###
    def selects(self):
        mydictionary = []
        
        self.cur.execute("select m_id, m_nm, tel, ymd from member")
        
        #fetchone() : 한줄씩읽기
        #fetchall() : 한번에읽기
        rows = self.cur.fetchall()
        for r in rows: #rows안에 들어있는 데이터들의 r(아이템들을) 다 읽을때까지 반복
            mydictionary.append({'m_id' : r[0], 'm_nm' : r[1], 'tel' : r[2], 'ymd' : r[3]})
             #mydictionary배열 안에 다음과 같은 내용 집어넣기(append)
             #'e_id' : 데이터 0번째 내용
        return mydictionary    
    
    ##select###
    def select(self,m_id):
        sql =f"""
        select
            m_id, m_nm, tel, ymd
        Form
            member
        where
            m_id ='{m_id}'
        """
        self.cur.execute(sql) #sql문 실행
        rows = self.cur.fetchall() # 데이터 한번에 읽기
        r = rows[0]
        ret = {'m_id' : r[0], 'm_nm' : r[1], 'tel' : r[2], 'ymd' : r[3]}
        return ret
            
       # cur conn 닫아주기 :  메모리 용량 
    def __del__(self):
        self.cur.close()
        self.conn.close()
               
#화면에 출력 
if __name__ == '__main__':
    ds = DaoMem
    #cnt = ds.insert('8','8','8', '8')
    #cnt = ds.update('9', '9', '9')
    #cnt = ds.delete('8') #8이라는 id 가지고 있는 col 지우기 
    #list = ds.selects()
    #select = ds.select('1') # e_id 1을 가지고 있는 col select하기 
    print(select)