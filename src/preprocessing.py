import csv
import re
import unicodedata
from pathlib import Path
from time import time


def clean_text(text):
    """
    Clean and normalize text while preserving Unicode characters.
    """

    if text is None:
        return ""

    text = str(text).strip()

    if not text:
        return ""

    # Unicode normalization
    text = unicodedata.normalize("NFKC", text)

    # Case normalization
    text = text.casefold()

    # Replace punctuation with spaces
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_file(input_file, output_file):
    """
    Preprocess one TSV file.

    Original rows and columns are preserved.
    Three cleaned columns are added:
        business_name_clean
        business_address_clean
        country_clean
    """

    start_time = time()
    row_count = 0

    with open(
        input_file,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as infile:

        reader = csv.DictReader(infile)

        fieldnames = reader.fieldnames + [
            "business_name_clean",
            "business_address_clean",
            "country_clean"
        ]

        with open(
            output_file,
            "w",
            encoding="utf-8-sig",
            newline=""
        ) as outfile:

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

                row_count += 1

    elapsed = time() - start_time

    print(
        f"Processed: {Path(input_file).name} | "
        f"Rows: {row_count:,} | "
        f"Time: {elapsed:.1f}s"
    )


def preprocess_dataset(input_dir, output_dir):
    """
    Preprocess all six Source files used in the challenge.
    """

    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    source_files = [
        "train_source1.tsv",
        "train_source2.tsv",
        "train_source3.tsv",
        "test_source1.tsv",
        "test_source2.tsv",
        "test_source3.tsv"
    ]

    for filename in source_files:

        input_file = input_dir / filename

        output_file = output_dir / (
            input_file.stem + "_preprocessed.tsv"
        )

        if not input_file.exists():
            print(f"WARNING: File not found: {input_file}")
            continue

        preprocess_file(
            input_file,
            output_file
        )


if __name__ == "__main__":

    print("Business Entity Resolution - Preprocessing")
    print("=" * 50)

    # Dataset folder containing the six original TSV files.
    INPUT_DIR = "dataset"

    # Folder where preprocessed files will be created.
    OUTPUT_DIR = "dataset/preprocessed"

    preprocess_dataset(
        INPUT_DIR,
        OUTPUT_DIR
    )

    print("=" * 50)
    print("Preprocessing completed.")