from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_report(query, final_answer):

    filename = "ai_report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    text = c.beginText(40, 750)

    text.setFont("Helvetica", 12)

    text.textLine("AI Research Report")
    text.textLine("")
    text.textLine("Query:")
    text.textLine(query)
    text.textLine("")
    text.textLine("Final Answer:")
    text.textLine(final_answer)

    c.drawText(text)

    c.save()

    return filename