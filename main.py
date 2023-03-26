from PIL import Image

import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
st.set_page_config(page_title="Mijn webpagina", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_tekening = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_z7dwyelr.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_izn8gnzq.json")
lottie_mario = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_niwtCZ.json")
img_lottie_animation = Image.open("images/man.png")
img_lottie_ezelsbrug = Image.open("images/ezelsbrug.png")
img_lottie_afbeelding = Image.open("images/fabriek.jpg")
img_lottie_meter = Image.open("images/meter.jpg")
img_lottie_zaag = Image.open("images/zaag.jpg")
img_lottie_opmeten = Image.open("images/opmeten.jpg")


with st.container():
    st.subheader("Hallo, Ik ben Mario :wave:")
    st.title("Kabelbanen plooien doe je zo?")
    st.write(
        """
        Ik werk al verschillende jaren in een een firma dat zowat alles doet met electriciteit.
        Van building systems,Industrie,Hoogspanning Postwerken,Lijnwerken...
        Nu zit ik in de afdeling hoogspanning.Maar ik heb jaren in de industrie,petrochemie gewerkt. 
        """)
    st.write("[Wil je meer info over de firma>](https://spie.be)")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""Kabelbanen leggen is één van de eerste werken
            dat je doet.
            Regelmatig moeten deze worden geplooid.
            Dit noemt men op de werkvloer bajonetten.
            Deze worden meestal op 45° of 30° geplooid.
            De reden hiervoor kom ik later nog op terug.
            Hoe starten we nu om een bajonet of bocht te plooien.
            Dit is niet zo moeilijk als men denkt.
            Er zijn 4 stappen te volgen.
            Optekenen,Opmeten,Uitrekenen en Maken.
            Als je deze 4 stappen volgt zal het maken van een bajonet zeer eenvoudig zijn.:sunglasses:
            
            
        """)
        with right_column:
            st.image(img_lottie_afbeelding)
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:

            st.header("1 Optekennen.")

            st.write("Teken je bajonet op zoals hier onder in het voorbeeld (opmeten)")
            st.write("Teken een driehoek naast je bajonet.")
            st.write("De maat van de driehoek schrijven we er later bij.")
            st.write("Schrijf de maat van de verspringing ook naast je bajonet.")
            st.write("De maat van de de lengte schrijven we er later bij. ")

        with right_column:

            st_lottie(lottie_tekening, height=250,key="tekening")

        #with st.expander("Voor meer info"):
            #st.image(img_lottie_opmeten)


        with st.container():




            st.write("---")
            st.header("2 Opmeten.")







             #st.write("##")
            with st.container():
                st.write("---")


                #left_column, right_column = st.columns(2)

            #with left_column:
                st.write("Hoe meten we dit nu op."
                                 "Dit is zeer eenvoudig.We moeten het verschil vinden tussen de verpringing. "
                                 "Dit is het punt waar de baan nu ligt en waar ze uiteindelijk zal komen te "
                                 "liggen.Hoe doen we dit nu? Eerst zoeken we een vast punt.Dit kan een muur zijn "
                                 "of een een petrel die evenwijdig loopt met onze baan.We meten nu van de linkse kant "
                                 "van de baan naar ons vast punt en dit doen we ook naar de kant waar de baan "
                                 "uiteindelijk zal komen te liggen.Deze twee getallen trekken we van mekaar af en we "
                                 "weten nu hoeveel de verspringing is.Noteer dit getal naast je tekening.Dit hebben we "
                                 "later nog nodig"
                                 ""
                                 "")
                with st.expander("Voor meer info"):
                    st.image(img_lottie_opmeten)


    with st.container():
        st.write("---")
        st.header("3 Uitrekennen.")
        st.write("""In het beging van de text heb ik verteld dat we vooral op 45° of 30° plooien.
        45°graden voor zowat alle kabbels.30° voor dikke kabels.Voor 45° moet men 2 getallen onthouden
          :red[1.40] voor de lengte van de bajonet en :red[4/5 of 0,8 ] voor de driehoek die we moeten uitsnijden
          Voor 30° onthouden we maal 2  voor de lengte van de bajonet en 0,54  voor de driehoek.
          bv we plooien een baan van 20 cm breed en de verspringing is ook 20 cm.Om het 
          het gemakelijk te maken gebruiken we 20cm. OPLOSSING: 20 maal 1,40 = 28 voor de lente van de bajonet. 20 maal 0,8 = 16
          voor de driehoek die we gaan uitsnijden.Hoe rekenen we dit nu uit bv met een baan van 15cm breed
          en een verspringing van 52.4cm.En dit zonder rekenmachiene.Hiervoor gebruiken we een ezelsbrugje.:wink:""")
        with st.expander("Voor meer info"):
        #if st.button('Meer info'):

            st.image(img_lottie_ezelsbrug)
        #else:
        #color = st.color_picker('Pick A Color', '#00f900')
        st.write("Wil je echt niet rekenen:yawning_face:")

        verspringing = st.number_input("Geef de verpringing van de bajonet")
        breete = st.number_input("Geef de breete van de baan? ")
        bajonet = verspringing * 1.40
        driehoek = breete * 0.8
        bajonet2 = verspringing * 2
        driehoek2 = breete * 0.54
        #color = st.color_picker('Pick A Color', '#00f900')
        if st.button('Uitrekenen'):
            st.write("De bajonet is",bajonet,"op 45°")
            st.write("De bajonet is",bajonet2,"op 30°")
            st.write("De driehoek is",driehoek,"op 45°")
            st.write("De driehoek is",driehoek2,"op 30°")

    st.write("Wil je een calculator dat alle graden kan uitrekenen?")
    st.write("Alleen voor Windows.")
    with open("calculator.zip", "rb") as file:
        btn = st.download_button(
            label="Download calculator",
            data=file,
            file_name="calculator.zip",
            mime="calculator.zip"
        )




    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("4 MAKEN")
            st.write("""Nu zijn we aan de laatst stap. Het maken van de bajonet.
            We weten nu hoe we een baan moeten Optekenen,Opmeten en Uitrekenen.
            Slijp of zaag nu netjes de driehoeken uit.Plooi ze naar mekaar en schroef ze vast.:thumbsup:""")
        with right_column:

            st.image(img_lottie_zaag)











        





















    #email bericht


    with st.container():
        st.write("---")
        st.header("zend me een berichtje")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/mariodeyck76@gmail.com" method="POST">
     <input type="text" name="name"placeholder="jou naam" required>
     <input type="email" name="email"placeholder="jou email" required>
     <textarea name="massage"placeholder="jou bericht"required></textarea>
     
                                
     <button type="submit">Send</button>
     </form>"""

        
        left_column,right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with right_column:
            st.empty()


    #st.write("[leer meer op >](https://hln.be)")
