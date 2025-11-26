# Day 6 – Fraud Alert Voice Agent

## Overview
Build a **fraud alert voice agent** for your favorite bank.

For the **primary goal**, everything can run using your existing voice setup (no extra UI):
- You will create a **sample database** describing for a few suspicious transaction.
- When a "fraud alert" call/session starts, your agent will **use userName from the database** and:
  - Introduce itself as the bank's fraud department.
  - Verify the customer in a basic, safe way.
  - Read out the suspicious transaction.
  - Ask if it was actually made by the customer.
  - Mark the case as **safe** or **fraudulent**.
  - If you persist anything, you'll do it by **writing to database entry**.

For the **advanced goals**, the main challenge is:
- Implement the same fraud flow using **actual telephony with LiveKit Telephony**, so someone can talk to the fraud bot from a real phone call.

> ⚠️ **Important:**  
> Use only **fake data**.  
> Do **not** request or handle real card numbers, PINs, passwords, or other sensitive information.  
> Keep everything clearly demo/sandbox-only.

## Primary Goal (MVP) – Single Fraud Case from Database, In-App Call

**Objective:**  
Build a voice agent that, when a fraud alert call starts, reads a **single fraud case** from a Database, talks the user through the details, asks if the transaction is legitimate, and updates the case status in Database to safe or fraudulent.

### Tasks

1. **Create a sample fraud cases in Database**
2. **Set up the fraud agent persona**
3. **Load the fraud case at call start**
4. **Implement a simple call flow**
5. **Update the fraud case in database**

### MVP Completion Checklist
- Created database with fake fraud cases
- Agent loads case from database using username
- Agent introduces itself as bank fraud rep
- Performs simple, safe verification
- Reads out suspicious transaction
- Asks if user made the transaction
- Updates case status in database

## Resources
- https://docs.livekit.io/agents/build/prompting/
- https://docs.livekit.io/agents/build/tools/
- https://www.geeksforgeeks.org/python/python-sqlite/
