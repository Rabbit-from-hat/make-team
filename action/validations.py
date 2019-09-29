from cerberus import Validator

class Validations:

    def __init__(self):
        self.schema = {
            'num':{
                    'tpye': 'integer',
                    'min': 0,
            }
        }
        self.vdate = Validator(self.schema)
    
    def int_check(self, func):

        def wrapper(*args, **kwargs):
            num = kwargs['party_num']

            if not self.vdate.validate(num):
                kwargs['party_num'] = -1
                return func(*args, **kwargs)

        return wrapper