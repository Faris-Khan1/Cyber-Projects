import os
from PyPDF2 import PdfReader

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class MetadataExtractor:
    def extract_metadata(self) -> str:
        pdf_file = os.path.join(__location__, "Totally_Safe_File.pdf")
        reader = PdfReader(pdf_file)
        metadata = str(reader.metadata) 
        print("\nMetadata for PDF File:\n", metadata)
        return metadata


class MetadataProcessor:
    def process_metadata(self, metadata: str) -> None:
        if "confidential".lower() in metadata.lower() or "classified".lower() in metadata.lower():
            print("\nThe PDF is tagged confidential or classified.")
        else:
            print("\nNo confidential/classified tags found in metadata.")


if __name__ == "__main__":
    extractor = MetadataExtractor()
    pdf_metadata = extractor.extract_metadata()

    processor = MetadataProcessor()
    processor.process_metadata(pdf_metadata)


