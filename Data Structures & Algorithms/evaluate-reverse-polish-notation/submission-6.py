class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nombre=[]
        operations=set(['+','*','/','-'])
        for c in tokens :
            if c in operations :
                n1=nombre.pop()
                n2=nombre.pop()
                if c=='+' :
                    nombre.append(n1+n2)
                elif c=='*':
                    nombre.append(n1*n2)
                elif c=='-':
                    nombre.append(n2-n1)
                else :
                    nombre.append(int(float(n2)/float(n1)))
            else :
                nombre.append(int(c))
        return int(nombre[0]) 
        