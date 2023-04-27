import streamlit as st

def introduction(display=True):
    
    #title
    st.markdown("<h2 style='text-align: center;'>Introduction</h2>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: left;'>Project Brief</h2>", unsafe_allow_html=True)
    
    st.write('''Suppose I have been hired as a consultant by music indusrty professionals working with Taylor Swift. The main objective of this project is to provide insights into the factors that influence the popularity of Taylor Swift's songs and to gain a deeper insight into song lyrics. By exploring these factors, we can gain a better understanding of what makes a Taylor Swift song popular and potentially use this knowledge to make informed decisions about which songs to promote, how to market them, and which elements to emphasize.
    ''')
    
    st.markdown("<h4 style='text-align: left;'>Project Objectives</h2>", unsafe_allow_html=True)
    
    st.markdown('''
    **1. Relationship between audio features and popularity:**  Explore the relationship between audio features (such as danceability, acousticness, energy, and valence) and popularity. For example, do songs that are more danceable tend to be more popular? Are there any audio features that have a strong correlation with popularity?

    **2. Album analysis:**  Analyze the characteristics of each album and compare them to each other. For example, are there any significant differences in the audio features of her early albums compared to her more recent ones? Are there any common themes or motifs that run throughout her albums?

    **3. Sentiment Analysis:** You could use sentiment analysis to explore the emotions conveyed in Taylor Swift's lyrics. For example, you could calculate the average sentiment score for each album or visualize the sentiment score for individual songs.

    **4. Lyrics analysis:**  You could explore the themes and topics that are common in Taylor Swift's lyrics. For example, you could use topic modeling to identify the most common topics in her songs.
    ''')