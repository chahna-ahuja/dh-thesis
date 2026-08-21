# BTS Reader-Insert Fanfiction Dataset Structure

## Dataset Size

| Metric | Value |
|---|---:|
| **Total Records** | 7,414 |
| **Total Columns** | 14 |

The final BTS reader-insert fanfiction corpus contains **7,414 records across 14 columns**.


## Column Schema

The following table summarizes the variables available in the final BTS single-member × reader fanfiction corpus, their detected data types, and their descriptions.

| Column Name | Data Type | Description |
|---|---|---|
| `s` | string | Unique identifier/database link for the fanfiction work |
| `kudos` | numeric | Number of user kudos received (reader engagement metric) |
| `title` | string | Fanfiction title |
| `summary` | string | Fanfiction summary or description |
| `datePublished` | string | Publication date of the fanfiction work |
| `words` | numeric | Total word count of the fanfiction |
| `rating` | string | Content rating assigned by AO3 |
| `romanticCategory` | string | Classification of romantic relationship category |
| `publicationStatus` | string | Publication status of the work |
| `keyword` | string | User-provided AO3 tags, including canonical and non-canonical tags |
| `relationship` | string | Relationship tags assigned to the fanfiction |
| `polyship_human_flag` | numeric | Manual annotation indicating whether the work was identified as involving a polyship |
| `member` | string | Primary BTS member associated with the fanfiction |
| `members_found` | string | BTS members detected in the metadata or text |

