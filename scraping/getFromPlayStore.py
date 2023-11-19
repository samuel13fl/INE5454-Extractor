from google_play_scraper import Sort, reviews
import pandas as pd


def fetch_reviews(app_id, count=500, sort=Sort.NEWEST, lang='pt', country='br'):
    all_reviews = []
    continuation_token = None

    while True:
        fetched_reviews, continuation_token = reviews(
            app_id,
            continuation_token=continuation_token,
            count=count,
            sort=sort,
            lang=lang,
            country=country
        )
        all_reviews.extend(fetched_reviews)


        if not continuation_token or not fetched_reviews:
            print(f"Coletadas {len(all_reviews)} avaliações do aplicativo {app_id}")
            break

    return all_reviews

def fetch_and_save_reviews(escolha, csv_path):
    app_reviews = fetch_reviews(escolha)

    for review in app_reviews:
        review['appId'] = escolha
        review['Empty1'] = None
        review['Empty2'] = None
        review['Fonte'] = 'Google Play'

    df_reviews = pd.DataFrame(app_reviews)
    df_reviews = df_reviews[['Fonte','score', 'content', 'Empty1', 'reviewCreatedVersion', 'Empty2', 'at']]

    with open(csv_path, 'a', encoding='utf-8') as file:
        df_reviews.to_csv(file, header=False, index=False)