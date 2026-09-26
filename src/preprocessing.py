import csv
import re
import unicodedata


def clean_text(text):
    if text is None:
        return ""

    text = str(text).strip()

    if not text:
        return ""

    text = unicodedata.normalize("NFKC", text)
    text = text.casefold()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)

        fieldnames = reader.fieldnames + [
            "business_name_clean",
            "business_address_clean",
            "country_clean"
        ]

        with open(output_file, "w", encoding="utf-8-sig", newline="") as outfile:
            writer = csv.DictWriter(
                outfile,
                fieldnames=fieldnames,
                delimiter="\t"
            )

            writer.writeheader()

            for row in reader:
                row["business_name_clean"] = clean_text(
                    row.get("business_name", "")
                )

                row["business_address_clean"] = clean_text(
                    row.get("business_address", "")
                )

                row["country_clean"] = clean_text(
                    row.get("country", "")
                )

                writer.writerow(row)