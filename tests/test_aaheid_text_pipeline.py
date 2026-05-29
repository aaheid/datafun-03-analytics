from pathlib import Path

from datafun.aaheid_text_pipeline import extract_text, transform_count_sentences


def test_extract_text(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.txt"
    test_file.write_text("One sentence. Two sentence.", encoding="utf-8")

    result = extract_text(file_path=test_file)

    assert "One sentence" in result


def test_transform_count_sentences() -> None:
    text = "One sentence. Two sentence. Three sentence."

    result = transform_count_sentences(text=text)

    assert result == 3
