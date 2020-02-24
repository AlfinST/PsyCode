import ply.lex as lex

tokens =("PROGRAM","UNKNOWN")

def t_PROGRAM(t):
    r'<program>[\s ]*<identifier>'
    print("<program>\n\t<program_name>{}".format(Input[word_count+2]))

def t_UNKNOWN(t):
    r'<.*>|[ \s]'
    print(t.value,end="")

def t_error(t):
    print("Well you F*#ed Up Big Time:(\n I blame -->",t)

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