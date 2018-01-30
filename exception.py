# encoding=utf-8
"""
1. try-except
2. self-defined exception
"""
from multiprocessing.pool import ThreadPool
import random
import threading
import time
import traceback

mutex = threading.Lock()


class TryExceptDemo:
    """
    python use 'try-except' to CATCH exception, and use 'raise' to THROW exception
    """

    def __init__(self):
        print("try-except demo-----------")
        TryExceptDemo.demo()

    @staticmethod
    def demo():
        try:
            try:
                1 / 0
            except:
                print('here is when exception happens')
                raise ArithmeticError('calculation error. top:%s, bottom:%s' % (1, 0))
            else:
                print('here is when exception not happens')
            finally:
                print('here is when all the block above finished')
        except ArithmeticError as e:
            print("ArithmeticError: ", e.message)
            try:
                raise RuntimeError('*err happens in except.')
            except Exception as ex:
                print(ex)
        except Exception as e:
            print("Exception: ", e.message)


class MyExceptionDemo:
    """
    TIP: str(e)==e.message
    """

    def __init__(self):
        print("self-defined exception demo-----------")
        try:
            msg = 'test'
            err = 'my-exception'
            raise MyExceptionDemo.MyException(msg, err)
        except Exception as e:
            print('%s: type=%s, msg=%s, err=%s' % (e, type(e).__name__, e.message, e.errors))

    class MyException(Exception):
        """
        NOTE:
            自定义异常需继承自Exception
            可以自定义'__str__'方法, 默认为返回message值
        """

        def __init__(self, message, errors):
            Exception.__init__(self, message)
            self.errors = errors


class ThreadExceptDemo:
    def __init__(self):
        print('------------- thread exception demo --------------')
        # try:
        #     self.run_thr()
        # except Exception, ex:
        #     print(ex
        try:
            pl = ThreadPool(10)
            self.method_share_pool_a(pl)
            self.method_share_pool_b(pl)
        except Exception as ex:
            print(ex)
        finally:
            pl.close()
            pl.join()

    def run_thr(self):
        try:
            pl = ThreadPool(20)
            print('before run thread')
            pl.map(ThreadExceptDemo.print_idx, range(0, 100))
        except:
            raise
        finally:
            pl.close()
            pl.join()
            print('after run thread')

    @staticmethod
    def print_idx(i):
        display(i)
        time.sleep(1)
        # if random.random() > 0.2:
        #     display(i)
        #     time.sleep(1)
        # else:
        #     raise RuntimeError('print idx err. TEST')

    def method_share_pool_a(self, pl):
        display('exec method A share threadpool')
        try:
            pl.map(ThreadExceptDemo.print_idx, range(100, 150))
            raise RuntimeError('error occur in method A')
        except:
            pl.close()
            pl.join()
            raise

    def method_share_pool_b(self, pl):
        display('exec method B share threadpool')
        try:
            pl.map(ThreadExceptDemo.print_idx, range(0, 100))
            raise RuntimeError('error occur in method A')
        except:
            pl.close()
            pl.join()
            raise


def display(content):
    global mutex

    mutex.acquire()
    print(content)
    mutex.release()


def print_ex_stack():
    display('====print exception stack demo====')
    try:
        raise RuntimeError('runtime err. TEST')
    except:
        display(traceback.format_exc())
    finally:
        display('after print stack')


def finally_in_loop():
    """
    code block in FINALLY is executed before the 'continue' & 'return' & 'break' in EXCEPT & TRY
    :return:
    """
    print("===demo: finally in loop===")
    while True:
        try:
            display("here in 'try'")
            # continue
            break
            # raise RuntimeError('test')
        except:
            display("here in 'except'")
            # continue
            break
        finally:
            display("here in 'finally'")


def catch_specific_err():
    """
    catch a specific err, which raise others
    :return:
    """
    try:
        raise ArithmeticError('test')
        # raise RuntimeError('test')
    except ArithmeticError as err:
        print("here catched an 'ArithmeticError':", err)
        pass
    except:
        print("an err catched by default 'except'")
        raise


if __name__ == "__main__":
    # TryExceptDemo()
    # MyExceptionDemo()
    # ThreadExceptDemo()
    # print_ex_stack()
    # finally_in_loop()
    catch_specific_err()
