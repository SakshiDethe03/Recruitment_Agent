from app.pipeline import recruitment_pipeline

def main():
    report = recruitment_pipeline(
        resume_path="data/resumes/Sakshi_Resume_Recruitment_Agent.pdf",
        job_description_path="data/jobs/job_description.txt",
    )

    print(report)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()