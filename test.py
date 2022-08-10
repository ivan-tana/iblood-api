def token_require(f):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
    
        return f(args, kwargs)
    return wrapper


