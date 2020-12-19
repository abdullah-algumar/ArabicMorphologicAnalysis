import ast
from collections import defaultdict

import naftawayh.wordtag

def nlp_naf(sentence):
    word_list = sentence.split(' ')
    post_result = defaultdict(list)
    tagger = naftawayh.wordtag.WordTagger()
    for word in word_list:
        if tagger.is_noun(word):
            print(u'%s is noun' % word)
            post_result['Results'].append([word, 'noun'])
        if tagger.is_verb(word):
            print(u'%s is verb' % word)
            post_result['Results'].append([word, 'verb'])
        if tagger.is_stopword(word):
            print(u'%s is stopword' % word)
            post_result['Results'].append([word, 'stopword'])

    print(post_result)
    return post_result

# nlp_naf('يلعب الطفل بالكرة')