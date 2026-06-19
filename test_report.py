from agents.report_generator import create_report

path = create_report(
    "This is a test ATS report."
)

print(path)