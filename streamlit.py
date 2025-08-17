# Tu installes Streamlit : pip install streamlit
import streamlit as st

# Personnalisation du style
st.markdown("""
    <style>
    body, .main {
        background-color: #111111 !important;
        color: #f5f5f5 !important;
    }
    .stTextInput>div>div>input {
        background-color: #222222 !important;
        color: #f5f5f5 !important;
        border: 1px solid #444444 !important;
    }
    .stMarkdown, .stSubheader, .stSuccess, .stInfo {
        color: #e0e0e0 !important;
    }
    .result-box {
        background: #222222;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        color: #f5f5f5;
        border: 1px solid #444444;
    }
    </style>
""", unsafe_allow_html=True)

# Titre personnalisé
st.markdown('<span style="font-size:18pt; font-weight:bold; color:#f5f5f5;">Bonjour,</span>', unsafe_allow_html=True)
st.markdown('<span style="color:#cccccc;">Entrez un mot, un prénom, ou une date de naissance (format JJMMAA ou JJMMAAAA) pour découvrir sa valeur numérologique.</span>', unsafe_allow_html=True)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre_numero = {lettre: index + 1 for index, lettre in enumerate(alphabet)}
nombres_maitres = {11, 22, 33}
nombres_angelique = {111, 222, 333, 444, 555, 666, 777, 888, 999}

def valeur_lettre(lettre):
    lettre = lettre.upper()
    if lettre in lettre_numero:
        return lettre_numero[lettre]
    if lettre.isdigit():
        num = int(lettre)
        if 1 <= num <= 26:
            return num
    return None

def valeur_mot(mot):
    mot = mot.upper()
    valeurs = [valeur_lettre(lettre) for lettre in mot if valeur_lettre(lettre) is not None]
    return sum(valeurs), valeurs

def reduction_nombre(n):
    if n in nombres_maitres or n in nombres_angelique:
        return n, [n]
    etapes = [n]
    while n > 9:
        n = sum(int(chiffre) for chiffre in str(n))
        etapes.append(n)
        if n in nombres_maitres or n in nombres_angelique:
            break
    return n, etapes

def chemin_de_vie(date_str):
    total = sum(int(chiffre) for chiffre in date_str if chiffre.isdigit())
    chemin, etapes = reduction_nombre(total)
    return chemin, etapes

# Encadré pour la saisie
with st.container():
    mot = st.text_input("📝 Saisie :", key="saisie", help="Mot, prénom ou date (JJMMAA ou JJMMAAAA)")

if mot:
    somme, valeurs = valeur_mot(mot)
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("Valeurs des lettres/chiffres")
    st.markdown(f"<span style='color:#cccccc;'>{valeurs}</span>", unsafe_allow_html=True)
    st.subheader("Somme totale")
    st.markdown(f"<span style='color:#ffffff; font-size:20px;'><b>{somme}</b></span>", unsafe_allow_html=True)

    total_reduit, etapes = reduction_nombre(somme)
    st.subheader("Nombre réduit")
    st.markdown(f"<span style='color:#ffffff; font-size:20px;'><b>{total_reduit}</b></span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:#888888;'>Étapes de réduction : {etapes}</span>", unsafe_allow_html=True)

    if total_reduit in nombres_maitres:
        st.success(f"✨ {total_reduit} est un nombre maître !")
        st.markdown('<span style="color:#cccccc;">Les nombres maîtres sont porteurs d\'une énergie particulière.</span>', unsafe_allow_html=True)
    elif total_reduit in nombres_angelique:
        st.info(f"😇 {total_reduit} est un nombre angélique !")
        st.markdown('<span style="color:#cccccc;">Les nombres angéliques sont considérés comme des messages spirituels.</span>', unsafe_allow_html=True)

    # Chemin de vie si la saisie ressemble à une date
    if mot.isdigit() and (len(mot) == 6 or len(mot) == 8):
        chemin, etapes_chemin = chemin_de_vie(mot)
        st.subheader("Chemin de vie")
        st.markdown(f"<span style='color:#ffffff; font-size:20px;'><b>{chemin}</b></span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#888888;'>Étapes de réduction : {etapes_chemin}</span>", unsafe_allow_html=True)
        if chemin in nombres_maitres:
            st.success(f"✨ {chemin} est un nombre maître pour le chemin de vie !")
        elif chemin in nombres_angelique:
            st.info(f"😇 {chemin} est un nombre angélique pour le chemin de vie !")
    st.markdown('</div>', unsafe_allow_html=True)
