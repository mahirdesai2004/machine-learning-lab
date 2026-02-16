
import os
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
import glob

# Constants
LAB_ROOT = "/Users/mahir/Desktop/MlLab/Lab-04"
OUTPUT_DIR = "/Users/mahir/Desktop/MlLab/.lab-report-screenshots"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to execute and convert notebook
def process_notebook(notebook_path, exp_name):
    print(f"Processing {notebook_path}...")
    try:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
        
        # Execute the notebook
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
        
        # Save executed notebook back (optional, but good for user)
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
            
        # Export to HTML
        html_exporter = HTMLExporter()
        html_exporter.theme = 'light' # Force light theme
        (body, resources) = html_exporter.from_notebook_node(nb)
        
        html_filename = os.path.join(OUTPUT_DIR, f"{exp_name}_notebook.html")
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(body)
            
        print(f"Generated HTML for {exp_name} at {html_filename}")
        return html_filename

    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")
        return None

# Find and process notebooks
experiments = [
    ("Experiment-1-Linear-Regression", "Exp1"),
    ("Experiment-2-Multiple-Regression", "Exp2"),
    ("Experiment-3-Logistic-Regression", "Exp3")
]

generated_html_files = []

for folder, prefix in experiments:
    nb_path = os.path.join(LAB_ROOT, folder, "notebook.ipynb")
    if os.path.exists(nb_path):
        html_file = process_notebook(nb_path, prefix)
        if html_file:
            generated_html_files.append((html_file, prefix))

print("Execution complete. Ready for screenshotting.")
