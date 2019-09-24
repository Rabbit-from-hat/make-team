from cerberus import Validator

schema = {
    'num':{
        'tpye': 'integer',
        'min': 0,
    }
}

# バリデータ作成
v = Validator(schema)

# integer check
def int_check(func):
    def wrapper(*args, **kwargs):
        num = func(args[1], **kwargs)
        if not v.validate(num):
            kwargs['party_num'] = -1
            return func(*args, **kwargs)
    return wrapper




