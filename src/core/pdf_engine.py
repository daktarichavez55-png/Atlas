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


def split_pdf(input_file, output_file, start_page, end_page):

    reader = PdfReader(input_file)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    if start_page < 1 or end_page > total_pages or start_page > end_page:
        raise ValueError(
            f"Please choose pages between 1 and {total_pages}."
        )

    for page_number in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_number])

    with open(output_file, "wb") as output:
        writer.write(output)

    return "PDF split successfully."