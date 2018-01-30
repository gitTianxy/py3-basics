# coding=utf-8
from util.mydbpool import MyDbUtils
import conf.db_config as DBConfig

create_tbl_sql = '''
CREATE TABLE pptv_publiccloud.filecp_244 (
  id INT(11) NOT NULL AUTO_INCREMENT,
  fid BIGINT(20) NOT NULL,
  channel_id BIGINT(20) DEFAULT NULL,
  status INT(11) NOT NULL,
  fromcp VARCHAR(45) NOT NULL,
  insert_time TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
  last_update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY fid_fromcp_uniq (fid,fromcp)
) ENGINE=INNODB AUTO_INCREMENT=343953 DEFAULT CHARSET=utf8
'''
col_exists_sql = '''
SELECT COUNT(*) 
FROM information_schema.COLUMNS 
WHERE 
    TABLE_SCHEMA = '%s' 
AND TABLE_NAME = 'filecp_%s' 
AND COLUMN_NAME = 'biztype'
'''
alter_tbl_sql = '''
ALTER TABLE %s.filecp_%s
ADD COLUMN biztype VARCHAR(45) COMMENT 'upload type';
'''
insert_row_sql = '''
INSERT IGNORE INTO pptv_publiccloud.filecp_%s (fid,channel_id,STATUS,fromcp,insert_time,last_update_time,biztype)
VALUES(%s,150262704,200,'private_cloud','2014-06-06 19:30:38','2014-12-30 22:00:43','%s');
'''
insert_partialrow_sql = '''
INSERT IGNORE INTO pptv_publiccloud.filecp_%s (fid,channel_id,STATUS,fromcp,insert_time,last_update_time)
VALUES(%s,150262705,200,'private_cloud','2014-06-06 19:30:38','2014-12-30 22:00:43');
'''


def generate_altertbl_sqls(path, tbl_start, tbl_end):
    with open(path, "w") as f:
        for i in range(tbl_start, tbl_end):
            f.write(alter_tbl_sql % i)
    f.close()


def insert_biztype(tb_seq, fid, biztype):
    conn = None
    cur = None
    try:
        if biztype is None:
            sql = insert_partialrow_sql % (tb_seq, fid)
        else:
            sql = insert_row_sql % (tb_seq, fid, biztype)
        conn = MyDbUtils.get_connect(DBConfig.local_config)
        cur = conn.cursor()
        cur.execute(sql)
    except Exception, e:
        print e
    else:
        conn.commit()
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def alter_tbl(db):
    for tbl_seq in range(0, 256):
        sql1 = col_exists_sql % (db, tbl_seq)
        conn = None
        cur = None
        try:
            conn = MyDbUtils.get_connect(DBConfig.ppc_config_test)
            cur = conn.cursor()
            cur.execute(sql1)
            count = cur.fetchone()[0];
            if count == 0:
                sql2 = alter_tbl_sql % (db, tbl_seq)
                print '---alter_tbl_sql: ', sql2
                cur = conn.cursor()
                cur.execute(sql2)
            else:
                print 'biztype EXISTS in fromcp_%s' % tbl_seq
        except Exception, e:
            print e
        else:
            conn.commit()
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    alter_tbl('cloudplay_publiccloud')
    '''
    generate_altertbl_sqls('../result/add_biztype.txt', 0, 256)
    insert_biztype(tb_seq=0, fid=281076, biztype='cc')
    insert_biztype(tb_seq=0, fid=281078, biztype=None)
    '''
