import docx2txt
import sys

def main():
    try:
        text = docx2txt.process(r"c:\Users\hp\Downloads\portfolio-master\portfolio-master\Narayana.docx")
        with open(r"c:\Users\hp\Downloads\portfolio-master\portfolio-master\cv_extracted.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Extraction complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
