from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class ExpenseBase(BaseModel):
	amount: float
	category: str
	merchant: str
	description: Optional[str] = None
	date: date

class ExpenseCreate(ExpenseBase):
	model_config = ConfigDict(from_attributes=True)
	
class ExpenseInput(BaseModel):
	text: str
	
class ExpenseExtraction(BaseModel):
	amount: float
	category: str
	description: str
	merchant: str
	date: str