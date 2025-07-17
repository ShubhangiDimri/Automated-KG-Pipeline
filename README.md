Overview
This project provides a fully automated pipeline that extracts entities and their relationships from unstructured text, utilizing a Large Language Model (LLM) and stores this data as a visual knowledge graph in Neo4j. This enables rapid transformation of scientific, technical, historic, or fictional texts into interactive, queryable graph structures—no manual data labeling required.

Tech Stack:

Python

Ollama (LLaMA 3 or other local LLM)

Neo4j Graph Database

LangChain (for text chunking/LLM support)

Pydantic (for structured output validation)

dotenv (for environment management)

Project Goals
Automate the extraction of knowledge graphs (nodes/entities and edges/relationships) from plain text documents.

Leverage LLMs for context-aware understanding of natural language, going beyond simple keyword/entity extraction.

Store structured graphs in Neo4j, so you can visually explore, query, and analyze the results with ease.

Provide a fully reproducible, extensible pipeline for teams, researchers, or demo purposes.

Features
Entity and relationship extraction: Automatically finds important people, projects, organizations, concepts, and their connections, directly from natural text.

LLM-powered parsing: Uses an LLM for context-rich understanding—no hand-written NLP rules.

Chunked document support: Handles large files by splitting them into manageable sections to preserve relational context.

Graph database storage: Every entity is stored with both a unique id and a human-friendly name for seamless Neo4j visualization. 

Easy, secure configuration: All credentials are managed via an .env file; nothing is hardcoded.






