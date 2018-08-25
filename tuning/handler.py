import time
import countloop


def timing(f):
    """
    decorator to count the execution time of a function
        :param f: function instance
    """
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(
            f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


@timing
def countloop_py(times):
    resp = 0
    for i in range(times):
        for x in range(i):
            resp = (x**i) % 5
    return resp


@timing
def countloop_rust(times):
    result = countloop.countloop(str(times))
    return result
