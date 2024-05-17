import streamlit as st
import chunking
import load
import persist
import embedding
import llm

from streamlit_option_menu import option_menu


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


if 'links' not in st.session_state:
    st.session_state.links = {"Wikipedia": [], "YouTube": []}

if 'files' not in st.session_state:
    st.session_state.files = {"Text": [], "PDF": [], "CSV": []}


def home_page():
    st.title(f"{selected}")


def load_link_page():
    st.title(f"{selected}")

    # Dropdown menu to select the type of data source
    link = st.selectbox("Select link source type", ["Wikipedia", "YouTube"])

    if link == "Wikipedia":
        st.write("Insert a Wikipedia link to extract the text from it.")
    elif link == "YouTube":
        st.write("Insert a YouTube link to fetch the video data.")

    new_link = st.text_input("Enter a link")

    # Button to add the link
    if st.button("Add"):
        if new_link:
            st.session_state.links[link].append(new_link)
            st.success("Link added successfully!")

    if any(st.session_state.links.values()):
        st.write("## Added Links")
        for link_type, links in st.session_state.links.items():
            if links:
                st.write(f"### {link_type}")
                st.markdown("---")
                for i, link in enumerate(links):
                    col1, col2 = st.columns([8, 1])
                    with col1:
                        st.write("•" + link)
                    with col2:
                        if st.button("❌", key=f"remove_{link_type}_{i}"):
                            st.session_state.links[link_type].pop(i)
                            st.experimental_rerun()


def load_data_page():
    st.title(f"{selected}")

    # Dictionary to store files
    if 'files' not in st.session_state:
        st.session_state.files = {"Text": [], "PDF": [], "CSV": []}

    # Dropdown menu to select the type of file
    file_type = st.selectbox("Select file type", ["Text", "PDF", "CSV"])

    if file_type == "Text":
        st.write("Upload a text file.")
        accept_file_types = ".txt"
    elif file_type == "PDF":
        st.write("Upload a PDF file.")
        accept_file_types = ".pdf"
    elif file_type == "CSV":
        st.write("Upload a CSV file.")
        accept_file_types = ".csv"

    uploaded_file = st.file_uploader("Upload file", accept_multiple_files=False, type=accept_file_types)

    # Button to add the file
    if st.button("Add"):
        if uploaded_file is not None:
            st.session_state.files[file_type].append(uploaded_file)
            st.success("File added successfully!")

    if any(st.session_state.files.values()):
        st.write("## Added Files")
        for file_type, files in st.session_state.files.items():
            if files:
                st.write(f"### {file_type}")
                st.markdown("---")
                for i, file in enumerate(files):
                    col1, col2 = st.columns([8, 1])
                    with col1:
                        st.write(file.name)
                    with col2:
                        if st.button("❌", key=f"remove_{file_type}_{i}"):
                            st.session_state.files[file_type].pop(i)
                            st.experimental_rerun()


def clean_data_page():
    st.title(f"{selected}")


def transform_data_page():
    st.title(f"{selected}")


def llm_page():
    st.title(f"{selected}")

    # Introduction
    st.write(
        "Welcome to the Large Language Model (LLM) page! LLMs are powerful AI models capable of generating human-like text.")

    # Example outputs
    st.write("### Example Outputs:")
    st.write("- LLM output example 1")
    st.write("- LLM output example 2")

    # Custom input
    st.write("### Generate LLM Output:")
    input_text = st.text_area("Enter your text here", height=100)
    if st.button("Generate Output"):
        # Call LLM function to generate output based on input_text
        generated_output = generate_llm_output(input_text)
        st.write("### Generated Output:")
        st.write(generated_output)

    # Parameter configuration (optional)
    # temperature = st.slider("Temperature", 0.1, 1.0, 0.5)
    # max_tokens = st.slider("Max Tokens", 50, 500, 200)
    # top_p = st.slider("Top P", 0.1, 1.0, 0.9)


def generate_llm_output(input_text):
    # Placeholder function to generate LLM output
    # You can replace this with your actual LLM model or API call
    # For simplicity, just return the input text reversed
    return input_text[::-1]


st.header("Mini Project 3 - NLP, NLU, GenAi")

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Load Link", "Load Data", "Clean Data", "Transform Data", "LLM"],
        icons=["1-square", "2-square", "3-square", "4-square", "5-square", "6-square"],
        menu_icon="folder",
        default_index=0,
    )
if selected == "Home":
    home_page()
elif selected == "Load Link":
    load_link_page()
elif selected == "Load Data":
    load_data_page()
elif selected == "Clean Data":
    clean_data_page()
elif selected == "Transform Data":
    transform_data_page()
elif selected == "LLM":
    llm_page()
