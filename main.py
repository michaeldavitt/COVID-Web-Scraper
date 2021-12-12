from datetime import datetime
import pandas as pd
from scraper import scrape


def main():
    df = pd.read_csv("DATA.csv")
    date_today = datetime.today()
    updated_figures = [date_today.strftime("%d/%m/%Y")]
    updated_figures.extend(scrape())
    df.loc[len(df)] = updated_figures
    df.to_csv("DATA.csv", index=False, header=True)


if __name__ == "__main__":
    main()
