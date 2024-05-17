import myutils
import importlib
from myutils import chunkDocs, langDetect, wordCloud


def get_splits(docs):
    return myutils.chunkDocs(docs, 350)
