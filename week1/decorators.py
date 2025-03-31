"""

$ python main.py
# error happens here
Error happened! : error message here
"""

def catches(catch):
    """
    catchis a tuple of exceptions, like (TypeError, RuntimeError)
    """

    def decorate(f):
        def newfunc(*a,**kw):
            try:
                return f(*a,**kw)
            except catch as e:
                # logging.exception("unexpected error in CLI’)
                print(f"caught an error: {repr(e)}")
            
        return newfunc
    return decorate