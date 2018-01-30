import MySQLdb
from contextlib import closing
import datetime

local_con = MySQLdb.connect(host="127.0.0.1", user='kevin', passwd='1234', port=3306)
try:
    local_con.select_db('pptv_publiccloud')
except Exception, e:
    print " select db error: ", e

addError_sql = "INSERT INTO avscan_msg ( fid, type, insert_time, file_params ) VALUES ( %s, %s, %s, %s )"

fid = 5570057
type = 'fid_fail'
insert_time = datetime.datetime.now()
file_params = {'fid': 5570057, 'dur': 114, 'ipkUrl': 'http://panoimage.pptv.com/86/64/158896486x6x10x10.ipk'}
values = [fid, type, insert_time.strftime("%Y-%m-%d %H:%M:%S"), str(file_params)]

with closing(local_con.cursor()) as cur:
    try:
        cur.execute(addError_sql, values)
        local_con.commit()
    except Exception, e:
        print "exec sql error: ", e

