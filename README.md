#  Automated Knowledge Graph Builder

This project provides a **fully automated pipeline** that extracts entities and their relationships from unstructured text using a **Large Language Model (LLM)**, and stores them as a **visual knowledge graph** in Neo4j. It transforms scientific, technical, historical, or fictional texts into **interactive, queryable graph structures**—with **zero manual labeling** required.

---

## Demo: Knowledge Graph Visualization

![kg](https'://github.com/user-attachments/assets/872f2823-c1c7-41d1-9a2c-cb4d45338121)

![Terminal](https://github.com/user-attachments/assets/2c5a1f1c-d08c-4c9b-b930-59b20b7f4938)

##  Key Features

- **Entity and Relationship Extraction**  
  Automatically identifies people, projects, organizations, concepts, and their interconnections directly from natural text.

- **LLM-Powered Parsing**  
  Utilizes an LLM for deep, context-rich language understanding—no hand-written NLP rules needed.

- **Chunked Document Support**  
  Efficiently processes large files by splitting them into manageable sections while preserving context.

- **Graph Database Storage**  
  Stores each entity with a unique ID and human-readable name in Neo4j, enabling seamless visualization and querying.

- **Easy, Secure Configuration**  
  All credentials and configurations are handled via a `.env` file—**no hardcoded secrets**.

---

##  Tech Stack

- **Language:** Python  
- **LLM Orchestration:** LangChain  
- **LLM:** Ollama (e.g., LLaMA 3.1)  
- **Graph Database:** Neo4j  
- **Data Validation:** Pydantic  
- **Configuration Management:** python-dotenv

---

##  Project Goals

-  Automate the extraction of **knowledge graphs** (nodes/entities and edges/relationships) from raw text.
-  Leverage LLMs for **context-aware understanding**—going beyond keyword spotting.
-  Store and visualize structured data in **Neo4j** for intuitive graph exploration and querying.
-  Deliver a **fully reproducible, secure, and extensible** pipeline for researchers, devs, and demo use.












