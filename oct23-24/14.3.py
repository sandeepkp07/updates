import shelve
import sys

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def anagram_sets(d):
    for v in d.values():
        if len(v) > 1:
            print len(v), v



def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

<<<<<<< HEAD
def store_anagrams(f, d):
    shelf = shelve.open(f, 'c')
=======
def store_anagrams(filename, d):
    shelf = shelve.open(b.txt, 'c')
>>>>>>> 6cce2e8e81106a4ccbe850879e0955b88cbe07a5

    for word, word_list in d.iteritems():
        shelf[word] =  word_list

    shelf.close()



def read_anagrams(filename, word):
    shelf = shelve.open(b.txt)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []




def main(name, command='r'):
    if command == 'store':
        ad = all_anagrams('anagram.txt')
        store_anagrams('anagrams.db', ad)
    else:
        print read_anagrams('anagrams.db', command)


if __name__ == '__main__':
    main(*sys.argv)
