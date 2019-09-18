import pymysql,xlwt

def export_excel(table_name):
    import pymysql
    host, user, passwd, db = '127.0.0.1', 'root', '140039', 'sbl_db'
    conn = pymysql.connect(user=user,host=host,port=3306,passwd=passwd,db=db,charset='utf8')
    cur = conn.cursor()
    sql = 'select * from %s;' %table_name
    cur.execute(sql)
    fileds = [filed[0] for filed in cur.description]
    all_data = cur.fetchall()

    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')

    for col, field in enumerate(fileds):
        sheet.write(0, col, field)

    row = 1
    for data in all_data:
        for col, field in enumerate(data):
            sheet.write(row, col, field)
        row += 1
    book.save('%s.xls' %table_name)

export_excel('student_info')
