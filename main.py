from fastapi import FastAPI

from fetch import fetch_data

app = FastAPI()


@app.get("/api/fetch")
async def fetch_point():

    data = fetch_data()

    titles = data[0]
    summaries = data[1]
    links = data[2]

    return {
        "Titles": titles,
        "Summaries": summaries,
        "Links": links
    }
