import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🐰 Talking Rabbit Data Analyst")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Dataset Preview")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(include="object").columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found for graphs")
    
    else:

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Bar Chart", "Line Chart", "Pie Chart"]
        )

        if chart_type == "Bar Chart":

            x = st.selectbox("X Axis", df.columns)
            y = st.selectbox("Y Axis", numeric_cols)

            fig, ax = plt.subplots()
            df.plot(kind="bar", x=x, y=y, ax=ax)
            st.pyplot(fig)


        elif chart_type == "Line Chart":

            y = st.selectbox("Select numeric column", numeric_cols)

            fig, ax = plt.subplots()
            df[y].plot(kind="line", ax=ax)
            st.pyplot(fig)


        elif chart_type == "Pie Chart":

            if len(categorical_cols) > 0:

                cat = st.selectbox("Category", categorical_cols)

                fig, ax = plt.subplots()
                df[cat].value_counts().plot(
                    kind="pie",
                    autopct="%1.1f%%",
                    ax=ax
                )

                ax.set_ylabel("")
                st.pyplot(fig)

            else:
                st.warning("No categorical columns available")