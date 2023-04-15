import Levenshtein

# Ground truth text
gt_text = "The quick brown fox jumps over the lazy dog"

# OCR output
ocr_text = "The qick brown fx jumpts ovr the lzzy dg"

# Calculate word error rate (WER)
gt_words = gt_text.split()
ocr_words = ocr_text.split()
wer = Levenshtein.distance(gt_words, ocr_words) / len(gt_words)

# Calculate character error rate (CER)
gt_chars = list(gt_text)
ocr_chars = list(ocr_text)
cer = Levenshtein.distance(gt_chars, ocr_chars) / len(gt_chars)

# Print results
print(f"WER: {wer:.2%}")
print(f"CER: {cer:.2%}")
