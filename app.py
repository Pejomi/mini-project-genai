import streamlit as st
import chunking
import load
import persist
import embedding
import llm


def main():
    documents = []
    wiki_docs = load.get_docs_from_wiki("Traffic accidents")
    pdf_docs = load.get_docs_from_pdf("traffic_accident.pdf")

    documents.extend(wiki_docs)
    documents.extend(pdf_docs)

    splits = chunking.get_splits(documents)

    vectordb = persist.store_embeddings(splits, embedding.get_embeddings())
    # vectordb = persist.load_embeddings(embedding.get_embeddings())

    question = "What is the most contributing factor in accidents?"
    # question = "What is the most common type of traffic accident?"

    answer = llm.ask(vectordb, question)

    print(answer)

    st.title("Mini Project 3: NLP, NLU and GenAi")


if __name__ == "__main__":
    main()
