import docx
import docx.document

def load_document_template(path: str) -> docx.document.Document:
    try:
        doc = docx.Document(path)
        return doc
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    

def fill_document_template(doc: docx.document.Document, data):
    # Fill document template logic here
    pass