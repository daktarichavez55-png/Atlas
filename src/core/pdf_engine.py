from pypdf import PdfReader, PdfWriter


def merge_pdfs(pdf_list, output_file):

    writer = PdfWriter()

    for pdf in pdf_list:

        reader = PdfReader(pdf)

        for page in reader.pages:
            writer.add_page(page)

    with open(output_file, "wb") as output:
        writer.write(output)

    return "PDFs merged successfully."


def get_pdf_info(pdf_file):

    reader = PdfReader(pdf_file)

    return {
        "pages": len(reader.pages),
        "encrypted": reader.is_encrypted
    }