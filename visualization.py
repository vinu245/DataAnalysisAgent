# visualization.py
import streamlit as st
import plotly.express as px

def show_kpis(df):
    st.subheader("KPI Overview")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    
    if 'revenue' in numeric_cols:
        revenue = df['revenue'].sum()
        st.metric("Total Revenue", f"${revenue:,.2f}")
    if 'orders' in numeric_cols:
        orders = df['orders'].sum()
        st.metric("Total Orders", f"{orders:,}")
    if 'customers' in numeric_cols:
        customers = df['customers'].nunique()
        st.metric("Unique Customers", f"{customers:,}")

def show_charts(df):
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    # Bar chart
    if numeric_cols and categorical_cols:
        fig = px.bar(df, x=categorical_cols[0], y=numeric_cols[0],
                     title=f"{numeric_cols[0]} by {categorical_cols[0]}")
        st.plotly_chart(fig, use_container_width=True)

    # Line chart
    for col in numeric_cols:
        fig = px.line(df, y=col, title=f"{col} over index")
        st.plotly_chart(fig, use_container_width=True)

    # Pie chart
    if categorical_cols:
        cat_col = categorical_cols[0]
        pie_data = df[cat_col].value_counts().reset_index()
        pie_data.columns = [cat_col, "count"]
        fig = px.pie(pie_data, names=cat_col, values="count", title=f"{cat_col} Distribution")
        st.plotly_chart(fig, use_container_width=True)
