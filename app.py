import pickle
import string
import streamlit as st
import webbrowser
global Lrdetect_Model
LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Tool")
input_test = st.text_input("provide your text input here", 'Hello my name is jay ')
button_clicked = st.button("Get Language Name")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))

    
import streamlit as st

# Define the layouts for each language
layouts = {
    "English": [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ],
    "French": [
        ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm'],
        ['w', 'x', 'c', 'v', 'b', 'n']
    ],
    "Hindi": [
        ['क', 'ख', 'ग', 'घ', 'ङ'],
        ['च', 'छ', 'ज', 'झ', 'ञ'],
        ['ट', 'ठ', 'ड', 'ढ', 'ण'],
        ['त', 'थ', 'द', 'ध', 'न'],
        ['प', 'फ', 'ब', 'भ', 'म'],
        ['य', 'र', 'ल', 'व'],
        ['श', 'ष', 'स', 'ह'],
        ['क्ष', 'त्र', 'ज्ञ'],
        ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'],
        ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ'],
        ['ं', 'ः', 'ँ', 'अं', 'अः', '।', '॥'],
        ['ऽ', '॰', 'ॱ']
    ],
    "Arabic": [
        ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج'],
        ['ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك'],
        ['ظ', 'ط', 'ذ', 'د', 'ز', 'و', 'ة', 'ى']
    ],
    "Russian": [
        ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
        ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
        ['я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']
    ],
    "Japanese": [
        ['あ', 'い', 'う', 'え', 'お'],
        ['か', 'き', 'く', 'け', 'こ'],
        ['さ', 'し', 'す', 'せ', 'そ'],
        ['た', 'ち', 'つ', 'て', 'と'],
        ['な', 'に', 'ぬ', 'ね', 'の'],
        ['は', 'ひ', 'ふ', 'へ', 'ほ'],
        ['ま', 'み', 'む', 'め', 'も'],
        ['や', 'ゆ', 'よ'],
        ['ら', 'り', 'る', 'れ', 'ろ'],
        ['わ', 'を', 'ん']
    ],
    "Telugu": [
        ['అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ'],
        ['క', 'ఖ', 'గ', 'ఘ', 'ఙ'],
        ['చ', 'ఛ', 'జ', 'ఝ', 'ఞ'],
        ['ట', 'ఠ', 'డ', 'ఢ', 'ణ'],
        ['త', 'థ', 'ద', 'ధ', 'న'],
        ['ప', 'ఫ', 'బ', 'భ', 'మ'],
        ['య', 'ర', 'ల', 'వ'],
        ['శ', 'ష', 'స', 'హ'],
        ['ళ', 'క్ష', 'ఱ', 'ం', 'ః', 'ఁ', '౦', '౧', '౨', '౩', '౪', '౫', '౬', '౭', '౮', '౯']
    ],
    "Tamil": [
        ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ'],
        ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம'],
        ['ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன'],
        ['ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ', '்'],
        ['ௐ', '௧', '௨', '௩', '௪', '௫', '௬', '௭', '௮', '௯']
    ],
    "Chinese": [
        ['我', '是', '一', '个', '学', '生'],
        ['我', '叫', '张', '明', '。'],
        ['你', '好', '吗', '？']
    ],
    "Turkish": [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç', 'ğ']
    ],
    "Urdu": [
        ['ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ'],
        ['د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش'],
        ['ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ']
    ],
    
    "Italian": [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
        ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'è'],
        ['é', 'ì', 'ò', 'ù', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'ç', 'ñ', 'ø', 'å']
    ],
    "German": [
    ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
    ['y', 'x', 'c', 'v', 'b', 'n', 'm', 'ß']
],

"Canadian": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
],
"Swedish": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
],
"Turkish": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ğ', 'ü'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç', ' ', ' ']
],
"Danish": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '¨'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'æ', 'ø', '\''],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-']
],
"Greek": [
    ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν'],
    ['ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'ς', ''],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
],
"Spanish": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'á', 'é', 'í']
],

"Dutch": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ''],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', ' ', ' ', ' ']
],
"Portuguese": [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'á', 'é', '']
],
"Malayalam": [
    ['ക', 'ഖ', 'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ'],
    ['ട', 'ഠ', 'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 'ദ', 'ധ', 'ന'],
    ['പ', 'ഫ', 'ബ', 'ഭ', 'മ', 'യ', 'ര', 'ല', 'വ', 'ശ'],
    ['ഷ', 'സ', 'ഹ', 'ള', 'ഴ', 'റ', 'ാ', 'ി', 'ീ', 'ു'],
    ['ൂ', 'ൃ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ', 'ം', 'ഃ'],
    ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'ഌ', 'എ', 'ഏ'],
    ['ഐ', 'ഒ', 'ഓ', 'ഔ', 'ക്ഷ', 'ജ്ഞ', '൦', '൧', '൨', '൩'],
    ['൪', '൫', '൬', '൭', '൮', '൯', '൰', '൱', '൲', '']
]






    # Add more languages as needed
}

def create_keyboard(layout):
    for row in layout:
        cols = st.columns(len(row))
        for col, char in zip(cols, row):
            if col.button(char, key=char):
                st.session_state.search_term += char

def main():
    st.title("Multilingual Virtual Keyboard")
    
    # Get the selected language from the user
    language = st.selectbox("Select Language", list(layouts.keys()))
    
    st.session_state.search_term = st.session_state.get("search_term", "")
    search_bar_placeholder = st.empty()
    search_bar = search_bar_placeholder.text_input("Type here", value=st.session_state.search_term)

    st.header(f"{language} Keyboard")
    create_keyboard(layouts[language])

    # Javascript to handle keyboard events
    js_code = """
    <script>
    document.addEventListener('keydown', function(event) {
        var key = event.key;
        var search_bar_element = document.getElementById("custom-text-input");
        if (search_bar_element !== document.activeElement) {
            search_bar_element.focus();
        }
        search_bar_element.value += key;
    });
    </script>
    """
    st.components.v1.html(js_code)

if __name__ == "__main__":
    main()
















