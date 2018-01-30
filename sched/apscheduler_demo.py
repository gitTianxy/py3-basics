# encoding=utf-8
"""
ABOUT the API

# API 功能
APScheduler是一个 Python 定时任务框架，使用起来十分方便.
* 提供了基于日期、固定时间间隔以及 crontab 类型的任务.
* 可以持久化任务.
* 支持 daemon 方式运行应用.

# API 组成 -- 4个组件
1. 触发器(trigger)
```
* date: 特定的时间点触发
* interval: 固定时间间隔触发
* cron: 在特定时间周期性地触发
```
2. 作业存储(job store)
```
* 默认的作业存储是简单地把作业保存在内存中，还有其他数据库方案。
* 一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。
* 调度器不能分享同一个作业存储。
```
3. 执行器(executor)
```
* ProcessPoolExecutor
* ThreadPoolExecutor
```
4. 调度器(scheduler)
```
* 应用的开发者通常不会直接处理作业存储、调度器和触发器，相反，调度器提供了处理这些的合适的接口。
* 例如添加、修改和移除作业。
* APScheduler 中有两种常用的调度器，BlockingScheduler 和 BackgroundScheduler.
```
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime
from apscheduler.events import *


def print_now():
    print datetime.now()


def print_date():
    print datetime.now().date()


def print_time():
    print datetime.now().time()


def job_listener(event):
    global scheduler
    global trigger_type

    if event.exception:
        job_fail()
    else:
        job_succ()

    if trigger_type == 'date':
        for job in scheduler.get_jobs():
            job.remove()
        scheduler.shutdown(wait=False)


def job_fail():
    print 'The job crashed :('


def job_succ():
    print 'The job worked :)'


def get_cron_val(args, key):
    if args.get(key):
        return args.get(key)
    else:
        return '*'


def blocking_sched(job, job_args=None, trigger=None, **trigger_args):
    """
    BlockingScheduler: use when the scheduler is the only thing running in your process
    3 types of triggers: cron, date, interval
    :param job:
    :param trigger:
    :param trigger_args:
    :return:
    """
    global scheduler
    global trigger_type

    scheduler = BlockingScheduler()
    trigger_type = trigger
    job_args = tuple(job_args) if job_args is not None else ()
    if trigger == 'cron':
        year = get_cron_val(trigger_args, 'year')
        month = get_cron_val(trigger_args, 'month')
        day = get_cron_val(trigger_args, 'day')
        day_of_week = get_cron_val(trigger_args, 'day_of_week')
        hour = get_cron_val(trigger_args, 'hour')
        minute = get_cron_val(trigger_args, 'minute')
        second = get_cron_val(trigger_args, 'second')
        scheduler.add_job(job, trigger, year=year, month=month, day=day, day_of_week=day_of_week, hour=hour,
                          minute=minute, second=second, args=job_args)
    elif trigger == 'date':
        scheduler.add_job(job, trigger, run_date=trigger_args['date'], args=job_args)
    elif trigger == 'interval':
        start = trigger_args.get('start_date')
        end = trigger_args.get('end_date')
        if start is None:
            start = datetime.now()
        if end:
            scheduler.add_job(job, trigger, seconds=trigger_args['seconds'], start_date=start, end_date=end)
        else:
            scheduler.add_job(job, trigger, seconds=trigger_args['seconds'], start_date=start)

    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()


# TODO
def bg_sched(job, job_args=None, trigger=None, **trigger_args):
    """
    BackgroundScheduler: use when you’re not using any of the frameworks below,
        and want the scheduler to run in the background inside your application
    :return:
    """
    global scheduler
    global trigger_type

    scheduler = BackgroundScheduler()
    trigger_type = trigger
    job_args = tuple(job_args) if job_args is not None else ()
    if trigger == 'cron':
        scheduler.add_job(job, trigger, args=job_args)
    elif trigger == 'date':
        scheduler.add_job(job, trigger, run_date=trigger_args['date'], args=job_args)
    elif trigger == 'interval':
        start = trigger_args.get('start_date')
        end = trigger_args.get('end_date')
        if start is None:
            start = datetime.now()
        if end:
            scheduler.add_job(job, trigger, seconds=trigger_args['seconds'], start_date=start, end_date=end)
        else:
            scheduler.add_job(job, trigger, seconds=trigger_args['seconds'], start_date=start)

    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()


scheduler = None
trigger_type = None
if __name__ == '__main__':
    blocking_sched(print_now, trigger='date', date='2017-12-21 13:28:59')
    # blocking_sched(print_now, trigger='cron', second='*/5')
    # blocking_sched(print_now, trigger='interval', seconds=5)
    # TODO:bg_sched(print_now, trigger='date', date='2017-12-21 11:54:00')
