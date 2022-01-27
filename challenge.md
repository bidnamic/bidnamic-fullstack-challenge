<img src="logo.png" alt="drawing" width="500"/>

## Full Stack Django Engineering Challenge

Our system ingests search term data from Google Ads API into a PostgreSQL database, via an AWS S3 Data Lake.

Once ingested we score each search term with its Return On Ad Spend (ROAS).

```text
ROAS = conversion value / cost
```

### Task

Using the Django Framework:

1. Ingest the given 3 CSVs (campaigns.csv, adgroups.csv and search_terms.csv) into a database, ensure the process is idempotent.


2. Create some end points to return the Top 10 Search Terms by ROAS for a campaign `structure_value` or adgroup `alias`.

   Only a user who is authenticated with the `api_access` permission can access the end points.


3. Write a Django HTML template to show the Top 10 Search Terms by ROAS by a selected campaign `structure_value` or adgroup `alias`.

### Submission

We really value neatness and things being put in place to aid local development and continuous integration.

Please fork this repo to complete the challenge.

Good luck we are rooting for you, show us what you can do!
