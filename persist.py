from langchain_community.vectorstores import Chroma

persist_directory = 'data2/chroma/'


def store_documents(splits, embeddings):
    # Create the vector store
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vectordb.persist()

    print("Saved count: " + str(vectordb._collection.count()))

    return vectordb


def load_documents(embeddings):
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    # You may want to verify loaded data or count entries
    print("Loaded count: " + str(vectordb._collection.count()))

    return vectordb

