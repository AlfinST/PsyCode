import json

text 	= lambda x:x[1]
tag 	= lambda x:x[0]	

# def nextObj(Object):
# 	for i in Object:
# 		Object.pop()
# 		yield Object
		
def TagLabel(current,source):
	#	Input	:	Takes the next tag_Obj along with where its from
	#	Activity: 	Source specifics and tags the basic tagging
	#	Output	: 	Depending on where the soure is, different taging policy
	###################################################################
	if source == "function":
		specialDict={"OpenOperator":"beg","CloseOperator":"end","comma":"endbeg"}
		t = tag(current)
		txt = text(current)
		if t in specialDict:
			return specialDict[t]		
		TagDict = {"identifier":Variable,"constant":Number,"operator":Operator}
		TagDict[t](txt)
		return "000"

def Variable(var_name):
	#	Input	:	Takes the variable name
	#	Activity: 	Prints the variable tag
	#	Output	: 	<variable>
	#					<variable_name>var_name<variable_naem>
	###################################################################
	print("<variable>\n<variable_name>{}</variable_name>\n</variable>".format(var_name))
	# if nextIs == "index"
def Number(num):
	#	Input	:	Takes the constant to be printed
	#	Activity: 	Prints the constant tag
	#	Output	: 	<constant>num<\constant>
	###################################################################
	print("<constant>{}</constant>".format(num))

def Operator(op):
	#	Input	:	Takes the operator to be printed
	#	Activity: 	Prints the operator tag
	#	Output	: 	<operator>num<\operator>
	###################################################################
	print("<operator>{}<opertator>".format(op))

def Expression(controlString):
	#	Input	:	Takes a string to check if exp begins or ends
	#	Activity: 	Prints the either closing/starting exp tag 
	# 				acts depending on ControlString 
	#	Output	: 	<operator>num<\operator>
	###################################################################
	if	controlString.startswith("end"):
		print("</exp>")
	if controlString.endswith("beg"):
		print("<exp>")

	
def Function(line):
	
	#	Input	:	Json object["data"]
	#	Activity: 	Takes first object and assigns it as function name
	#				Additonal objets are to be taged as arguemnts 
	#	Output	:	<function>
	#					<function_name> funciton_name<funciton_name>
	#					<args> ... </args>
	#				</function>
	#####################################################################
	print("<function>")
	function_name = text(line[0])
	
	print("<function_name>{}<function_name>".format(function_name))
	print("<args>")
	newArg= "Clear"
	for nextIndex in range(1,len(line)):
		Expression(newArg)
		newArg = TagLabel(current=line[nextIndex],source="function")			
		print("</args>")
	print("</function>")
	pass

def Assignment(line):
	#	Input	:	tag_Obj
	#	Activity:	tags the variable and vlaue
	#	Output	:	<assignment>
	#					<variable>
	#						<var_name>var_name<var_name>
	#						<index?>
	#					</variable>
	#					<value>
	#						....
	#					</value>
	# print("Assignment stuff here")
	print("<assignment>")
	print("<variable>")
	var_name = line[0][1]
	print("<var_name>{}</var_name>".format(var_name))
	if line[1][0]
	pass

def If(line):
	#	Input
	#	Activity
	#	Output

	print("If done here")
	pass

def Else(line):
	#	Input
	#	Activity
	#	Output

	print("Else Im with the other guy")
	pass

def Print(line):
	#	Input
	#	Activity
	#	Output

	print("Print You need me trust me")
	pass

def While(line):
	#	Input
	#	Activity
	#	Output

	print("While your at it")
	pass

if __name__ == "__main__":
	#	Input: Table.json file
	#	Activity: tags accodringly
	#	Output: Fully tagged XML file

	with open("Table.json") as jsonFile:
		ParsedTree = json.load(jsonFile)
	
	TagDict = {"function":Function,"assignment":Assignment,"if":If,\
				"else":Else,"print":Print,"while":While}

	for line in ParsedTree:
		# print(line,end="\n\n")
		# tagLine = " ".join([tag[0] for tag in line["data"]])
		# print(tagLine,end="\n\n")
		t = line["tag"]
		txt = line["data"]
		# for i in range(2):
		# 	print("something",list(nextObj(line["data"][0])))
		TagDict[t](txt)
		print("="*10)
