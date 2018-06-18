import pymysql

import settings


class DB:
    def __init__(self):
        self.db = pymysql.connect(**settings.DATABASE)
        self.cursor = self.db.cursor()
        print('数据库连接成功')

    def save(self, item):
        self.cursor.execute('insert zhaopin(zwmc,gsmc,zwyx,gzdd) values(%s,%s,%s,%s)',
                            args=(item.zwmc,item.gsmc,item.zwyx,item.gzdd))
        if self.cursor.rowcount:
            print('数据保存成功')
            self.db.commit() # 提交事务

    def close(self):
        self.db.close()

if __name__ == '__main__':
    DB()