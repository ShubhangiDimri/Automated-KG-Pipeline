# Manage connections and writes to Neo4j.
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv
from graph_models import Graph

load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def get_driver():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        driver.verify_connectivity()
        print(" Successfully connected to Neo4j.")
    except Exception as e:
        print(f" Failed to connect to Neo4j: {e}")
        exit()
    return driver

# Inside src/neo4j_interface.py
def store_graph_in_neo4j(driver, graph):
    """
    Stores graph nodes and relationships in Neo4j using standard Cypher.
    This version does NOT require the APOC plugin.
    """
    if not graph or (not graph.nodes and not graph.relationships):
        print("Graph is empty. Nothing to store.")
        return
        
    with driver.session() as session:
        # 1. Create Nodes
        if graph.nodes:
            for node in graph.nodes:
                session.run(
                    """
                    MERGE (n:Entity {id: $id})
                    SET n.name = $id, n.type = $type
                    """,
                    id=node.id, type=node.type
                )
        
        # 2. Create Relationships (<<< YEH SAHI LOGIC HAI BINA APOC KE)
        if graph.relationships:
            for rel in graph.relationships:
                # Relationship type ko Cypher ke liye safe banayein (e.g., "IS PART OF" -> "IS_PART_OF")
                # Yeh zaroori hai kyunki relationship types mein space nahi ho sakta.
                rel_type = rel.type.replace(" ", "_").upper()

                # Standard MERGE query ka istemaal karein
                # Hum f-string ka istemaal sirf rel_type ke liye kar rahe hain, jo safe hai.
                # Baaki saara data ($source_id, $target_id) parameters ke through jaata hai taaki security bani rahe.
                query = f"""
                MATCH (a:Entity {{id: $source_id}})
                MATCH (b:Entity {{id: $target_id}})
                MERGE (a)-[r:`{rel_type}`]->(b)
                RETURN type(r)
                """
                session.run(
                    query,
                    source_id=rel.source, 
                    target_id=rel.target
                )
    print(" Graph data successfully stored in Neo4j.")


