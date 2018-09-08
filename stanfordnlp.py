from stanfordcorenlp import StanfordCoreNLP
import nltk, re, pprint

nlp = StanfordCoreNLP(r'C:\Users\Mahshid\Downloads\Compressed\stanford-corenlp-full-2018-02-27\stanford-corenlp-full-2018-02-27')
#"^\d(\.\d{1,2}){0,2}(\.x){0,1}"
sentence = 'Multiple SQL injection vulnerabilities in trackback.php in myWebland myBloggie 2.1.4 and earlier allow remote attackers to execute arbitrary SQL commands via the (1) title, (2) url, (3) excerpt, or (4) blog_name parameters. '
print ('Tokenize:', nlp.word_tokenize(sentence))
print ('Part of Speech:', nlp.pos_tag(sentence))
print ('Named Entities:', nlp.ner(sentence))
print ('Constituency Parsing:', nlp.parse(sentence))
print ('Dependency Parsing:', nlp.dependency_parse(sentence))

"""
#NLP Book REGEX extracting#
A tag pattern is a sequence of part-of-speech tags delimited using angle brackets
rule says that an NP chunk should be formed whenever the chunker finds an optional determiner (DT) followed by any number of adjectives (JJ)
and then a noun (NN). Using this grammar, we create a chunk parser
"""

###*********find all w.w example: item.php*********###
match = re.findall('[a-zA-Z]+\.[a-zA-Z]+', sentence)
print (match)
sentences = nlp.pos_tag(sentence)
grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentences)
print (result)
result.draw()

#####Only NP: create a tree by giving a node label and a list of children####
tree1 = nltk.Tree('NP', result)
print (tree1)

#####traverse tree###

# def traverse(t):
#     try:
#         t.label()
#     except AttributeError:
#         print(t, end=" ")
#     else:
#         # Now we know that t.node is defined
#         print('(', t.label(), end=" ")
#         for child in t:
#             traverse(child)
#         print(')', end=" ")

# traverse(tree1)

nlp.close()