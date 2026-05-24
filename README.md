# AI Vendor Matching Assistant

## Project Overview

AI Vendor Matching Assistant is a beginner-friendly AI engineering project designed to simulate how intelligent vendor recommendation systems work.

The system accepts user requirements such as:

* Vendor category
* Budget
* Location
* Delivery preference

The application then:

1. Searches vendor data
2. Calculates matching scores
3. Ranks vendors
4. Generates AI-based recommendations
5. Displays results visually in terminal

This project was built to understand:

* AI workflow architecture
* Recommendation systems
* Modular Python development
* AI-assisted reasoning
* Vendor ranking systems
* OpenAI integration
* Scoring logic
* Workflow simulation

---

# Features

* AI-powered vendor recommendation system
* Vendor ranking engine
* Match score calculation
* OpenAI-generated recommendations
* Visual terminal workflow
* Match score bar charts
* Modular project structure
* Beginner-friendly architecture

---

# Tech Stack

| Technology                  | Purpose                      |
| --------------------------- | ---------------------------- |
| Python                      | Core programming language    |
| OpenAI API                  | AI recommendation generation |
| VS Code                     | Development environment      |
| Virtual Environment (venv)  | Dependency isolation         |
| Git & GitHub                | Version control              |
| Modular Python Architecture | Scalable project design      |

---

# Project Workflow

```text
User Input
    ↓
AI Workflow Starts
    ↓
Vendor Database Search
    ↓
Score Calculation
    ↓
Vendor Ranking
    ↓
AI Recommendation Generation
    ↓
Results Displayed
```

---

# Folder Structure

```text
vendor-matching-agent/
│
├── venv/
├── src/
│   ├── agents/
│   ├── data/
│   ├── llm/
│   ├── similarity/
│   ├── tools/
│   └── utils/
│
├── app.py
├── Requirements.txt
├── .env
├── .gitignore
```

---

# Core Concepts Used

## 1. AI Workflow Simulation

The application simulates how AI systems process requests step-by-step.

---

## 2. Recommendation Engine

The project ranks vendors based on:

* category match
* location match
* budget similarity
* delivery preference

---

## 3. Scoring System

Each vendor receives points depending on how closely they match user requirements.

Example:

| Condition         | Score |
| ----------------- | ----- |
| Same category     | +40   |
| Same location     | +25   |
| Delivery match    | +20   |
| Budget similarity | +15   |

---

## 4. AI Recommendation Generation

OpenAI API generates natural language recommendations explaining why a vendor is a good match.

Example:

```text
FreshFoods Pvt Ltd is a strong match because it supports catering services in Bangalore with express delivery and fits your preferred budget range.
```

---

# Modules Explanation

## app.py

Main entry point of the application.

Responsibilities:

* Takes user input
* Displays workflow
* Calls matching agent
* Displays results
* Displays score bars

---

## matching_agent.py

Controls the complete vendor matching workflow.

Responsibilities:

* Calls search tool
* Calls scoring engine
* Calls AI recommendation generator
* Sorts vendors by score

---

## vendors.py

Stores vendor database.

Each vendor contains:

* name
* category
* budget
* location
* delivery type
* rating

---

## scoring.py

Calculates vendor match score.

Used for:

* ranking
* recommendation quality
* comparison logic

---

## llm_handler.py

Handles OpenAI integration.

Used for:

* generating AI explanations
* simulating intelligent recommendation systems

---

# Sample Output

```text
============================================================
        AI VENDOR MATCHING ASSISTANT
============================================================

✓ Understanding User Request
✓ Searching Vendor Database
✓ Calculating Match Scores
✓ Ranking Best Vendors
✓ Generating AI Recommendations

============================================================
               TOP VENDOR MATCHES
============================================================

1. FreshFoods Pvt Ltd
----------------------------------------
Match Score : 92%
Vendor Rating : 4.8
Delivery Type : express

Why matched?
• Matching category
• Same location
• Preferred delivery available
• Fits budget range
```

---

# Challenges Faced During Development

* Python virtual environment setup
* Folder structure organization
* API integration
* File path debugging
* OpenAI quota handling
* Modular code architecture
* Terminal workflow visualization

---

# Key Learnings

Through this project, the following concepts were learned:

* Modular Python development
* AI workflow architecture
* Recommendation system basics
* Vendor ranking logic
* OpenAI API integration
* GitHub project management
* Debugging and environment setup
* Scalable project structure

---

# Future Improvements

Planned future upgrades:

* Streamlit frontend
* LangGraph integration
* Cosine similarity with embeddings
* Vector database integration
* Neo4j knowledge graph
* Context memory
* Multi-agent workflow
* MCP tool calling
* Real vendor database/API

---

# Conclusion

This project successfully demonstrates the foundational concepts behind AI-powered recommendation systems and agent workflows.

The project was intentionally designed as a beginner-friendly learning project to understand how:

* AI workflows operate
* recommendation systems rank results
* modular architecture improves scalability
* AI-generated explanations improve user experience

The system serves as a strong foundation for future advanced AI engineering projects.

---

# Author

Shreya Chaturvedi

AI Vendor Matching Assistant Project
