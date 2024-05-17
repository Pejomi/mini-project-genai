import myloadlib


def get_docs_from_wiki(subject):
    lang = 'en'
    docs = myloadlib.loadWiki(subject, lang, 2)

    return docs


def get_docs_from_pdf(pdf_path):
    docs = myloadlib.loadFile(pdf_path)
    return docs
