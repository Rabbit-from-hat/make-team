#  送信用に配列を編集
#　
#  msg = {
#    'チーム1',
#    'a',
#    'b',
#    'チーム2',
#    'c',
#    'd'}

def team_msg(team, num:int):
    msg = []

    for i in range(num):
        msg.append("チーム"+str(i+1))
        for line in team: 
            for mem in line:
                msg.append(mem)

    msg = "\n".join(msg)
    return msg