from pydantic import BaseModel, Field

class AboutProduct(BaseModel):
    name: str = Field(description="Product name")
    description: str = Field(description="Product description")
    price_usd: int = Field(description="Product price in USD")
