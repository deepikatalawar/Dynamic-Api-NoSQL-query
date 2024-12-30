from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class QueryRequest(BaseModel):
    collection: str
    filter: Optional[Dict[str, Any]] = {}
    projection: Optional[Dict[str, int]] = {}
    limit: Optional[int] = 10
    skip: Optional[int] = 0
    sort: Optional[Dict[str, int]] = {}
    aggregation: Optional[List[Dict[str, Any]]] = None
