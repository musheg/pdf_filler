
Development setup
-----------------
Install required system packages:

    pip install -r requirments.txt

Usage example

    python main.py pdf_samples/3.pdf out.pdf
    python main.py pdf_samples/4.pdf out.pdf
    python main.py pdf_samples/5.pdf out.pdf
    python main.py pdf_samples/6.pdf out.pdf
    python main.py pdf_samples/9.pdf out.pdf

help

    python main.py -h
    
You can set your JSON file with field values by passing third argument, like:

    python main.py pdf_samples/3.pdf out.pdf my_json.json