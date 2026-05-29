from pathlib import Path
from typing import Any


def extract_text(*, file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")
    return file_path.read_text(encoding="utf-8")


def transform_count_sentences(*, text: str) -> int:
    sentences = [sentence.strip() for sentence in text.split(".") if sentence.strip()]
    return len(sentences)


def verify_sentence_count(*, count: int) -> None:
    if count <= 0:
        raise ValueError("Sentence count must be greater than zero.")


def load_sentence_report(*, count: int, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as file:
        file.write("AAHeid Text Sentence Report\n")
        file.write(f"Sentence count: {count}\n")


def run_aaheid_text_pipeline(
    *, raw_dir: Path, processed_dir: Path, logger: Any
) -> None:
    logger.info("AAHEID TEXT: START")

    input_file = raw_dir / "aaheid_notes.txt"
    output_file = processed_dir / "aaheid_sentence_count.txt"

    text = extract_text(file_path=input_file)
    count = transform_count_sentences(text=text)
    verify_sentence_count(count=count)
    load_sentence_report(count=count, out_path=output_file)

    logger.info("AAHEID TEXT: wrote %s", output_file)
    logger.info("AAHEID TEXT: END")
