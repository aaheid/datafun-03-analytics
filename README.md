# ## Custom Project

For my custom project, I modified the XLSX pipeline.

Changes:
- Changed the target word from "GitHub" to "Data"
- Updated the output filename to `xlsx_feedback_data_count.txt`
- Improved logging messages

Results:
- Successfully executed with:
  uv run python -m datafun.app_aaheid
- Created:
  data/processed/xlsx_feedback_data_count.txt

Key Insight:
The ETVL pattern separates Extract, Transform, Verify, and Load responsibilities, making data processing easier to maintain and debug.

## Custom Project

For my custom project, I created a custom text ETVL pipeline.

My new pipeline file is:

- `src/datafun/aaheid_text_pipeline.py`

My raw data file is:

- `data/raw/aaheid_notes.txt`

My output file is:

- `data/processed/aaheid_sentence_count.txt`

The pipeline follows the ETVL process:

- Extract: reads text from `aaheid_notes.txt`
- Transform: counts the number of sentences
- Verify: checks that the sentence count is greater than zero
- Load: writes the result to `aaheid_sentence_count.txt`

I chose a text file because plain text is a common data format. Counting sentences is useful because it gives a quick summary of the amount of written content.

To run my custom project:

```powershell
uv run python -m datafun.app_aaheid
