def solution(id_pw, db):
    idli = [[i,db[i][0]] for i in range(len(db)) if db[i][0] == id_pw[0]]
    if len(idli) == 0 : return 'fail'
    else:
        for idx,id in idli:
            if db[idx][1] == id_pw[1]:
                return 'login'
        return 'wrong pw'