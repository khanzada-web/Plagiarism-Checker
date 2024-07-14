import spacy

nlp=spacy.load("en_core_web_md")
with open('D:\Cubex_interShip_projects\Plagiarism Checker\File1.txt','r') as File:
    context=File.read()

with open('D:\Cubex_interShip_projects\Plagiarism Checker\File2.txt','r') as File2:
    context2=File2.read()


doc1=nlp(context)
doc2=nlp(context2)

similarity = doc1.similarity(doc2)

percentage=similarity*100

print("Similarity In Percentage:",percentage )
