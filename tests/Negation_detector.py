from pathlib import Path
from medkit.core.text import TextDocument
from medkit.text.segmentation import SentenceTokenizer
from medkit.text.context import NegationDetector, NegationDetectorRule

#importation du texte
doc = TextDocument.from_file(Path(r"C:\Users\Administrateur\Documents\ENSTA Bretagne\2A\aime\tests\ENSTAP1.txt"))

#tokenisation du texte en phrases
sent_tokenizer = SentenceTokenizer(
    output_label="sentence",
    punct_chars=[".", "?", "!"],
)

sentences = sent_tokenizer.run([doc.raw_segment])

# for sentence in sentences:
#     print(f"uid={sentence.uid}")
#     print(f"text={sentence.text!r}")
#     print(f"spans={sentence.spans}, label={sentence.label}\n")

#detection des negations

negation_detector = NegationDetector(output_label="negation")
negation_detector.run(syntagma_segs)

# Display negated syntagmas
for syntagma_seg in syntagma_segs:
    negation_attr = syntagma_seg.attrs.get(label="negation")[0]
    if negation_attr.value:
        print(syntagma_seg.text)