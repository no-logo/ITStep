import functools
import os

class Logger:
    def log_info(self, message):
        raise NotImplementedError

    def log_debug(self, message):
        raise NotImplementedError

    def log_error(self, message):
        raise NotImplementedError
    

class ConsoleLogger(Logger):
   
    def log_info(self, message):
        print(f'log_info: {message}')

    def log_debug(self, message):
        print(f'log_debug: {message}')

    def log_error(self, message):
        print(f'log_error: {message}')

class FileLogger(Logger):
    
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                pass
                
     def log_info(self, message):
        with open(self.file_name, 'a') as file:
            file.write(f'[INFO]: {message}')

    def log_debug(self, message):
        pass

    def log_error(self, message):
        pass
    

def log_operator(level):
    pass

def log_operator(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            logger = ConsoleLogger()
            if level == 'INFO':
                logger.log_info(f'Callint {func.__name__} with args {args} and kwargs {kwargs}')
            elif level == 'DEBUG':
                logger.log_debug(f'Callint {func.__name__} with args {args} and kwargs {kwargs}')
            elif level == 'ERROR':
                logger.log_error(f'Callint {func.__name__} with args {args} and kwargs {kwargs}')
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, name) -> None:
        self.name = name

    @log_operator('INFO')
    def login(self):
        print(f'{self.name} hass logged in')

    @log_operator('ERROR')
    def logout(self):
        print(f'{self.name} hass logged out')
        
u = User('Andrzej')
u.login()