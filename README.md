# Airflow Data Enrichment with LocationIQ

It's a simple demo to show how data enrichment using data from LocationIQ API

## Data Input

A simple json data input provided in directory **data/int_input**

## Data Output

Once the dag manually run, it should generates a json file on directory **data/int_output**

## Build & Run

Go to [LocationIQ](https://locationiq.com), do sign up or login if you already have account and get the API key

Edit the .env and set LOCATIONIQ_API_KEY as your API key above

```
git clone https://github.com/jimbas/data-enrich-locationiq.git
cd data-enrich-locationiq
docker-compose up -d
docker-compose logs -f
```

Examine and wait until you see **[INFO] Listening at: http://0.0.0.0:8080**

Open your favorite browser and type **http://127.0.0.1:8080** on address bar

Use **admin** for username and password

## References

- [Location IQ API](https://docs.locationiq.com/reference/search)
