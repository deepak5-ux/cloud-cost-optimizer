# app/schemas/input_schema.py

from pydantic import BaseModel

class WorkloadRequest(BaseModel):
    workload_type: str
    traffic_level: str
    budget: str

    class Config:
        schema_extra = {
            "example": {
                "workload_type": "Web App",
                "traffic_level": "Low",
                "budget": "Low"
            }
        }
