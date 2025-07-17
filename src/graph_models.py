#Store your Pydantic models for nodes, relationships, and graphs
from pydantic import BaseModel, Field
from typing import List, Optional

class Node(BaseModel):
    id: str = Field(description="Unique identifier for the node (usually entity name)")
    type: str = Field(description="Category or type (e.g., Person, Technology)")

class Relationship(BaseModel):
    source: str = Field(description="ID of the source node")
    target: str = Field(description="ID of the target node")
    type: str = Field(description="Type of the relationship (e.g., 'USES', 'WORKS_WITH')")

class Graph(BaseModel):
    nodes: Optional[List[Node]]
    relationships: Optional[List[Relationship]]
