import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    exit(1)

FILE_1 = r"C:\Users\USER\Downloads\OTHERS\5ers RAG bot\5ers-rag-dev\the5ers-faqs-full.md"
RAW_DATA_DIR = r"C:\Users\USER\Downloads\OTHERS\5ers RAG bot\5ers-rag-dev\raw_data"

def read_files():
    text = ""
    with open(FILE_1, 'r', encoding='utf-8') as f:
        text += "--- SOURCE 1: the5ers-faqs-full.md ---\n"
        text += f.read() + "\n\n"
        
    for root, dirs, files in os.walk(RAW_DATA_DIR):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    text += f"--- SOURCE 2: {file} ---\n"
                    content = f.read()
                    if len(content) > 100000:
                        content = content[:100000] + "...(truncated)"
                    text += content + "\n\n"
    return text

def main():
    print("Reading data sources...")
    
    merged_content = "# The 5ers Compiled FAQ\n\n"
    
    with open(FILE_1, 'r', encoding='utf-8') as f:
        merged_content += f.read() + "\n\n"
        
    for root, dirs, files in os.walk(RAW_DATA_DIR):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Basic deduplication: if this exact content is not already in the merged content
                    if content[:100] not in merged_content:
                        merged_content += f"## Scraped Data: {file}\n\n"
                        merged_content += content + "\n\n"
                        
    output_path = r"C:\Users\USER\Downloads\OTHERS\5ers RAG bot\5ers-rag-dev\data\faq_data.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(merged_content)
        
    print(f"Compilation result written to {output_path}")

if __name__ == "__main__":
    main()
