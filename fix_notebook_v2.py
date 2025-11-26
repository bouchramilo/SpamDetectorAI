import json
import os

notebook_path = r'c:\Users\ramas\OneDrive\Desktop\SpamDetectorAI\notebooks\partie_1.ipynb'

print(f"Reading {notebook_path}...")
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
updated_count = 0

# Content to ensure exists
required_lines = [
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "nltk.download('punkt')\n",
    "nltk.download('punkt_tab')\n"
]

for i, cell in enumerate(cells):
    if cell['cell_type'] == 'code':
        source = cell['source']
        source_text = ''.join(source)
        
        # Check if this is a tokenization cell
        if "word_tokenize" in source_text:
            print(f"Found tokenization cell at index {i}")
            
            # Check if it needs updates
            new_source = []
            has_imports = "import nltk" in source_text
            has_punkt = "nltk.download('punkt')" in source_text
            has_punkt_tab = "nltk.download('punkt_tab')" in source_text
            
            if not has_punkt_tab:
                print(f"  Adding punkt_tab to cell {i}")
                
                # Reconstruct the cell source
                # If it doesn't have imports, add them at the top
                if not has_imports:
                    new_source.extend(required_lines)
                    new_source.append("\n")
                else:
                    # It has imports, but maybe not downloads
                    # We'll just prepend the missing downloads after imports if possible, 
                    # or just put them at the top to be safe.
                    # Simplest is to prepend the required lines that are missing.
                    if not has_punkt:
                         new_source.append("nltk.download('punkt')\n")
                    new_source.append("nltk.download('punkt_tab')\n")
                
                # Add the original source
                new_source.extend(source)
                
                # Update the cell
                cells[i]['source'] = new_source
                updated_count += 1

if updated_count > 0:
    print(f"Updated {updated_count} cells.")
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("File saved.")
else:
    print("No cells needed updating (punkt_tab already present).")
