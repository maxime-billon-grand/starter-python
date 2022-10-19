
# ========= USING MINIDOM ===========
from xml.dom import minidom

file = minidom.parse('./File_job11/domains.xml')


domains = file.getElementsByTagName("table")
nbr = len(domains)

print("(Minidom method) - There is",nbr, "domain names on the XML file")


# ========= USING NO IMPORT ===========
countAll = str(input("Do you want to count the domain names in the first part of the file ? (Y/N):"))

nbr=0
match countAll:
    case "Y":
        for line in open ('./File_job11/domains.xml', "r"):
            if "http" in line or '"domain">' in line:
                nbr+=1
    case "N":
        for line in open ('./File_job11/domains.xml', "r"):
            if '"domain">' in line:
                nbr+=1
    case _:
        countAll = str(input("You didnt' enter a valid answer\nDo you want to count the domain names in the first part of the file ? (Y/N):"))




print("(no import method) - There is", nbr, "domain names on the XML file")



