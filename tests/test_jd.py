from app.agents.job_description_analyzer import analyze_jd

jd="""
We are hiring a Python Backend Developer.

Requirements:
- Python
- FastAPI
- Docker
- PostgreSQL

Experience: 3+ years
Location: Pune
"""

print(analyze_jd(jd))