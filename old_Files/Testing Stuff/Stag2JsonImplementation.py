# import ply.lex as lex
import json

def variable(name,outputFile,intend,type = None):
    print("\t"*intend,end="")
    print("<variable>")
    
    if type == None:
        print("\t"*intend,end="")
        print("\t\t<var_name>{}</var_name>".format(name))
    
    print("\t"*intend,end="")
    print("\t</variable>")

def function(line,outputFile,intend):
    print("<function>")
    argsNO = len(line)
    if line[0][0] == "identifier":
        print("\t"*intend,end="")
        print("\t<function_name>{}</function_name>".format(line[0][1]))
    
    if argsNO == 2:
        print("\t"*intend,end="")
        print("\t<args>")
        args = line[1][1]
        args = args[1:-1].split(',')
        # print(args)
        for argument in args:
            print("\t"*intend,end="")
            print("\t\t<exp>{}</exp>".format(argument))
        print("\t"*intend,end="")
        print("\t</args>")
    print("\t"*intend,end="")
    print("</function>")

def assignment(line,outputFile,intend):
    print("\t"*intend,end="")
    print("<assignment>")
    # print(line)
    print("\t"*intend,end="")
    
    variable(line[0][1],outputFile,intend)
    
    print("\t"*intend,end="")
    print("<value>")
    for i in line:
        if i[0] == "identifier":
            pass
        # need a lexer

def bodyChecker(old,new):
    intend = None
    if old == new:
        pass
    if old < new:
        print("\t"*new,end="")
        print("<body>")

    while old > new:
        print("\t"*old,end="")
        print("<done></done>")
        print("\t"*old,end="")
        print("</body>")
        old -= 1

if __name__ == "__main__":
    
    with open("Table.json","r") as Jsonfile:
        ParsedTree = json.load(Jsonfile)

    old_intendLevel = 0
    
    with open("PythonXML.xml","w") as outputFile:
        for branch in ParsedTree:
            tag = branch["tag"]
            line = branch["data"]
            current_intendLevel = branch["intendLevel"]
            
            bodyChecker(old_intendLevel,current_intendLevel)
            old_intendLevel = current_intendLevel
            
            if tag == 'function':
                function(line,outputFile,current_intendLevel)

            if tag == 'assignment':
                assignment(line,outputFile,current_intendLevel)
    
    print("="*50)
    for i in ParsedTree:
        print(i)
    