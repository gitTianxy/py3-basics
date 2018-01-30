import mysql.connector

ppc_con = None
cursor = None
date_begin = '2017-06-02'

sql_tmpl = '''
SELECT fid, evalue
FROM fileextend_inner_%s
WHERE last_update_time>%s
AND ekey='av_scan_result'
AND fid IN(fids)
'''


def initDB():
    global ppc_con
    global cursor
    config = {
        'host': '10.200.70.202',
        'user': 'qamysql',
        'password': 'Qa&MySQL!2014',
        'port': 3312,
        'database': 'cloudplay_publiccloud'
    }
    ppc_con = mysql.connector.connect(**config)


try:
    initDB()
    print 'connection success'
    cursor = ppc_con.cursor()
    i = 1
    fids = [5542145, 5542657, 5542401, 5543169]
    plcholder = ', '.join('%s' for unused in fids)
    pst = sql_tmpl.replace('fids', plcholder)
    params = []
    params.append(i)
    params.append(date_begin)
    params.extend(fids)
    cursor.execute(pst, params)
    for fid, evalue in cursor:
        print 'fid=%s, evalue=%s' % (fid, evalue)

    print '-----------------------------'
    # cursor.execute(sql_tmpl, (i, date_begin))
    cursor.execute(pst, params)
    results = cursor.fetchall()
    for item in results:
        print 'fid=%s, evalue=%s' % (item[0], item[1])

except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
finally:
    cursor.close()
    ppc_con.close()
