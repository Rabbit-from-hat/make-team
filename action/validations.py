from cerberus import Validator

class Validations:

    def __init__(self):
        schema = {
            'num':{
                    'type': 'integer',
                    'min': 0
            }
        }
        self.vdate = Validator(schema)
    
    def int_check(self, party_num):
        
        num = {'num': party_num}

        if not self.vdate.validate(num):
            return '実行できません。整数で指定してください。'
        return 1
    
    def grouping_check(self, state, party_num, mem_len):

        #依頼主自身がVoiceChannelにいないとき
        if state is None: 
            return '実行できません。ボイスチャンネルに入ってコマンドを実行してください。'

        #ボイスチャンネルに一人しかいない場合
        if mem_len == 1:
            return '実行できません。２人以上参加してください。'

        #party_numがメンバー数を超えていた場合
        if party_num > mem_len:
            return '実行できません。チーム数がメンバーを超えてます。'
        
        return 1