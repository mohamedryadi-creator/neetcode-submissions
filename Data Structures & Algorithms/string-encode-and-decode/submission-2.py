class Solution:

    def encode(self, strs: List[str]) -> str:
        str=""
        for i in strs :
            longueur=f"{len(i)}"
            str+="".join([longueur,'@',i])
        print(str)

        return str

        

    def decode(self, s: str) -> List[str]:
        res=[]
        longueur=""
        indice=0
        i=0
        while i<len(s):
            if s[i]=='@':
                indice=i
                n=int(longueur)
                mot=""
                for j in range(i+1,i+n+1):
                    mot+=s[j]
                    
                    
                res.append(mot)
                i=indice+n+1
                longueur=""
                continue
            longueur+=s[i]
            i+=1
        return res
            
            



