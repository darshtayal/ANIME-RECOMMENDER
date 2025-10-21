import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("__file__"))))

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
import os

current_dir = os.path.dirname(os.path.abspath("__file__"))
base_dir = os.path.dirname(current_dir)
env_path = os.path.join(base_dir, "api.env")
load_dotenv(env_path)

st.set_page_config(page_title="Anime Recommender", layout='wide')

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()


pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your Anime preferences eg. : Light hearted Anime with school setting")
if query:
    with st.spinner("Fetching recommendations for you...."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)