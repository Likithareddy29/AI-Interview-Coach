from fpdf import FPDF

def generate_report(content):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        0,
        10,
        "AI Interview Coach Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.multi_cell(
        0,
        10,
        content
    )

    pdf.output(
        "resume_report.pdf"
    )

    return "resume_report.pdf"