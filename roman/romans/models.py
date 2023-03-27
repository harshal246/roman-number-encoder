from django.db import models


class encoding_to_number:


    def transform(args):
        dict={
        1:"I",
        15:"V",
        2:"X",
        25:"L",
        3:"C",
        4:"M",
        35:"D"}
        v=""
        p=len(str(args))
        g=str(args)
        for i in range(p):
            a=dict.get(p)
            if int(g[i])>=4 and int(g[i])<=8:a=dict.get(int(str(p)+"5"))
            elif int(g[i])==9:v+=a+dict.get(p+1)
            if int(g[i])<=3:v+=a*int(g[i])
            elif int(g[i])==4 and p!=4:v+=dict.get(p)+a
            elif int(g[i])>=5 and int(g[i])<=8:v+=a+dict.get(p)*(int(g[i])-5)
            p-=1
        return "M"*4+v if len(g)==4 and g[0]=="4" else v
    
