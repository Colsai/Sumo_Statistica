import pandas as pd
import requests

BASE_URL = "https://www.sumo.or.jp/EnHonbashoMain/torikumi/1"


def fetch_day_results(day: int, base_url: str = BASE_URL) -> pd.DataFrame:
    """Fetch results table for a single day of the basho.

    Parameters
    ----------
    day : int
        Day number to fetch (1-15).
    base_url : str
        Base URL for the tournament results.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the bouts for the given day.
    """
    url = f"{base_url}/{day}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # pandas.read_html extracts all tables; the first one typically
    # contains the bouts for the day
    tables = pd.read_html(response.text)
    if not tables:
        raise ValueError(f"No tables found on {url}")
    return tables[0]


def fetch_all_results(num_days: int = 15, base_url: str = BASE_URL) -> pd.DataFrame:
    """Fetch results for all days of the basho.

    Parameters
    ----------
    num_days : int
        Number of days to retrieve. Defaults to 15.
    base_url : str
        Base URL for the tournament results.

    Returns
    -------
    pandas.DataFrame
        Combined DataFrame of all bouts.
    """
    all_frames = []
    for day in range(1, num_days + 1):
        df = fetch_day_results(day, base_url)
        df["Day"] = day
        all_frames.append(df)
    return pd.concat(all_frames, ignore_index=True)


if __name__ == "__main__":
    # Example usage
    try:
        results_df = fetch_all_results()
        print(results_df)
    except Exception as exc:
        print(f"Failed to scrape results: {exc}")
