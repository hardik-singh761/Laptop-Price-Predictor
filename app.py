#Importing Libraries
import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",layout="wide")

#import model
st.title("Laptop Price Predictor 💻 by Hardik")
pipe=pickle.load(open("./model/pipe.pkl","rb"))
df=pickle.load(open("./model/df.pkl","rb"))

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # brand input
    company = st.selectbox("Brand", df["Company"].unique())

with middle_column:
    # laptop type
    type = st.selectbox("Type", df["TypeName"].unique())

with right_column:
    # Ram size
    ram = st.selectbox("Ram (in GB)", df["Ram"].unique())

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Weight input
    weight = st.number_input("Weight of laptop in kg")

with middle_column:
    # Screen
    screen = st.selectbox('Screen Type',df['Screen'].unique())

with right_column:
    # Touchscreen
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # IPS display
    ips = st.selectbox("IPS Display", ["No", "Yes"])

with middle_column:
    # RetinaDisplay
    rd = st.selectbox("Retina Display", ["No", "Yes"])

with right_column:
    # CPU Frequency
    cpu_freq = st.number_input("CPU Frequency")

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # screen size
    Screen_size = st.number_input("Screen Size (in Inches)")

with middle_column:
    # resolution
    resolution = st.selectbox('Screen Resolution',['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600','2560x1440', '2304x1440'])

with right_column:
    # Primary Storage
    Primary_storage = st.number_input("Primary Storage (In GB)")

# making 3 cols left_column, middle_column, right_column
left_column,middle_column,right_column = st.columns(3)
with left_column:
    # Secondary Storage
    Secondary_storage = st.number_input("Secondary Storage (In GB)")

with middle_column:
    # Primary Storage Type
    pst = st.selectbox('Primary Storage Type',df['PrimaryStorageType'].unique())

with right_column:
    # Secondary Storage Type
    sst = st.selectbox('Secondary Storage Type',df['SecondaryStorageType'].unique())

left_column,middle_column,right_column=st.columns(3)
with left_column:
    # GPU Company
    gpu_company = st.selectbox('GPU Company',df['GPU_company'].unique())

with middle_column:
    # CPU
    cpu = st.selectbox('CPU',df['CPU'].unique())

with right_column:
    # OS
    os = st.selectbox('OS',df['Simplified_OS'].unique())

if st.button("Predict Price"):
    ppi = None
    if touchscreen=="Yes":
        touchscreen=1
    else:
        touchscreen=0

    if ips == "Yes":
        ips=1
    else:
        ips=0

    if rd == 'Yes':
        rd=1
    else:
        rd=0
    
    X_res=int(resolution.split("x")[0])
    Y_res=int(resolution.split('x')[1])
    ppi=((X_res ** 2)+(Y_res ** 2))**0.5/Screen_size
    query=np.array([company,type,ram,weight,screen,touchscreen,ips,rd,cpu_freq,Primary_storage,Secondary_storage,pst,sst,gpu_company,ppi,cpu,os])

    query=query.reshape(1, 17)
    if weight==0.0:
        st.title('None')
    else:
        st.title("The Predicted Price of Laptop = Rs "+str(int(np.exp(pipe.predict(query)[0]))))


