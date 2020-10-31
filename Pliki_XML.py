#Zadanie XML
from xml.dom import minidom

##########		parser DOM		##########
def print_xml_data():
	for i in nodes:
		print("---------------------------------------------------")
		print("[", i.getElementsByTagName("imie")[0].getAttribute("foo"), "]")
		print(i.getElementsByTagName("imie")[0].nodeName, ":	", i.getElementsByTagName("imie")[0].childNodes[0].toxml())
		print(i.getElementsByTagName("nazwisko")[0].nodeName, ":	", i.getElementsByTagName("nazwisko")[0].childNodes[0].toxml())
		print(i.getElementsByTagName("telefon")[0].nodeName, ":	", i.getElementsByTagName("telefon")[0].childNodes[0].toxml())
		print(i.getElementsByTagName("email")[0].nodeName, ":	", i.getElementsByTagName("email")[0].childNodes[0].toxml())
		print("---------------------------------------------------")


DOMTree = minidom.parse('example_file_x_m_l.xml')
nodes = DOMTree.getElementsByTagName("osoba")

print_xml_data()

nodes[0].getElementsByTagName("email")[0].childNodes[0].nodeValue = "new_mail@gmail.com"
nodes[1].getElementsByTagName("email")[0].childNodes[0].nodeValue = "new_mail@onet.pl"
nodes[2].getElementsByTagName("email")[0].childNodes[0].nodeValue = "new_mail@outlook.com"

print_xml_data()

with open("New_file_x_m_l.xml", "w") as file:
	DOMTree.writexml(file)
file.close()



##########		parser SAX		##########
import xml.sax

parser = xml.sax.make_parser()
parser.parse('example_file_x_m_l.xml')
