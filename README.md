# MSc Digital Humanities Thesis, KU Leuven
### Chahna Ahuja 
# Do Character Bots Dream of Fanfiction?
## The Remediation of Fanfiction Tropes as Intimate Fantasies on Character.AI


### About the Repository

This GitHub repository serves as the primary workspace documenting the computational materials and workflows developed for my MSc Digital Humanities thesis at KU Leuven. It contains cleaned datasets, preprocessing scripts, analysis python notebooks, technical reports, and visualisations produced throughout the research process.

The repository is grounded in considerations of transparency and reproducibility that have come to define the field of Digital Humanities. 


### Research Focus

Recent scholarship has suggested that character chatbots, such as those on Character.AI, are not entirely novel forms of fan practice, but emerge from longer histories of fan-created narratives and imaginative play. Contributing empirical evidence to this discourse, this project asks: How do the genre conventions and narrative imaginaries within fanfiction communities travel and transform in character chatbots?

In addressing this question, I study fan practices as modes of affective reception and draw on two forms of fan-created metadata: fanfiction tags on Archive of Our Own (AO3), and user-created bot descriptions and greetings on Character.AI. The analysis focuses specifically on fan practices within the South Korean boy band BTS fandom.

This repository focuses on the computational analysis that constitutes the distant reading component of the thesis. The computational findings are situated within a broader mixed-method approach that combines distant reading with close reading of vernacular fan practices and conventions of genre, tropes, and communal expectations.

### Data Sources

The computational analysis draws on two primary datasets:

* **Character.AI bot corpus** — BTS character bot descriptions and greetings collected from the open-source [Nomic Atlas Character.AI dataset](https://atlas.nomic.ai/data/auth0thread765/all-cai-characters-/map) that only contains character bot metadata.

* **AO3 fanfiction corpus** — BTS reader-insert fanfiction metadata derived from the [GOLEM AO3 dataset](https://golemlab.eu/about/), with particular attention to user-created tags in the reader-insert genre. The GOLEM dataset was developed as part of the EU-funded project **“Graphs and Ontologies for Literary Evolution Models” (GOLEM)** and is hosted at the University of Groningen (Pannach et al. 2024).


### Repository Structure

The repository is organised to follow the main stages of the computational workflow, from accessing and constructing the two corpora, through preprocessing and analysis, to the resulting datasets, reports, and visualisations.

The main components are:

#### 1. `requirements.txt`

Contains all third-party Python packages required to run the notebooks and scripts.

#### 2. `.env.example`

Provides a template for the environment variable required to access the Character.AI dataset through Nomic Atlas.

To access the Character.AI dataset:

1. Go to [Nomic Atlas](https://atlas.nomic.ai?utm_source=chatgpt.com).
2. Log in or create a Nomic account.
3. Navigate to **Settings** and create an API key for your account.
4. Copy `.env.example` to `.env`.
5. Add your API key to the `.env` file:

```env
NOMIC_API_KEY=your_api_key_here
```

The API key is loaded by `nomic_login.py` and used by `cai_nomic.py` to access the Character.AI dataset when running `01_bts_cai_corpus.ipynb`.

If access to the Nomic Atlas dataset is unavailable, you may contact the author regarding access to the raw Nomic Atlas dataset used in this research, subject to the applicable dataset terms and permissions.

> **Important:** Do not commit your `.env` file or API key to GitHub.

#### 3. `scripts/`

Contains reusable Python scripts that support data access and corpus construction.

* `nomic_login.py` — loads the Nomic Atlas API key and establishes access to Nomic Atlas.
* `cai_nomic.py` — accesses and processes the Character.AI dataset from Nomic Atlas.
* `sparql_client.py` — provides the SPARQL client used to query the GOLEM AO3 triple store.

#### 4. `notebooks/`

Contains the Jupyter notebooks documenting the computational workflow. The notebooks are organised into three stages: **corpus construction, data preprocessing, and analysis**.

##### Corpus Construction

These notebooks construct the two primary corpora used in the thesis.

* `01_bts_cai_corpus.ipynb` — constructs the BTS Character.AI bot corpus from the Nomic Atlas dataset.
* `02_bts_fics_corpus.ipynb` — constructs the BTS reader-insert AO3 fanfiction corpus from the GOLEM database.

##### Data Preprocessing

These notebooks clean and prepare the corpora for computational analysis.

* `03_bot_preprocessing.ipynb` — preprocesses the Character.AI bot corpus.
* `04_fics_data_preprocessing.ipynb` — preprocesses the AO3 fanfiction corpus.

##### Analysis

These notebooks perform the main computational analyses used in the thesis.

* `05_bots_semantic_clustering.ipynb` — performs semantic clustering of bot descriptions and greetings using a **SBERT → UMAP → HDBSCAN** pipeline. This notebook was run in Google Colab by the author due to its computational requirements, but is modular and can also be run locally with the required dependencies.

* `06_tag_network_analysis.ipynb` — performs **tag co-occurrence network analysis** of fanfiction tags. The notebook uses the **Leiden community detection algorithm** to identify communities of tags across different fanfiction content ratings.

#### 5. `data/`

Contains datasets generated at different stages of corpus construction and preprocessing.

##### Filtered Datasets

These are the datasets obtained after filtering the larger source datasets to create the BTS-specific corpora.

* `bts_bots/` — filtered BTS Character.AI bot corpus from Nomic Atlas.
* `bts_fics/` — filtered BTS fanfiction corpus from the GOLEM database.

##### Cleaned Datasets

These contain the cleaned and preprocessed data used in subsequent analyses.

* `bots/` — cleaned and preprocessed Character.AI bot data.
* `fics/` — cleaned and preprocessed fanfiction data.

##### Bot Semantic Clustering Cache

* `bts_thesis_cache/` — cached embeddings and intermediate outputs generated during the bot semantic clustering workflow. These files allow computationally expensive steps to be reused without recomputing the embeddings.

#### 6. `reports/`

Contains the reports, tabulated outputs, experimental results, and visualisations generated throughout corpus construction, preprocessing, and analysis. These figures and markdown reports support the arguments in the thesis. 

##### Bots

* `bots_reports/` — reports and tabulated outputs from the Character.AI bot corpus construction, preprocessing, and analysis.
* `bots_figures/` — visualisations generated throughout the bot corpus construction, preprocessing, and analysis.

##### Fics

* `fics_reports/` — reports and tabulated outputs from the fanfiction corpus construction, preprocessing, and analysis.

  * `tag_network_models/` — experimental data from different community detection and network-analysis configurations.
  * `network_models/` — finalised fanfiction tag co-occurrence networks across content ratings.

* `fic_figures/` — visualisations generated throughout the fanfiction corpus construction, preprocessing, and analysis.



## Installation

This repository uses Python notebooks and scripts for the computational analysis. The recommended Python versions are **Python 3.10 or 3.11**.

### 1. Clone the repository

Clone the repository from GitHub:

```bash
git clone <REPOSITORY-URL>
cd DH_Thesis
```

### 2. Install packages in requirements.txt 


```bash
pip install -r requirements.txt
```

### 3. Install the spaCy language model

The preprocessing notebooks use spaCy's English language model. Install it with:

```bash
python -m spacy download en_core_web_sm
```

### 4. Configure the Nomic Atlas API key

Create a local `.env` file in the root directory of the repository. You can use `.env.example` as a template:

You can also simply copy `.env.example` and rename the copy to `.env`.


The project uses `python-dotenv` to load this variable. `nomic_login.py` reads the API key, while `cai_nomic.py` uses it to access the Character.AI dataset.


### 5. Run the notebooks

After installation, open the repository in Jupyter Notebook, JupyterLab, or another compatible Python environment.

The notebooks are intended to be followed in the following order:

```text
01_bts_cai_corpus.ipynb
02_bts_fics_corpus.ipynb
03_bot_preprocessing.ipynb
04_fics_data_preprocessing.ipynb
05_bots_semantic_clustering.ipynb
06_tag_network_analysis.ipynb
```

### Note on Google Colab

The `05_bots_semantic_clustering.ipynb` notebook was run in Google Colab by the author because of its computational requirements. The notebook is modular and can also be run locally with the required dependencies.

Some notebooks contain Colab-specific imports, such as:

```python
from google.colab import drive, file
```

These are only required when running the relevant sections in Google Colab.

## Terms of Use

This repository contains the filtered and cleaned datasets generated specifically for this research. Raw source datasets are not redistributed as part of this repository.

This repository is primarily intended to document and support the computational research underlying the **MSc Digital Humanities thesis submitted at KU Leuven (2025–2026)**. It is not intended to function as a standalone software package.

Copyright in the original code, documentation, and research materials created for this repository is retained by the author. The use of third-party datasets and materials remains subject to the terms and conditions of their respective sources.

For methodological context, ethical considerations, theoretical discussion in fan studies and cultural studies, and interpretation of the computational findings from a digital humanities perspective, please refer to the accompanying thesis. A copy of the thesis may be requested from the author after September 2026.

