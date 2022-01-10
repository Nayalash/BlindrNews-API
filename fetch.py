import feedparser


def fetch_data():
    titles = []
    summaries = []
    links = []

    NewsFeed = feedparser.parse("https://www.teamblind.com/rss/Software-Engineering/rss")

    for i in range(1, 11):
        titles.append(NewsFeed.entries[i].title)
        summaries.append(NewsFeed.entries[i].summary)
        links.append(NewsFeed.entries[i].id)

    return titles, summaries, links
