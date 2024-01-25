from docx import Document


def read_transcript(file_path):
    document = Document(file_path)

    messages = []
    current_role = None
    current_content = ""

    for paragraph in document.paragraphs:
        if paragraph.style.name.startswith("Heading 1"):
            # Detecting the title with underline
            title = paragraph.text.strip()
            title_underline = '-' * len(title)
        elif paragraph.text.lower().startswith("customer:"):
            if current_role is not None:
                messages.append({"role": current_role, "content": current_content.strip()})
            current_role = "user"
            current_content = paragraph.text[10:].strip()
        elif paragraph.text.lower().startswith("service representative:"):
            if current_role is not None:
                messages.append({"role": current_role, "content": current_content.strip()})
            current_role = "service representative"
            current_content = paragraph.text[26:].strip()
        else:
            current_content += " " + paragraph.text.strip()

    if current_role is not None:
        messages.append({"role": current_role, "content": current_content.strip()})

    return messages


# Replace 'transcript1.docx' with the actual path to your document
read_transcript("C:\\Users\\cohen\\Transcripts\\Transcript1.docx")


