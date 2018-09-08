from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'C:\Users\Mahshid\Downloads\Compressed\stanford-corenlp-full-2018-02-27\stanford-corenlp-full-2018-02-27')

sentence = 'Buffer overflow in NFS mountd gives root access to remote attackers, mostly in Linux systems.'
print ('Tokenize:', nlp.word_tokenize(sentence))
print ('Part of Speech:', nlp.pos_tag(sentence))
print ('Named Entities:', nlp.ner(sentence))
print ('Constituency Parsing:', nlp.parse(sentence))
print ('Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()