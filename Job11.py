from xml.dom import minidom

file = minidom.parse('./File_job11/domains.xml')


domains = file.getElementsByTagName("table")
nbr = len(domains)

print("There is",nbr, "domain names on the XML file")
