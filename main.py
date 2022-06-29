import json

from fillpdf import fillpdfs
import fire


def fill_pdf(pdf_file, out_pdf='out.pdf', json_fields_file_path="./field_values.json"):
    fillpdfs.get_form_fields(pdf_file)
    fillpdfs.print_form_fields(pdf_file)
    # returns a dictionary of fields
    # Set the returned dictionary values a save to a variable
    # For radio boxes ('Off' = not filled, 'Yes' = filled)

    f = open(json_fields_file_path)
    field_dictionary = json.load(f)

    fillpdfs.write_fillable_pdf(pdf_file, out_pdf, field_dictionary)

    # If you want it flattened:
    fillpdfs.flatten_pdf(out_pdf, 'newflat.pdf')


if __name__ == '__main__':
  fire.Fire(fill_pdf)
