from medkit.core.text import TextDocument
from medkit.text.ner.hf_entity_matcher import HFEntityMatcher

matcher = HFEntityMatcher(model="medkit/DrBERT-CASM2")

test_doc = TextDocument("Il ne boit pas d'alcool et ne fume pas de tabac.")
detected_entities = matcher.run([test_doc.raw_segment])


# show information
msg = "|".join(f"'{entity.label}':{entity.text}" for entity in detected_entities)
print(f"Text: '{test_doc.text}'\n{msg}")
