Automated Knowledge Graph Builder
This project provides a fully automated pipeline that extracts entities and their relationships from unstructured text, utilizing a Large Language Model (LLM), and stores this data as a visual knowledge graph in Neo4j. This enables rapid transformation of scientific, technical, historic, or fictional texts into interactive, queryable graph structures—no manual data labeling required.

Demo: Knowledge Graph Visualization
(Here you can add a screenshot of your final graph)

Key Features
Entity and Relationship Extraction: Automatically finds important people, projects, organizations, concepts, and their connections, directly from natural text.

LLM-Powered Parsing: Uses an LLM for context-rich understanding—no hand-written NLP rules.

Chunked Document Support: Handles large files by splitting them into manageable sections to preserve relational context.

Graph Database Storage: Every entity is stored with both a unique ID and a human-friendly name for seamless Neo4j visualization.

Easy, Secure Configuration: All credentials are managed via an .env file; nothing is hardcoded.

Tech Stack
Language: Python

LLM Orchestration: LangChain

LLM: Ollama (LLaMA 3 or other local LLM)

Database: Neo4j Graph Database

Data Validation: Pydantic

Configuration: python-dotenv

Project Goals
Automate the extraction of knowledge graphs (nodes/entities and edges/relationships) from plain text documents.

Leverage LLMs for context-aware understanding of natural language, going beyond simple keyword extraction.

Store structured graphs in Neo4j so you can visually explore, query, and analyze the results with ease.

Provide a fully reproducible and extensible pipeline for researchers, teams, or demo purposes.









