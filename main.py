# main.py
import streamlit as st
import pandas as pd
import plotly.express as px
import pandasql as ps


st.set_page_config(page_title="AI Sales Monitoring Dashboard", layout="wide")
st.title("AI Sales Monitoring Dashboard")

# =========================
# 1️⃣ Upload File
# =========================
uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # =========================
    # 2️⃣ Preprocessing
    # =========================
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    st.subheader("Cleaned Data Preview")
    st.dataframe(df.head())

    # =========================
    # 3️⃣ Sales KPI Monitoring
    # =========================
    st.subheader("Sales Performance Monitoring")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:

        selected_metric = st.selectbox(
            "Select Sales Metric to Monitor",
            numeric_cols
        )

        total_value = df[selected_metric].sum()

        baseline = st.number_input(
            "Enter Previous/Baseline Value",
            value=float(total_value)
        )

        if total_value < baseline:
            st.metric(
                label=f"Total {selected_metric}",
                value=f"{total_value:,.2f}",
                delta=f"-{baseline-total_value:,.2f}",
                delta_color="inverse"
            )
            st.error("⚠️ ALERT: Sales Dropped Below Baseline!")
        else:
            st.metric(
                label=f"Total {selected_metric}",
                value=f"{total_value:,.2f}",
                delta=f"+{total_value-baseline:,.2f}"
            )

    # =========================
    # 4️⃣ Trend Visualization
    # =========================
    if "date" in df.columns:
        try:
            df["date"] = pd.to_datetime(df["date"])
            trend = df.groupby("date")[selected_metric].sum().reset_index()

            st.subheader("Trend Over Time")
            fig = px.line(trend, x="date", y=selected_metric,
                          title=f"{selected_metric} Over Time")
            st.plotly_chart(fig, use_container_width=True)
        except:
            pass

    # =========================
    # 5️⃣ Interactive Visualization
    # =========================
    st.subheader("Custom Visualization")

    x_axis = st.selectbox("Select X-axis", df.columns)
    y_axis = st.selectbox(
        "Select Y-axis (numeric)",
        df.select_dtypes(include="number").columns
    )
    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Pie"])

    if st.button("Generate Chart"):

        if chart_type == "Bar":
            fig = px.bar(df, x=x_axis, y=y_axis,
                         title=f"{y_axis} vs {x_axis}")
            st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Line":
            fig = px.line(df, x=x_axis, y=y_axis,
                          title=f"{y_axis} vs {x_axis}")
            st.plotly_chart(fig, use_container_width=True)

        elif chart_type == "Pie":
            fig = px.pie(df, names=x_axis, values=y_axis,
                         title=f"{y_axis} Distribution by {x_axis}")
            st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 6️⃣ SQL Query Execution
    # =========================
    st.subheader("Optional SQL Query Execution")

    st.write("Use 'df' as the table name.")
    sql_query = st.text_area(
        "Paste SQL Query Here",
        placeholder="Example: SELECT region, SUM(revenue) FROM df GROUP BY region"
    )

    if st.button("Run SQL Query"):

        if sql_query.strip() != "":
            try:
                result = ps.sqldf(sql_query, locals())
                st.subheader("Query Result")
                st.dataframe(result)
            except Exception as e:
                st.error(f"SQL Error: {e}")

    # =========================
    # 7️⃣ Download Cleaned File
    # =========================
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Cleaned CSV",
        data=csv,
        file_name="cleaned_sales_data.csv"
    )

else:
    st.info("Upload a CSV or Excel file to start.")
