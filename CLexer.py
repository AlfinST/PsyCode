import ply.lex as lex
import json

tokens = ("DECLARATION","DEFINITION","NEWLINE","STOPWORDS")

def t_DECLARATION(t):
    r'(?:[Dd]eclare\s+)?(?:a|an)?\s*(?:int|[Ii]ntegers?|Floats?|floats?|chars?|[cC]haracters?)\s+(?:variable[s]?)?\s*([a-zA-Z][a-zA-Z0-9_]*)(?:(?:\s*(?:,|and)\s*)?[a-zA-Z][a-zA-Z0-9_]*)*'
    
    ip = t.value
    ip = ip.replace(","," , ")
    ip = ip.split()

    sem = "Declaration"
    start = 0
    if ip[0].lower() == "declare":
        start +=1
    if ip[start] in ("an","a"):
        start +=1
    var_list =list() 
    L = len(ip)
    typeDict= {"int":"int","integers":"int","integer":"int","float":"float","floats":"float","char":"char","character":"char","characters":"char"}
    for i in range(L-1,start-1,-1):

        if ip[i].lower() in ("variable","variables","and",","):
            continue
    
        elif ip[i].lower() in ("int","integers","integer","float","floats","char","characters"):
            Type = typeDict[ip[i].lower()]
            pass

        else:
            var_list.append(ip[i])
    # print(f"semantics:{sem},type = {Type},variables:{var_list}")
    print("<var_declare>")
    for  var in var_list:
        print("<variable>")
        print("<var_name>{}</var_name>".format(var))
        print("<var_type>{}</var_type>".format(Type))
        print("</variable>")
    print("</var_declare>")

def t_STOPWORDS(t):
    r'.+'
    print(t)
    pass

def t_NEWLINE(t):
    r'\n'
    print("")

def t_error(t):
    print("Well That was unexpected",t)
    print("Do better")

if __name__ == "__main__":
    lexer = lex.lex()
    with open("t1.pc","r") as inputFile:
        lines = inputFile.readlines()
    print("<program>")
    for line in lines:
        lexer.input(line)
        while tok:=lex.token():
            pass
    print("</program>")
