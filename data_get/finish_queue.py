import queue


def finish_queue(fun):
    def inner(self):
        try:
            fun(self)
        except queue.Empty:
            print("end queue")

    return inner
