# Open a file
fo = open('text.txt', 'w')

#Get some info
print('Name: ', fo.name)
print('is closed: ', fo.closed)
print('Opening mode: ', fo.mode)
# Write to file
fo.write('I love Python')
fo.write(' and Javascript')
# close file
fo.close()

# Open to append
fo = open('text.txt', 'a')
fo.write(' I also like php')
fo.close()

#read from file
fo = open('text.txt', 'r+')
text = fo.read()
print(text)
fo.close()

#create file
fo = open('text2.txt', 'w+')
fo.write('This is my new file')
fo.close()