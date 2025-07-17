#Read input documents and split text into manageable chunks.


from langchain.text_splitter import RecursiveCharacterTextSplitter

def read_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def split_text(text, chunk_size=512, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
