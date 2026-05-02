from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
	amount: float
	category: str
	description: str
	date: Optional[date] = None