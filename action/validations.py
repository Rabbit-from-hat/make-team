from cerberus import Validator

class Validations:

    def __init__(self):
        schema = {
            'num':{
                    'tpye': 'integer',
                    'min': 0,
            }
        }
        self.vdate = Validator(schema)
    
    def int_check(self, party_num):

        if not self.vdate.validate(party_num):
            msg = "実行できません。整数で指定してください。"
            return 0, msg        
        return 1
    
    def grouping_check(self, state, party_num, mem_len):

        #依頼主自身がVoiceChannelにいないとき
        if state is None: 
            return 0, '実行できません。ボイスチャンネルに入ってコマンドを実行してください。'

        #ボイスチャンネルに一人しかいない場合
        if mem_len == 1:
            return 0, '実行できません。２人以上参加してください。'

        #party_numがメンバー数を超えていた場合
        if party_num > mem_len:
            return 0,'実行できません。チーム数がメンバーを超えてます。'