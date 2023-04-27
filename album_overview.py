import streamlit as st
import pandas as pd

def album_overview(display=True):
    
    df = pd.read_csv('final_data.csv')
    
    albums_list = [x.capitalize() for x in list(df['album'].unique())]

    # selector for choosing an album
    selected_album = st.selectbox("Select an album", albums_list)
    selected_album = selected_album.lower()
    
    # section header
    st.markdown("<h3 style='text-align: left;'>Album Overview</h2>", unsafe_allow_html=True)

    # creating columns
    left_column, right_column = st.columns(2)
    
    #displaying album cover on the left
    with left_column:
        album_cover = df.loc[df['album'] == selected_album, 'image'].head(1).to_string(index=False)
        st.image(album_cover, use_column_width=True)
    
    # displaying album metrics on the right
    with right_column:
        # release date
        st.metric(label="Release Date", value=df.loc[df['album'] == selected_album, 'release_date'].head(1).to_string(index=False))
        
        # number of songs
        count_by_album_df = df.groupby('album').count().reset_index()
        st.metric(label="Number of Songs", value=count_by_album_df.loc[count_by_album_df['album'] == selected_album, 'title'].to_string(index=False))
        
        # total duration
        sum_by_album_df = df.groupby('album').sum().reset_index()
        st.metric(label="Total Duration (minutes)", value=round(sum_by_album_df.loc[sum_by_album_df['album'] == selected_album, 'duration_ms'].astype(float)/60000, 2))
        
    
    # creating columns
    left_column, right_column = st.columns(2)
    
    #displaying album cover on the left
    with left_column:
        st.markdown("<h3 style='text-align: left;'>Track List</h2>", unsafe_allow_html=True)

        track_list = df.loc[df['album'] == selected_album, ['track_number', 'title', 'lyrics']].sort_values(by='track_number').reset_index(drop=True)
        track_list = track_list.rename(columns={'track_number': 'Track Number', 'title': 'Track Title', 'lyrics': 'Track Lyrics'})
        track_list = track_list.set_index('Track Number')

        st.dataframe(track_list[['Track Title']], width=500)
    
    with right_column:
        st.markdown("<h3 style='text-align: left;'>Track Lyrics</h2>", unsafe_allow_html=True)
        selected_track = st.selectbox("Select a track", list(df.loc[df['album'] == selected_album, ['title', 'track_number']].sort_values(by='track_number')['title']))
        st.write(df.loc[df['title'] == selected_track, 'lyrics'].values[0])