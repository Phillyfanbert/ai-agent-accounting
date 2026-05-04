import os
import datetime
import google.generativeai as genai
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from dotenv import load_dotenv
from database import engine, get_db
import models
import schemas

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


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
	
@app.post("/analyze-expense/", response_model=schemas.ExpenseCreate)
def analyze_expense(expense_input: schemas.ExpenseInput, db: Session = Depends(get_db)):
	try:
		model = genai.GenerativeModel('gemini-2.5-flash')
		today_str = date.today().isoformat()
		prompt = f"""
		You are a highly accurate financial assistant.
		Analyze the following expense description and extract the details.
		- If a date isn't explicitly mentioned, assume today's date: {today_str}.
		- For the 'description' field, include the merchant name and a brief summary of what was bought.
		- Output the 'date' field strictly as a string in 'YYYY-MM-DD' format.
		
		User's Expense Text: "{expense_input.text}"
		"""
		response = model.generate_content(
			prompt,
			generation_config=genai.GenerationConfig(
				response_mime_type="application/json",
				response_schema=schemas.ExpenseExtraction,
			),
		)
		parsed_data = schemas.ExpenseExtraction.model_validate_json(response.text)
		formatted_date = datetime.datetime.strptime(parsed_data.date, "%Y-%m-%d").date()
		db_expense = models.Expense(
			amount=parsed_data.amount,
			category=parsed_data.category,
			description=parsed_data.description,
			date=formatted_date
		)
		db.add(db_expense)
		db.commit()
		db.refresh(db_expense)
		return db_expense
	except Exception as e:
		db.rollback()
		raise HTTPException(status_code=500, detail=f"Failed to process expense: {str(e)}")
		
		
		
		