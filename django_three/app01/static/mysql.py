import sqlite3

class SqLite:
    #创建对象时自动执行，连接数据库
    def __init__(self):
        try:
            self.conn = sqlite3.connect(r'E:\pycharm\django_three\db.sqlite3')
            self.cursor = self.conn.cursor()
            print('连接成功')

        except Exception as err:
            print('连接失败',err)
    #查询
    def get_sqlite(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print('查询失败',err)
    # 增删改
    def in_de_up_sql(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            self.conn.rollback()
            print('修改数据失败')
            return False
    #关闭数据库
    def close(self):
        self.conn.close()
        self.cursor.close()
        print('数据库已关闭')


# db_sql=SqLite()
#
# sql='select * from user'
#
# print(db_sql.get_sqlite(sql))


