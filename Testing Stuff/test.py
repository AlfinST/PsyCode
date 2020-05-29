import ply.lex as lex
import json

debugMode = False

def addToLine(tagPair):
	global jsonLine
	jsonLine.append(tagPair)

def setSemantics(semantic):
	global lineSemantic
	lineSemantic = semantic
	
def addToTable():
	global intend_level
	global jsonObj
	global jsonLine
	global lineSemantic
	objDict = dict()
	objDict["intendLevel"] = intend_level
	objDict["tag"] = lineSemantic
	objDict["data"] = jsonLine
	jsonObj.append(objDict)

tokens = ("ISGREATER","ISGREQ","EQUALS","VAR","OPERATOR","CONSTANT","IF","ELSE","STRING",\
		"FUNCTION","PROGRAM","ARGS","ASSIGNMENT","IDENTIFIER","SPACES",\
		"NEWLINE","INPUT","TO","WHILE")
#Direct Replacemet

def t_VAR(t):
	r'[vV]ariable|to'
	if debugMode:
		print("",end="")

def t_WHILE(t):
	r'while'
	if debugMode:
		print("<while>",end="")
	setSemantics("while")

def t_INPUT(t):
	r'ok'
	if debugMode:
		print("<input>")

def t_TO(t):
	r'\sto'
	addToLine(("=",t.value))
	if debugMode:
		print("=",end="")

def t_ISGEQ(t):
	r'is\sgreater\sthan\sor\sequal\sto'
	if debugMode:
		print("<boolOp>",end="")
	addToLine(("boolOp","ge"))

def t_ISGREATER(t):
	r'is\s[gG]reater\sthan'
	if debugMode:
		print("<boolOp>",end="")
	addToLine(("boolOp","g"))

def t_ISLEQ(t):
	r'is\s[lL]ess[er]*\sthan\sor\sequal\sto'
	if debugMode:
		print("<boolOp>",end="")
	addToLine(("boolOp","le"))

def t_ISLESSER(t):
	r'is\s[lL]ess[er]*\sthan'
	if debugMode:
		print("<boolOp>",end="")
	addToLine(("boolOp","l"))

def t_ASSIGNMENT(t):
	r'set|[Aa]ssign|initiali[zs]e'
	if debugMode:
		print("<assign>",end="")
	# addToLine(("assign",t.value))
	setSemantics("assignment")
	#return t

def t_EQUALS(t):
	r'=|[eE]quals|to|as'
	if debugMode:
		print('= ',end ="")
	addToLine(("=",t.value))
	setSemantics("assignment")
	#return t

def t_PRINT(t):
	r'[Pp]rint'
	if debugMode:
		print("<print>",end="")
	setSemantics("print")

def t_RETURN(t):
	r'[Rr]eturn'
	if debugMode:
		print("<return>",end="")
	setSemantics("return")
	addToLine(("return",t.value))

#Top level stuff
def t_FUNCTION(t):
	r'[Ff]unction'
	if debugMode:
		print("<function>",end ="")
	# addToLine(("function",t.value))
	setSemantics("function")
	#return t

def t_PROGRAM(t):
	r'[pP]rogram'
	# print("\ttoken:program:",t,"\n")
	if debugMode:
		print("<program>",end="")
	# addToLine(("program",t.value))
	setSemantics("program")
	#return t

def t_IF(t):
	r'[iI]f'
	if debugMode:
		print("<if>",end="")
	# addToLine(("if",t.value))
	setSemantics("if")

def t_ELSE(t):
	r'[Ee]lse'
	if debugMode:
		print("<else>",end="")
	# addToLine(("else",t.value))
	setSemantics("else")


#Mid level Stuff

def t_BOOLOPERATOR(t):
	r'>=|<=|!=|<|>|='
	if debugMode:
		print("<boolOp>",end="")
	boolDict ={"<":"l",">":"g","==":"eq",\
				"<=":"le",">=":"ge"}
	addToLine(("boolOp",boolDict[t.value]))

def t_OPERATOR(t):
	r'\+|\-|\\|\*\*|\*'
	if debugMode:
		print("<operator>",end="")
	addToLine(("operator",t.value))
	#return t

def t_CONSTANT(t):
	r'[0-9]+'
	if debugMode:
		print("<constant>",end="")
	addToLine(("constant",t.value))
	#return t

#Bottom level 
def t_STRING(t):
	r'\"(\\.|[^"\\])*\"'
	if debugMode:
		print("<string>",end="")
	addToLine(("string",t.value))
	#return t

def t_IDENTIFIER(t):
	r'[a-zA-Z][0-9a-zA-Z_]*'
	# print("\ttoken:identifier",t,"\n")
	if debugMode:
		print("<identifier>",end ="")
	addToLine(("identifier",t.value))
	#return t

def t_ARGS(t):
	r'\(.*\)'
	if debugMode:
		print("<args>",end=" ")
	addToLine(("args",t.value))
	#return t

def t_NEWLINE(t):
	r'\n'
	if debugMode:
		print(t.value,end="")
	addToTable()

def t_SPACES(t):
	r'\s'
	if debugMode:
		print(t.value,end="")


def t_UNKNOWN(t):
	r'.*[\(\)=+<]'
	if debugMode:
		print("$",t,end ="")
	# addToLine(t.value)
	return 

def t_error(t):
	if debugMode:
		print(t,"\tunaccounted for\n\n",t,"\n\n")

def intendChecker(line,intend_level):
	new_intend_level = 0
	for i in line:
		if i=='\t':
			new_intend_level+=1
		else:
			break
	if debugMode:
		print(new_intend_level,end=":")
	if new_intend_level > intend_level:
		if debugMode:
			print("\t"*(new_intend_level)+"<body>")
		if debugMode:
			print(new_intend_level,end=":")
	count = 0
	while (new_intend_level+count) < intend_level:
		if debugMode:
			print("\t"*(intend_level-count),"<done></done>")
			print("\t"*(intend_level-count),"</body>")
		count+=1

	return new_intend_level

if __name__ == "__main__":
	lexer = lex.lex()
	with open("t1.pc","r") as f:
		linebyline = f.readlines()
		intend_level = 0
		jsonObj = list()
		for line in linebyline:
			# print(line)
			lineSemantic = ""
			jsonLine = list()
			intend_level = intendChecker(line,intend_level)
			lexer.input(line)
			# print("\t"*intend_level,end="")
			while tok:= lexer.token():
				# json_file.append(tok.value)
				pass
		with open("Table.json",'w') as table:
			json.dump(jsonObj,table,indent=4)
	
	for line in jsonObj:
		if debugMode:
			print(line["data"])
		# if debugMode:
		# 	print(i)

