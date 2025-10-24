# Airflow Data Enrichment Using LocationIQ

It's a simple demo to show data enrichment taking advantage data from LocationIQ API

## Files Modified

These are files that I modified from the original source

### Simple modification

- docker-compose.yaml

### Heavily Modified

- .env (still original. Please refer to google-drive link in the replied email)
- src/integrations/geocode_util.py
- src/transformers/address_transformer.py
- src/utils/reader.py
- src/utils/writer.py

## Files Created

These are files (or directories) that I created (doesn't exist on the original source)

- dags, logs, plugins (directory)
- dags/bci_interview_dag.py
- src/\_\_init\_\_.py

## File Generated

Once the **bci_interview_dag** dag manually run. It should generates a json file on directory **data/int_test_output**

- data/int_test_output/output_sample.json

## Build & Run

Edit the .env file to get API key

```
git clone https://github.com/jimbas/bci-interview
cd bci-interview
# replace .env with the one in google-drive link
docker-compose up -d
docker-compose logs -f
```

Examine and wait until you see **[INFO] Listening at: http://0.0.0.0:8080**

Open your favorite browser and type **http://127.0.0.1:8080** on address bar

Use **admin** for username and password

## References

- [Location IQ API](https://docs.locationiq.com/reference/search)
