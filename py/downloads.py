from transformers import AutoTokenizer, AutoModel, AutoConfig

model_name = "medkit/DrBERT-CASM2"
cache_dir = "./models_cache"  # Dossier local pour stocker le modèle

AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
AutoModel.from_pretrained(model_name, cache_dir=cache_dir)
AutoConfig.from_pretrained(model_name, cache_dir=cache_dir)
