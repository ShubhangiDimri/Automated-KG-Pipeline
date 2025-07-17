# Handle LLM prompt engineering and response parsing
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
from graph_models import Graph

def extract_graph_with_ollama(text_chunk: str):
    llm = ChatOllama(
        model=os.getenv("OLLAMA_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        temperature=0.0
    ).with_structured_output(Graph)

    # <<< PROMPT MEIN SUDHAAR KIYA GAYA HAI
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a top-tier algorithm for extracting information in structured formats.
From the given text, extract entities and their relationships as a knowledge graph.

### Instructions
- **Nodes**: Each node must have a unique `id` representing the actual name of the entity (e.g., "Marie Curie", "Radium", "Poland"). Each node must also have a `type` (e.g., "Person", "Element", "Country").
- **Relationships**: Define directed connections between nodes. The `source` and `target` must match one of the node `id`s. The `type` should describe the relationship (e.g., "DISCOVERED").

### Example
Text: "Marie Curie, born in Poland, discovered the element Radium. She collaborated with her husband, Pierre Curie, on her research."
JSON Output:
{{
  "nodes": [
    {{"id": "Marie Curie", "type": "Person"}},
    {{"id": "Poland", "type": "Country"}},
    {{"id": "Radium", "type": "Element"}},
    {{"id": "Pierre Curie", "type": "Person"}}
  ],
  "relationships": [
    {{"source": "Marie Curie", "target": "Poland", "type": "BORN_IN"}},
    {{"source": "Marie Curie", "target": "Radium", "type": "DISCOVERED"}},
    {{"source": "Marie Curie", "target": "Pierre Curie", "type": "COLLABORATED_WITH"}}
  ]
}}
"""),
        ("human", "Here is the text to analyze:\n\n{input_text}")
    ])

    chain = prompt | llm
    try:
        print(" Invoking Ollama model for graph extraction.")
        result = chain.invoke({"input_text": text_chunk})
        return result
    except Exception as e:
        print(f" Error invoking Ollama or parsing the output: {e}")
        return None

