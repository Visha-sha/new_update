import xml.etree.ElementTree as ET
xml_file="etree.xml"

tree=ET.parse(xml_file)
root=tree.getroot()

print(root.tag.center(40,"*"))

for child in root:
    print("*"*20)
    print(child.tag,child.attrib['title'])
    for i in range(0,len(child)):
        print("{0}:{1}".format(child[i].tag,child[i].text))
