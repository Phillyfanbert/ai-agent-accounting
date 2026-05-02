from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from database import Base

class Expense(Base):
	__tablename__ = "expenses"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Float, nullable=False)
	merchant = Column(String, index=True)
	category = Column(String, index=True)
	date = Column(Date, nullable=False)
	description = Column(String, nullable=True)
	
class Subscription(Base):
	__tablename__ = "subscriptions"
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True, nullable=False)
	monthly_cost = Column(Float, nullable=False)
	billing_cycle = Column(String, default="monthly")
	is_active = Column(Boolean, default=True)
	cheaper_alternative_found = Column(Boolean, default=False)
	alternative_details = Column(String, nullable=True)