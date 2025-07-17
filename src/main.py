# Orchestrate the overall workflow.
import os
import os
from dotenv import load_dotenv
from data_splitter import read_document, split_text
from ollama_extractor import extract_graph_with_ollama
from neo4j_interface import get_driver, store_graph_in_neo4j

if __name__ == "__main__":
    load_dotenv()
    driver = get_driver()
    text = read_document("your_document.txt")
    print(f" Document loaded. Length: {len(text)} characters.")
    chunks = split_text(text)
    print(f" Text split into {len(chunks)} chunk(s).")

    for i, chunk in enumerate(chunks):
        print(f"\n--- Processing Chunk {i+1}/{len(chunks)} ---")
        print(f" Chunk Text:\n{chunk}\n")
        graph = extract_graph_with_ollama(chunk)
        if graph:
            print(" Extracted Graph:")
            # Updated for Pydantic v2+
            print(graph.model_dump_json(indent=2))
            store_graph_in_neo4j(driver, graph)
            print(" Graph chunk stored successfully.")
        else:
            print(" No graph data could be extracted from this chunk.")

    driver.close()
    print("\n All chunks processed. Graph construction complete.")


