from bs4 import BeautifulSoup


fh= open('/Users/diveshangula/localrepo/PythonInternetProgramming/assignments/week03/bloglist.html','r')
parsed = BeautifulSoup(fh)

entries = parsed.find_all('div',class_='feedEntry')


def my_function(parsed_page) :
    pgsql = []
    django =[]
    other =[]
    for e in entries :
        anchor = e.find('a')
        paragraph = e.find('p', 'discreet')
        title = anchor.text.strip()
        url = anchor.attrs['href']
        try :
            stripedPara = paragraph.text.strip()
            if 'PostgreSQL' in stripedPara :
                pgsql.append((title,url))    
            elif 'Django' in stripedPara :
                django.append((title,url))
            else :
                other.append((title,url))  
                              
        except AttributeError:
            print 'Uncategorized'
        except UnicodeEncodeError:
            print 'haha unicode Error'
    return pgsql,django,other
        
        

PostgresList,DjangoList,OrtherList = my_function(entries)


print len(PostgresList)
print type(PostgresList)
print PostgresList

print len(DjangoList)
print type(DjangoList)
print DjangoList

print len(OrtherList)
print type(OrtherList)
print OrtherList
    


