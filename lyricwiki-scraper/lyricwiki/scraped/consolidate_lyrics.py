import csv, math, string, sys
from nltk.corpus import stopwords

#Increases field size limit
csv.field_size_limit(1000000000)

def main (document):
    with open(document, 'rb') as csvfile:
        docreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        with open('alllyricsbyartist.csv', 'a') as f:
            docwriter = csv.writer(f, delimiter=',')
            lyrics = ''
            for row in docreader:
                artist = row[1]
                song = row[2]
                clean_song = clean_text(song)
                for word in clean_song:
                    lyrics += word + ' '
            docwriter.writerow([artist, lyrics])
            print "Done with " + document

def clean_text (text):
    lowercase_text = text.lower()
    unhyphenated = string.replace(lowercase_text, "-", " ")
    printable = filter(lambda x: x in string.printable, unhyphenated)
    spaced_commas = string.replace(printable, ",", ", ")
    n_standardize = string.replace(spaced_commas, "niggaz", "niggas")
    unpunctuated_text = string.translate(n_standardize, None, string.punctuation)
    split_text = unpunctuated_text.split()
    rapwords = ['rapgenius.com', 'chorus', 'verse', '2x', '3x', '4x', '5x', '6x', '7x', '8x', 
        '9x', '10x,' 'hook', 'intro', 'outro', 'u', '2', '4', 'em', 'dem', 'ya', 'hes', 'shes', 'im', 'theyre', 'youll', 'ima', 
        'iim', 'simi', 'hunh']
    stoplist = stopwords.words('english') + rapwords
    important_text = filter(lambda x: x not in stoplist, split_text)
    return important_text

if __name__ == "__main__": main(sys.argv[1])