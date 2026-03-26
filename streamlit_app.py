import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Dream Interpreter", page_icon="🌙")

st.title("🌙 Dream Interpreter")
st.write("Application pour interpreter tes reves")

st.divider()

choix = st.radio("Comment veux-tu raconter ton reve ?", ["J'ecris mon reve", "Je parle dans le micro"])

mon_reve = ""

if choix == "J'ecris mon reve":
    mon_reve = st.text_area("Ecris ton reve ici :", height=100)

else:
    st.write("Clique sur le bouton pour enregistrer")
    
    audio = st.audio_input("Enregistre ton reve")
    
    if audio is not None:
        st.success("Enregistrement recu !")
        st.audio(audio)
        
        st.write("Ecris ce que tu as dit :")
        mon_reve = st.text_input("Texte de ton reve :", "Je volais dans le ciel")

st.divider()

style_image = st.selectbox("Style de l'image :", ["Naturel", "Fee rique", "Reveur"])

if st.button("Interpreter mon reve"):
    if mon_reve != "":
        
        st.subheader("Ton reve")
        st.write(mon_reve)
        
        mots = mon_reve.split()
        if len(mots) > 5:
            resumee = mots[0] + " " + mots[1] + " " + mots[2] + " " + mots[3] + " " + mots[4] + "..."
        else:
            resumee = mon_reve
        
        st.subheader("Resume")
        st.write(resumee)
        
        st.subheader("Interpretation")
        
        if "vol" in mon_reve or "ciel" in mon_reve or "nuage" in mon_reve:
            st.write("Tu as envie de liberte")
        elif "peur" in mon_reve or "tombe" in mon_reve or "cauchemar" in mon_reve:
            st.write("Tu as des angoisses")
        elif "eau" in mon_reve or "mer" in mon_reve or "riviere" in mon_reve:
            st.write("Tu as besoin de calme")
        elif "maison" in mon_reve or "famille" in mon_reve or "parent" in mon_reve:
            st.write("Tu penses a ta famille")
        elif "blanc" in mon_reve or "lumiere" in mon_reve:
            st.write("Tu cherches la purete")
        elif "amour" in mon_reve or "coeur" in mon_reve:
            st.write("L'amour est important pour toi")
        elif "travail" in mon_reve or "ecole" in mon_reve:
            st.write("Tu as des pressions")
        elif "animal" in mon_reve or "chat" in mon_reve or "chien" in mon_reve:
            st.write("Ecoute ton instinct")
        elif "mort" in mon_reve or "fin" in mon_reve:
            st.write("Symbole de changement")
        else:
            st.write("Ce reve montre ce que tu ressens")
        
        st.subheader("Image de ton reve")
        
        try:
            mots_pour_image = mon_reve.replace(" ", "+")[:60]
            
            if style_image == "Naturel":
                style = "nature"
            elif style_image == "Fee rique":
                style = "fantasy"
            else:
                style = "dreamy"
            
            adresse = f"https://image.pollinations.ai/prompt/{mots_pour_image}+reve+{style}"
            
            reponse = requests.get(adresse, timeout=25)
            image = Image.open(BytesIO(reponse.content))
            st.image(image, use_container_width=True)
            
        except:
            st.write("L'image n'a pas pu etre generee")
        
    else:
        st.warning("Ecris ou parle de ton reve avant de cliquer")