import pymysql
from conf import config

def select_records(sql,type,conf_db: dict):
    """
    返回数据库的查询结果
    :param sql: sql查询语句
    :param type:0-返回第一条结果；1-返回全部结果
    :param conf_db:数据库配置参数
    :return:tuple类型的结果
    """
    res = []
    try:
        conn = pymysql.connect(**conf_db)
        cursor = conn.cursor()
        cursor.execute(sql)
        if (type == 0):
            res = cursor.fetchone()
        elif (type == 1):
            res = cursor.fetchall()
        return res
    except Exception as e:
        raise e

if __name__ == '__main__':
    sql = "SELECT c2.id as customerId FROM `crm_company` c1,crm_customer c2 WHERE c2.company_id = c1.id AND c1.created_by = 'xietao' AND type='1'"
    print(type(select_records(sql, 0, config.crm)[0]))