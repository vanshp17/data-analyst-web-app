#vanshita patil

#import

import streamlit as st
import pandas as pd
import seaborn as sns


#1. Title and subheader
st.title('Data Analyst')
st.subheader('Data Aalysis Using Python and Streamlit')



#2.Upload Dataset

upload=st.file_uploader('Upload Your Dataset(In CSV Format only)')
if upload is not None:
    data=pd.read_csv(upload)


#3.Show Dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())


#4. Check Datatype of each column
if upload is not None:
    if st.checkbox('Dataype of each columns'):
        st.text('Datatypes')
        st.write(data.dtypes)

#5. Find the shape of Our dataset(No of Rows and columns)
if upload is not None:
    data_shape=st.radio('What dimension do you ant to check? ',('Rows','Columns'))
    if data_shape=='Rows':
        st.text('No of Rows')
        st.write(data.shape[0])
    else:
        st.text('No of columns')
        st.write(data.shape[1])

#6. Find null values in Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox('Null values in the dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success('Congratulations, No missing values')


#7. FInd Duplicates values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning('This dataset contain some dupliactes values')
        dup=st.selectbox('Do you want to remove Duplicate Values ',\
                        ('Select one',"Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text('Duplicates values are removed')
        if dup=="No":
            st.text('Ok No problem')



#8. Get overaall statistics
if upload is not None:
    if st.checkbox('Summary of dataset'):
        st.write(data.describe(include='all'))
        



#9. About section
if st.button('About App'):
    st.text('Bulit with streamlit')
    st.text('Thanks to streamlit')

#10. By
if st.checkbox('By'):
    st.success('Vanshita Patil')





