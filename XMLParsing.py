import xml.etree.ElementTree as ET

def RecursiveTagging(Tree,i):
    children = list(Tree)
    tag = Tree.tag
    txt = Tree.text
    if len(children) == 0:
        if Tree.text == None:
            print("{}<{}/>".format("   "*i,tag))
        else:
            print("{}<{}>{}</{}>".format("   "*i,tag,txt,tag))
    else:
        print("{}<{}>".format("   "*i,tag))
        # to go deeper
        for child in children:
            RecursiveTagging(child,i+1)
        # after this is end tag
        print("{}</{}>".format("   "*i,tag))
        
if __name__ == "__main__":    
    with open("Answer.xml") as F:
        tree = ET.parse(F)
    root = tree.getroot()
    # for child in root:
    #     print(child)
    #     for grandchildren in child:
    #         print(grandchildren)
    #     # print()
    print("\n\n","*"*10)
    RecursiveTagging(root,0)
