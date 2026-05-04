from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
	amount: float
	category: str
	description: str
	date: date
	
class ExpenseInput(BaseModel):
	text: str
	
class ExpenseExtraction(BaseModel):
	amount: float
	category: str
	description: str
	date: str