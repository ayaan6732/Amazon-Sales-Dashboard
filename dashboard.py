import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
df=pd.read_csv("Amazon Sale Report.csv")
st.title("AMAZON SALES")
st.sidebar.title("Controls")
status=st.sidebar.selectbox("Select Status",df["Status"].unique())
side,site=st.sidebar.slider("Select Amount Range",float(df["Amount"].min()),float(df["Amount"].max()),(float(df["Amount"].min()),float(df["Amount"].max())))
fulfilment=st.sidebar.selectbox("Select Fulfilment",df["Fulfilment"].unique())
st.sidebar.markdown("Hide Showbar")
showscatter=st.sidebar.checkbox("Scatter Chart", True)
showhist=st.sidebar.checkbox("Histogram", True)
showbar=st.sidebar.checkbox("Bar Chart", True)
showcount=st.sidebar.checkbox("Count Plot", True)
showline=st.sidebar.checkbox("Line Plot", True)
showpie=st.sidebar.checkbox("Pie Chart", True)
dt=df[(df["Status"]==status)&(df["Amount"]>=side)&(df["Amount"]<=site)&(df["Fulfilment"]!=fulfilment)]
st.download_button(label="Download Data",data=dt.to_csv(index=False).encode("utf-8"),file_name="data.csv",mime="text/csv")
st.subheader("Dataset Review")
st.dataframe(dt)
hg,hj=st.columns(2)
if showscatter:
    with hg:
        st.header("Scatter Chart")
        plt.figure(figsize=(14,12))
        plt.scatter(data=dt,x="Qty",y="Amount")
        plt.title("Quantity VS Amount")
        st.pyplot(plt)
if showhist:
    with hj:
        st.header("Histogram")
        plt.figure(figsize=(14,12))
        plt.hist(dt["Qty"],bins=40)
        plt.title("Quantity Distribution")
        st.pyplot(plt)
gh,aj,wl=st.columns(3)
gh.metric("Quantity 1",int((dt["Qty"]==1).sum()))
aj.metric("Quantity 2",int((dt["Qty"]==2).sum()))
wl.metric("Quantity 3",int((dt["Qty"]==3).sum()))
vo,ok=st.columns(2)
dt["Qty"]=pd.to_numeric(dt["Qty"])
hl=dt["Qty"].value_counts().sort_index()
print(hl)
if showbar:
    with vo:
        st.header("Bar Chart")
        plt.figure(figsize=(14,12))
        plt.bar(hl.index,hl.values)
        plt.title("Quantity of Products")
        plt.xlabel("Quantity")
        plt.ylabel("Count")
        plt.xticks(hl.index)
        st.pyplot(plt)
if showcount:
    with ok:
        st.header("Countplot")
        plt.figure()
        sns.countplot(data=dt,x="Size")
        plt.title("Size Count")
        st.pyplot(plt)
ln,sc=st.columns(2)
if showline:
    with ln:
        st.header("Line Plot")
        plt.figure()
        sns.lineplot(data=dt,x=("Category"),y=("Amount"))
        plt.title("Category VS Shipment Service")
        st.pyplot(plt)
fj=dt.sort_values("Amount",ascending=False).head()
if showpie:
    with sc:
        st.header("Pie Chart")
        plt.pie(fj["Amount"],labels=fj["Style"],autopct="%1.1f%%")
        plt.title("Style Promotion")
        st.pyplot(plt)
