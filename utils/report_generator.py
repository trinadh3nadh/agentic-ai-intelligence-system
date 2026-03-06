from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import os


def generate_report(query, answer):

    filename = "ai_report.pdf"

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("AI Research Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("<b>Query:</b>", styles["Heading3"]))
    elements.append(Paragraph(query, styles["BodyText"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("<b>Final Answer:</b>", styles["Heading3"]))
    elements.append(Paragraph(answer.replace("\n", "<br/>"), styles["BodyText"]))

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    doc.build(elements)

    return filename
