#标签树的上行遍历
soup=BeautifulSoup(demo, "html.parser")
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

##p
##body 
##html
##[document]
