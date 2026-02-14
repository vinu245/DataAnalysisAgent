# query_processor.py
import pandasql as ps
import re
from difflib import get_close_matches

def map_column(user_col, df):
    match = get_close_matches(user_col.lower().replace(" ", "_"), df.columns.tolist(), n=1)
    return match[0] if match else None

def english_to_sql(query_text, df):
    query_text = query_text.lower()

    # Top N
    if "top" in query_text and "by" in query_text:
        n_match = re.search(r'top (\d+)', query_text)
        col_match = re.search(r'by ([\w\s]+)', query_text)
        if n_match and col_match:
            n = int(n_match.group(1))
            col = map_column(col_match.group(1), df)
            if col:
                return f"SELECT * FROM df ORDER BY {col} DESC LIMIT {n}"

    # Sum grouped by
    elif "sum" in query_text and "group by" in query_text:
        col_match = re.search(r'sum of ([\w\s]+)', query_text)
        group_match = re.search(r'group by ([\w\s]+)', query_text)
        if col_match and group_match:
            col = map_column(col_match.group(1), df)
            group = map_column(group_match.group(1), df)
            if col and group:
                return f"SELECT {group}, SUM({col}) as total_{col} FROM df GROUP BY {group}"

    # Average grouped by
    elif "average" in query_text and "group by" in query_text:
        col_match = re.search(r'average ([\w\s]+)', query_text)
        group_match = re.search(r'group by ([\w\s]+)', query_text)
        if col_match and group_match:
            col = map_column(col_match.group(1), df)
            group = map_column(group_match.group(1), df)
            if col and group:
                return f"SELECT {group}, AVG({col}) as avg_{col} FROM df GROUP BY {group}"

    # Count distinct
    elif "distinct" in query_text or "unique" in query_text:
        col_match = re.search(r'distinct ([\w\s]+)', query_text)
        if col_match:
            col = map_column(col_match.group(1), df)
            if col:
                return f"SELECT COUNT(DISTINCT {col}) as distinct_{col} FROM df"

    # Total / sum of column
    elif "total" in query_text or "sum of" in query_text:
        col_match = re.search(r'(?:total|sum of) ([\w\s]+)', query_text)
        if col_match:
            col = map_column(col_match.group(1), df)
            if col:
                return f"SELECT SUM({col}) as total_{col} FROM df"

    # Default: select all
    return "SELECT * FROM df"
