
def team_msg(team,num):
    msg = []

    for line in team:
        msg.append("チーム"+num)
        for mem in line:
            msg.append(mem)
        num -= 1

    msg = "\n".join(msg)
    return msg
    
    