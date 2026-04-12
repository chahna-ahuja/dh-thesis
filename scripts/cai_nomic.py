# scripts/cai_nomic.py
from nomic import AtlasDataset

def load_nomic_dataset(dataset_name="auth0thread765/all-cai-characters-"):
    """
    Load Character.AI dataset from Nomic Atlas and return the DataFrame.
    """
    dataset = AtlasDataset(dataset_name)
    atlas_map = dataset.maps[0]
    df = atlas_map.data.df
    meta = dataset.meta
    return df, meta