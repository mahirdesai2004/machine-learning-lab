
import os
import re
from playwright.sync_api import sync_playwright

OUTPUT_DIR = "/Users/mahir/Desktop/MlLab/.lab-report-screenshots"
HTML_DIR = "/Users/mahir/Desktop/MlLab/.lab-report-screenshots"

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        experiments = [
            ("Exp1", "Exp1_notebook.html"),
            ("Exp2", "Exp2_notebook.html"),
            ("Exp3", "Exp3_notebook.html")
        ]
        
        for exp_prefix, html_name in experiments:
            html_path = os.path.join(HTML_DIR, html_name)
            if not os.path.exists(html_path):
                print(f"Skipping {html_name}, not found.")
                continue
                
            print(f"Processing {html_name}...")
            page.goto(f"file://{html_path}")
            
            # Find all cells
            cells = page.query_selector_all(".jp-Cell")
            
            code_counter = 1
            output_counter = 1
            
            for i, cell in enumerate(cells):
                # Check for input area (Code) - only for CodeCells
                if "jp-CodeCell" in cell.get_attribute("class"):
                    input_area = cell.query_selector(".jp-InputArea")
                    if input_area and input_area.is_visible():
                        # We might want to capture just the editor part to avoid prompts if desired, 
                        # but input_area includes prompt "In [x]:" which is good for context.
                        screenshot_path = os.path.join(OUTPUT_DIR, f"{exp_prefix}_Code_{code_counter}.png")
                        try:
                            input_area.screenshot(path=screenshot_path)
                            print(f"Captured {screenshot_path}")
                            code_counter += 1
                        except Exception as e:
                            print(f"Failed to capture code {i}: {e}")

                    # Check for output area (Results, Graphs)
                    # Output is usually within jp-Cell-outputWrapper -> jp-OutputArea
                    output_area = cell.query_selector(".jp-OutputArea")
                    if output_area and output_area.is_visible():
                        # Check if it's empty
                        if not output_area.query_selector(":scope > *"):
                            continue
                            
                        screenshot_path = os.path.join(OUTPUT_DIR, f"{exp_prefix}_Output_{output_counter}.png")
                        try:
                            output_area.screenshot(path=screenshot_path)
                            print(f"Captured {screenshot_path}")
                            output_counter += 1
                        except Exception as e:
                            print(f"Failed to capture output {i}: {e}")

        browser.close()

if __name__ == "__main__":
    take_screenshots()
