from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest
from app.database import get_collection
from typing import List

router = APIRouter()

@router.post("/query")
async def query(request: QueryRequest):
    try:
        # Validate limit and skip values
        if request.limit < 1:
            raise HTTPException(status_code=400, detail="Limit must be greater than 0.")
        if request.skip < 0:
            raise HTTPException(status_code=400, detail="Skip must be 0 or greater.")
        
        # Get the MongoDB collection based on user input
        collection = get_collection(request.collection)

        # If aggregation pipeline is provided, use it
        if request.aggregation:
            result = collection.aggregate(request.aggregation)
        else:
            # Perform a standard query with filter, projection, and sorting
            result = collection.find(request.filter, request.projection)\
                                .sort(list(request.sort.items()))\
                                .skip(request.skip)\
                                .limit(request.limit)

        # Convert the result (cursor) to a list and return the response
        data = list(result)
        return {"status": "success", "data": data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
