from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date
from database import engine, get_db
import models
import schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Accounting API")

@app.get("/")
async def root():
	return {"message": "Hello World! The AI Agent Accounting server is running."}

@app.get("/health")
async def health_check():
	return {"status": "healthy", "service": "Backend is operational"}

@app.post("/expenses/")
def log_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
	new_expense = models.Expense(
		amount=expense.amount,
		category=expense.category,
		description=expense.description,
		date=expense.date or date.today()
	)
	db.add(new_expense)
	db.commit()
	db.refresh(new_expense)
	return {"message": "Expense logged successfully!", "expense": new_expense}
	
@app.get("/expenses/")
def get_expenses(db: Session = Depends(get_db)):
	expenses = db.query(models.Expense).all()
	return expenses