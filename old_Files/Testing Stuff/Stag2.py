import ply.lex as lex
import re as R

tokens =("PROGRAM","UNKNOWN","ASSIGN","EXP_ASSIGN","NEWLINE")

def t_PROGRAM(t):
    r'<program>[\s ]*<identifier>'
    print("<program>\n\t<program_name>{}<\program_name>".format(Input[word_count+2]))
    increment(2)

def t_ASSIGN(t):
    r'<assign>.+</assign>'
    text = t.value.split()
    length = len(text)
    # print(text)
    # print(length)

    for eq,i in enumerate(text):
        if i == '=':
            break
    # print(eq)
    
    text.remove("<assign>")
    text.remove("</assign>")

    print("<assignment>\n\t<variable>")
    print("\t\t<var_name>{}</var_name>".format(Input[word_count+2]))
    increment(2)
    print("\t</variable>\n\t<value>\n\t\t<expression>")
    print("\t\t\t<int>{}</int>".format(Input[word_count+2]))
    increment(2)
    # for i in range(eq+1,length):
    #     word = text[word_count]
    print("\t\t</expression>\n\t</value>")

def t_EXP_ASSIGN(t):
    r'<identifier>[\s ]*=[\s ]*.*'
    text = t.value.split()
    # print(text)
    # text.remove("<assign>")
    # text.remove("</assign>")
    print("<assignment>\n\t<variable>")
    print("\t\t<var_name>{}</var_name>".format(Input[word_count+1]))
    increment(1)
    print("\t</variable>\n\t<value>\n\t\t<expression>")
    print("\t\t\t<int>{}</int>".format(Input[word_count+2]))
    increment(2)
    print("\t\t</expression>\n\t</value>")

def t_NEWLINE(t):
    r'\n'
    print("",end="")

def t_UNKNOWN(t):
    r'<.*>|[ \s]'
    print(""+t.value,end="")

def t_error(t):
    print("Well you F*#ed Up Big Time:(\n I blame -->",t)

def increment(x):
    global word_count 
    word_count += x
Input_file = open('t11.pc','r')
Input = Input_file.read()
Input = Input.split()
word_count = -1
lexer = lex.lex()
fXML = open("Phase1.intXML",'r')
XML_Input = fXML.read()
lexer.input(XML_Input)
while tok := lexer.token():
    print(tok)
