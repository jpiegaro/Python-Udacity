# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    split=content.split()
    for e in split:
        add_to_index(index,e,url)
        


add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


#****A secondary alternate method to do something similar I mocked up.
def add_page_to_index(url,content):
    stage1=content.split()
    n=len(stage1)
    stage2=[url]*n
    stage3=map(list,zip(stage1,stage2))
    for e in stage3:
        e[1]=[e[1]]
    print stage3
	
add_page_to_index('http://roma.org','Hello I am Joel.')