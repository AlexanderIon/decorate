import time


def log_decorate1(my_path="log.txt"):
    def log_decorate(some_function):

        def new_function(*args, **kwargs):

            date_ = time.time()
            result = some_function(*args, **kwargs)
            param = str(locals())
            with open(my_path, "w", encoding="utf-8") as file:
                file.write(param)
            return result

        return new_function

    return log_decorate



