# Keyword Extraction Benchmark

## Dataset

Evaluation Dataset: 20 customer feedback samples

---

## Results

| Model | Precision | Recall | F1 Score | Runtime |
|---------|---------|---------|---------|---------|
| TF-IDF (Research Paper Model) | 0.275 | 0.133 | 0.173 | ~0.01 sec |
| YAKE | 0.283 | 0.758 | 0.395 | 0.059 sec |

---

## Observations

1. YAKE significantly outperformed the TF-IDF baseline.

2. Recall improved from 0.133 to 0.758.

3. F1 Score improved from 0.173 to 0.395.

4. Domain-independent keyword extraction methods appear more suitable for customer feedback data than TF-IDF models trained on research papers.
