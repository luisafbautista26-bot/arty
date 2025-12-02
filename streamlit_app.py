import streamlit as st
import requests
import random
from datetime import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

# Configurar Gemini AI
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None

# Configuración de la página
st.set_page_config(
    page_title="Arty - Tu Asistente de Arte IA",
    page_icon="🎨",
    layout="wide"
)

# ==================== MÓDULO 1: POESÍA ====================
class PoetryAssistant:
    """Asistente para redacción de poesía con diferentes estructuras."""
    
    ESTRUCTURAS = {
        "Soneto": {
            "descripcion": "14 versos endecasílabos (11 sílabas), esquema ABBA ABBA CDC DCD",
            "versos": 14,
            "silabas": 11,
            "esquema": "ABBA ABBA CDC DCD"
        },
        "Haiku": {
            "descripcion": "3 versos: 5-7-5 sílabas, temática naturaleza/momento",
            "versos": 3,
            "silabas": [5, 7, 5],
            "esquema": "Libre"
        },
        "Décima": {
            "descripcion": "10 versos octosílabos (8 sílabas), esquema ABBAACCDDC",
            "versos": 10,
            "silabas": 8,
            "esquema": "ABBAACCDDC"
        },
        "Cuarteto": {
            "descripcion": "4 versos endecasílabos, esquema ABBA",
            "versos": 4,
            "silabas": 11,
            "esquema": "ABBA"
        },
        "Lira": {
            "descripcion": "5 versos con esquema 7a-11B-7a-7b-11B",
            "versos": 5,
            "silabas": [7, 11, 7, 7, 11],
            "esquema": "aBabB"
        },
        "Verso Libre": {
            "descripcion": "Sin restricciones métricas ni de rima",
            "versos": "Variable",
            "silabas": "Variable",
            "esquema": "Libre"
        },
        "Redondilla": {
            "descripcion": "4 versos octosílabos, esquema ABBA",
            "versos": 4,
            "silabas": 8,
            "esquema": "ABBA"
        },
        "Terceto": {
            "descripcion": "3 versos endecasílabos, esquema ABA",
            "versos": 3,
            "silabas": 11,
            "esquema": "ABA"
        },
        "Octava Real": {
            "descripcion": "8 versos endecasílabos, esquema ABABABCC",
            "versos": 8,
            "silabas": 11,
            "esquema": "ABABABCC"
        },
        "Silva": {
            "descripcion": "Combinación libre de versos de 7 y 11 sílabas",
            "versos": "Variable",
            "silabas": [7, 11],
            "esquema": "Libre"
        }
    }
    
    @staticmethod
    def ayudar_con_poesia(idea_usuario, estructura_elegida):
        """Ayuda al usuario a redactar su idea en la estructura poética elegida."""
        if not model:
            return "⚠️ Por favor configura la API key de Gemini para usar esta función."
        
        estructura_info = PoetryAssistant.ESTRUCTURAS.get(estructura_elegida)
        
        prompt = f"""Eres un asistente literario experto en poesía. El usuario tiene una idea y quiere que lo ayudes a redactarla (NO escribirla completamente por él) en formato de {estructura_elegida}.

Estructura {estructura_elegida}:
- Descripción: {estructura_info['descripcion']}
- Número de versos: {estructura_info['versos']}
- Sílabas por verso: {estructura_info['silabas']}
- Esquema de rima: {estructura_info['esquema']}

Idea del usuario: "{idea_usuario}"

Tu trabajo:
1. Analiza la idea del usuario
2. Sugiere cómo distribuir la idea en los versos de la estructura
3. Propone palabras que rimen según el esquema
4. Da consejos sobre métrica y ritmo
5. Ofrece 2-3 primeros versos como EJEMPLO (no completes todo el poema)
6. Deja que el usuario complete el resto con tu guía

NO escribas el poema completo. Ayuda al usuario a que lo escriba él mismo."""

        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error al generar ayuda: {str(e)}"
    
    @staticmethod
    def contar_silabas(verso):
        """Contador aproximado de sílabas en español."""
        # Simplificado - en producción usar librería especializada
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        silabas = 0
        anterior_vocal = False
        
        for char in verso:
            if char in vocales:
                if not anterior_vocal:
                    silabas += 1
                anterior_vocal = True
            else:
                anterior_vocal = False
        
        return silabas


# ==================== MÓDULO 2: IDENTIFICACIÓN DE PINTURAS ====================
class ArtIdentifier:
    """Identificador de pinturas usando múltiples APIs de museos."""
    
    @staticmethod
    def buscar_en_met_museum(query):
        """Busca en The Metropolitan Museum API."""
        try:
            # Búsqueda
            search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}"
            search_response = requests.get(search_url, timeout=5)
            
            if search_response.status_code != 200:
                return None
            
            data = search_response.json()
            if not data.get('objectIDs'):
                return None
            
            # Obtener detalles del primer resultado
            object_id = data['objectIDs'][0]
            object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
            object_response = requests.get(object_url, timeout=5)
            
            if object_response.status_code == 200:
                artwork = object_response.json()
                return {
                    'titulo': artwork.get('title', 'Desconocido'),
                    'artista': artwork.get('artistDisplayName', 'Desconocido'),
                    'año': artwork.get('objectDate', 'Desconocido'),
                    'cultura': artwork.get('culture', 'N/A'),
                    'medio': artwork.get('medium', 'N/A'),
                    'dimensiones': artwork.get('dimensions', 'N/A'),
                    'departamento': artwork.get('department', 'N/A'),
                    'imagen': artwork.get('primaryImage', ''),
                    'fuente': 'Metropolitan Museum'
                }
        except Exception as e:
            st.error(f"Error en Met Museum: {str(e)}")
            return None
    
    @staticmethod
    def buscar_en_rijksmuseum(query):
        """Busca en Rijksmuseum API."""
        try:
            url = f"https://www.rijksmuseum.nl/api/en/collection?key=0fiuZFh4&q={query}&ps=1"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('artObjects'):
                    art = data['artObjects'][0]
                    return {
                        'titulo': art.get('title', 'Desconocido'),
                        'artista': art.get('principalOrFirstMaker', 'Desconocido'),
                        'año': art.get('dating', {}).get('presentingDate', 'Desconocido'),
                        'imagen': art.get('webImage', {}).get('url', ''),
                        'fuente': 'Rijksmuseum'
                    }
        except Exception as e:
            st.error(f"Error en Rijksmuseum: {str(e)}")
            return None
    
    @staticmethod
    def buscar_en_harvard(query):
        """Busca en Harvard Art Museums API."""
        api_key = os.getenv('HARVARD_API_KEY')
        if not api_key or api_key == 'your_harvard_key_here':
            return None
        
        try:
            url = f"https://api.harvardartmuseums.org/object?apikey={api_key}&q={query}&size=1"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('records'):
                    art = data['records'][0]
                    return {
                        'titulo': art.get('title', 'Desconocido'),
                        'artista': art.get('people', [{}])[0].get('name', 'Desconocido') if art.get('people') else 'Desconocido',
                        'año': art.get('dated', 'Desconocido'),
                        'cultura': art.get('culture', 'N/A'),
                        'imagen': art.get('primaryimageurl', ''),
                        'fuente': 'Harvard Art Museums'
                    }
        except Exception as e:
            st.error(f"Error en Harvard: {str(e)}")
            return None
    
    @staticmethod
    def identificar_pintura(query):
        """Busca en múltiples APIs y combina resultados."""
        resultados = []
        
        # Buscar en todas las APIs
        met_result = ArtIdentifier.buscar_en_met_museum(query)
        if met_result:
            resultados.append(met_result)
        
        rijks_result = ArtIdentifier.buscar_en_rijksmuseum(query)
        if rijks_result:
            resultados.append(rijks_result)
        
        harvard_result = ArtIdentifier.buscar_en_harvard(query)
        if harvard_result:
            resultados.append(harvard_result)
        
        return resultados


# ==================== MÓDULO 3: RECOMENDACIONES DE PELÍCULAS ====================
class MovieRecommender:
    """Recomendador de películas usando TMDb API."""
    
    TMDB_API_KEY = os.getenv('TMDB_API_KEY')
    BASE_URL = "https://api.themoviedb.org/3"
    
    GENEROS = {
        28: "Acción", 12: "Aventura", 16: "Animación", 35: "Comedia",
        80: "Crimen", 99: "Documental", 18: "Drama", 10751: "Familia",
        14: "Fantasía", 36: "Historia", 27: "Terror", 10402: "Música",
        9648: "Misterio", 10749: "Romance", 878: "Ciencia Ficción",
        10770: "Película de TV", 53: "Thriller", 10752: "Bélica", 37: "Western"
    }
    
    @staticmethod
    def recomendar_por_genero(genero, cantidad=5):
        """Recomienda películas por género."""
        try:
            # Encontrar el ID del género
            genero_id = None
            for id, nombre in MovieRecommender.GENEROS.items():
                if genero.lower() in nombre.lower():
                    genero_id = id
                    break
            
            if not genero_id:
                return None
            
            url = f"{MovieRecommender.BASE_URL}/discover/movie"
            params = {
                'api_key': MovieRecommender.TMDB_API_KEY,
                'with_genres': genero_id,
                'sort_by': 'vote_average.desc',
                'vote_count.gte': 1000,
                'language': 'es-ES',
                'page': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                peliculas = []
                
                for movie in data['results'][:cantidad]:
                    peliculas.append({
                        'titulo': movie.get('title', 'Desconocido'),
                        'año': movie.get('release_date', 'N/A')[:4] if movie.get('release_date') else 'N/A',
                        'sinopsis': movie.get('overview', 'No disponible'),
                        'valoracion': movie.get('vote_average', 0),
                        'poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else None
                    })
                
                return peliculas
        except Exception as e:
            st.error(f"Error al buscar películas: {str(e)}")
            return None
    
    @staticmethod
    def buscar_por_tematica(tematica, cantidad=5):
        """Busca películas por temática específica."""
        try:
            url = f"{MovieRecommender.BASE_URL}/search/movie"
            params = {
                'api_key': MovieRecommender.TMDB_API_KEY,
                'query': tematica,
                'language': 'es-ES',
                'page': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                peliculas = []
                
                for movie in data['results'][:cantidad]:
                    peliculas.append({
                        'titulo': movie.get('title', 'Desconocido'),
                        'año': movie.get('release_date', 'N/A')[:4] if movie.get('release_date') else 'N/A',
                        'sinopsis': movie.get('overview', 'No disponible'),
                        'valoracion': movie.get('vote_average', 0),
                        'poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else None
                    })
                
                return peliculas
        except Exception as e:
            st.error(f"Error al buscar por temática: {str(e)}")
            return None


# ==================== MÓDULO 4: INFORMACIÓN DE ARTISTAS ====================
class ArtistInfo:
    """Información sobre artistas, pintores, escritores y directores."""
    
    @staticmethod
    def buscar_en_wikipedia(nombre):
        """Busca información del artista en Wikipedia."""
        try:
            # Buscar página
            search_url = "https://es.wikipedia.org/w/api.php"
            search_params = {
                'action': 'query',
                'list': 'search',
                'srsearch': nombre,
                'format': 'json',
                'srlimit': 1
            }
            
            search_response = requests.get(search_url, params=search_params, timeout=5)
            search_data = search_response.json()
            
            if not search_data['query']['search']:
                return None
            
            page_title = search_data['query']['search'][0]['title']
            
            # Obtener extracto
            extract_params = {
                'action': 'query',
                'prop': 'extracts|pageimages',
                'exintro': True,
                'explaintext': True,
                'titles': page_title,
                'format': 'json',
                'piprop': 'original'
            }
            
            extract_response = requests.get(search_url, params=extract_params, timeout=5)
            extract_data = extract_response.json()
            
            pages = extract_data['query']['pages']
            page_id = list(pages.keys())[0]
            page = pages[page_id]
            
            return {
                'nombre': page.get('title', nombre),
                'biografia': page.get('extract', 'No disponible'),
                'imagen': page.get('original', {}).get('source', ''),
                'fuente': 'Wikipedia'
            }
        except Exception as e:
            st.error(f"Error en Wikipedia: {str(e)}")
            return None
    
    @staticmethod
    def buscar_director_tmdb(nombre):
        """Busca información de un director de cine en TMDb."""
        try:
            url = f"{MovieRecommender.BASE_URL}/search/person"
            params = {
                'api_key': MovieRecommender.TMDB_API_KEY,
                'query': nombre,
                'language': 'es-ES'
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data['results']:
                    person = data['results'][0]
                    person_id = person['id']
                    
                    # Obtener detalles completos
                    detail_url = f"{MovieRecommender.BASE_URL}/person/{person_id}"
                    detail_params = {
                        'api_key': MovieRecommender.TMDB_API_KEY,
                        'language': 'es-ES'
                    }
                    
                    detail_response = requests.get(detail_url, params=detail_params, timeout=5)
                    detail_data = detail_response.json()
                    
                    # Obtener películas dirigidas
                    credits_url = f"{MovieRecommender.BASE_URL}/person/{person_id}/movie_credits"
                    credits_response = requests.get(credits_url, params=detail_params, timeout=5)
                    credits_data = credits_response.json()
                    
                    peliculas_dirigidas = []
                    for movie in credits_data.get('crew', []):
                        if movie.get('job') == 'Director':
                            peliculas_dirigidas.append({
                                'titulo': movie.get('title'),
                                'año': movie.get('release_date', 'N/A')[:4] if movie.get('release_date') else 'N/A'
                            })
                    
                    return {
                        'nombre': detail_data.get('name', nombre),
                        'biografia': detail_data.get('biography', 'No disponible'),
                        'nacimiento': detail_data.get('birthday', 'N/A'),
                        'lugar': detail_data.get('place_of_birth', 'N/A'),
                        'imagen': f"https://image.tmdb.org/t/p/w500{detail_data['profile_path']}" if detail_data.get('profile_path') else None,
                        'peliculas': peliculas_dirigidas[:10],
                        'fuente': 'TMDb'
                    }
        except Exception as e:
            st.error(f"Error en TMDb: {str(e)}")
            return None


# ==================== INTERFAZ STREAMLIT ====================
def main():
    st.title("🎨 Arty - Tu Asistente de Arte IA")
    st.markdown("*Explora el mundo del arte: poesía, pintura, cine y cultura*")
    
    # Sidebar para selección de módulo
    st.sidebar.title("🎯 Selecciona una función")
    modulo = st.sidebar.radio(
        "¿Qué quieres hacer?",
        ["✍️ Ayuda con Poesía", "🖼️ Identificar Pinturas", "🎬 Recomendaciones de Películas", "👤 Info de Artistas/Directores"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("💡 **Tip:** Este asistente usa IA y múltiples APIs de museos y bases de datos culturales.")
    
    # ==================== MÓDULO 1: POESÍA ====================
    if modulo == "✍️ Ayuda con Poesía":
        st.header("✍️ Asistente de Redacción Poética")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Tu idea poética")
            idea = st.text_area(
                "Escribe tu idea, sentimiento o tema que quieres expresar:",
                height=150,
                placeholder="Ejemplo: Quiero escribir sobre la melancolía del otoño y las hojas cayendo..."
            )
        
        with col2:
            st.subheader("Estructura deseada")
            estructura = st.selectbox(
                "Elige la estructura poética:",
                list(PoetryAssistant.ESTRUCTURAS.keys())
            )
            
            # Mostrar información de la estructura
            info_estructura = PoetryAssistant.ESTRUCTURAS[estructura]
            st.info(f"**{estructura}**\n\n{info_estructura['descripcion']}")
        
        if st.button("🎯 Ayudarme a redactar", type="primary"):
            if not idea:
                st.warning("⚠️ Por favor escribe tu idea primero")
            else:
                with st.spinner("✨ Analizando tu idea y preparando sugerencias..."):
                    ayuda = PoetryAssistant.ayudar_con_poesia(idea, estructura)
                    st.markdown("### 📝 Sugerencias para tu poema")
                    st.markdown(ayuda)
        
        # Sección de contador de sílabas
        st.markdown("---")
        st.subheader("🔢 Contador de Sílabas")
        verso_test = st.text_input("Escribe un verso para contar sus sílabas:")
        if verso_test:
            silabas = PoetryAssistant.contar_silabas(verso_test)
            st.success(f"**{silabas} sílabas** (aproximado)")
    
    # ==================== MÓDULO 2: IDENTIFICAR PINTURAS ====================
    elif modulo == "🖼️ Identificar Pinturas":
        st.header("🖼️ Identificador de Pinturas")
        st.markdown("Busca información sobre pinturas famosas por título, artista o descripción")
        
        busqueda = st.text_input(
            "🔍 Buscar pintura:",
            placeholder="Ejemplo: La noche estrellada, Mona Lisa, Guernica..."
        )
        
        if st.button("🔎 Buscar", type="primary"):
            if busqueda:
                with st.spinner("🎨 Buscando en museos de todo el mundo..."):
                    resultados = ArtIdentifier.identificar_pintura(busqueda)
                    
                    if resultados:
                        st.success(f"✅ Encontrados {len(resultados)} resultado(s)")
                        
                        for i, resultado in enumerate(resultados):
                            with st.expander(f"📌 {resultado['titulo']} - {resultado['fuente']}", expanded=(i==0)):
                                col1, col2 = st.columns([1, 2])
                                
                                with col1:
                                    if resultado.get('imagen'):
                                        st.image(resultado['imagen'], use_container_width=True)
                                    else:
                                        st.info("Sin imagen disponible")
                                
                                with col2:
                                    st.markdown(f"**🎨 Título:** {resultado['titulo']}")
                                    st.markdown(f"**👤 Artista:** {resultado['artista']}")
                                    st.markdown(f"**📅 Año:** {resultado['año']}")
                                    
                                    if resultado.get('cultura'):
                                        st.markdown(f"**🌍 Cultura:** {resultado['cultura']}")
                                    if resultado.get('medio'):
                                        st.markdown(f"**🖌️ Medio:** {resultado['medio']}")
                                    if resultado.get('dimensiones'):
                                        st.markdown(f"**📏 Dimensiones:** {resultado['dimensiones']}")
                                    if resultado.get('departamento'):
                                        st.markdown(f"**🏛️ Departamento:** {resultado['departamento']}")
                                    
                                    st.caption(f"Fuente: {resultado['fuente']}")
                    else:
                        st.warning("❌ No se encontraron resultados. Intenta con otro término de búsqueda.")
            else:
                st.warning("⚠️ Por favor ingresa un término de búsqueda")
    
    # ==================== MÓDULO 3: RECOMENDACIONES DE PELÍCULAS ====================
    elif modulo == "🎬 Recomendaciones de Películas":
        st.header("🎬 Recomendador de Películas")
        
        tipo_busqueda = st.radio("Buscar por:", ["Género", "Temática específica"])
        
        if tipo_busqueda == "Género":
            generos_disponibles = list(set(MovieRecommender.GENEROS.values()))
            genero = st.selectbox("Selecciona un género:", sorted(generos_disponibles))
            cantidad = st.slider("¿Cuántas películas quieres?", 1, 10, 5)
            
            if st.button("🎥 Recomendar", type="primary"):
                with st.spinner("🎬 Buscando las mejores películas..."):
                    peliculas = MovieRecommender.recomendar_por_genero(genero, cantidad)
                    
                    if peliculas:
                        st.success(f"✅ {len(peliculas)} recomendaciones de {genero}")
                        
                        for pelicula in peliculas:
                            with st.expander(f"🎬 {pelicula['titulo']} ({pelicula['año']}) - ⭐ {pelicula['valoracion']}/10"):
                                col1, col2 = st.columns([1, 3])
                                
                                with col1:
                                    if pelicula['poster']:
                                        st.image(pelicula['poster'], use_container_width=True)
                                
                                with col2:
                                    st.markdown(f"**Año:** {pelicula['año']}")
                                    st.markdown(f"**Valoración:** ⭐ {pelicula['valoracion']}/10")
                                    st.markdown(f"**Sinopsis:** {pelicula['sinopsis']}")
                    else:
                        st.error("❌ No se pudieron obtener recomendaciones")
        
        else:  # Temática específica
            tematica = st.text_input(
                "🔍 Buscar por temática:",
                placeholder="Ejemplo: vampiros, segunda guerra mundial, viajes en el tiempo..."
            )
            cantidad = st.slider("¿Cuántas películas quieres?", 1, 10, 5)
            
            if st.button("🎥 Buscar", type="primary"):
                if tematica:
                    with st.spinner("🎬 Buscando películas relacionadas..."):
                        peliculas = MovieRecommender.buscar_por_tematica(tematica, cantidad)
                        
                        if peliculas:
                            st.success(f"✅ {len(peliculas)} películas encontradas sobre '{tematica}'")
                            
                            for pelicula in peliculas:
                                with st.expander(f"🎬 {pelicula['titulo']} ({pelicula['año']}) - ⭐ {pelicula['valoracion']}/10"):
                                    col1, col2 = st.columns([1, 3])
                                    
                                    with col1:
                                        if pelicula['poster']:
                                            st.image(pelicula['poster'], use_container_width=True)
                                    
                                    with col2:
                                        st.markdown(f"**Año:** {pelicula['año']}")
                                        st.markdown(f"**Valoración:** ⭐ {pelicula['valoracion']}/10")
                                        st.markdown(f"**Sinopsis:** {pelicula['sinopsis']}")
                        else:
                            st.error("❌ No se encontraron películas")
                else:
                    st.warning("⚠️ Por favor ingresa una temática")
    
    # ==================== MÓDULO 4: INFO DE ARTISTAS ====================
    elif modulo == "👤 Info de Artistas/Directores":
        st.header("👤 Información de Artistas y Directores")
        
        tipo_artista = st.radio("Tipo de artista:", ["🎬 Director de Cine", "🎨 Pintor/Escritor (General)"])
        
        nombre = st.text_input(
            "Nombre del artista:",
            placeholder="Ejemplo: Frida Kahlo, Gabriel García Márquez, Steven Spielberg..."
        )
        
        if st.button("🔍 Buscar Información", type="primary"):
            if nombre:
                with st.spinner(f"📚 Buscando información sobre {nombre}..."):
                    if tipo_artista == "🎬 Director de Cine":
                        # Buscar primero en TMDb
                        info_tmdb = ArtistInfo.buscar_director_tmdb(nombre)
                        info_wiki = ArtistInfo.buscar_en_wikipedia(nombre)
                        
                        if info_tmdb:
                            st.success(f"✅ Información encontrada: {info_tmdb['nombre']}")
                            
                            col1, col2 = st.columns([1, 2])
                            
                            with col1:
                                if info_tmdb.get('imagen'):
                                    st.image(info_tmdb['imagen'], use_container_width=True)
                            
                            with col2:
                                st.markdown(f"### {info_tmdb['nombre']}")
                                st.markdown(f"**📅 Nacimiento:** {info_tmdb['nacimiento']}")
                                st.markdown(f"**📍 Lugar:** {info_tmdb['lugar']}")
                            
                            st.markdown("### 📖 Biografía")
                            st.write(info_tmdb['biografia'] if info_tmdb['biografia'] != 'No disponible' else info_wiki.get('biografia', 'No disponible'))
                            
                            if info_tmdb.get('peliculas'):
                                st.markdown("### 🎬 Películas Dirigidas")
                                for pelicula in info_tmdb['peliculas']:
                                    st.markdown(f"- **{pelicula['titulo']}** ({pelicula['año']})")
                        
                        elif info_wiki:
                            st.success(f"✅ Información encontrada: {info_wiki['nombre']}")
                            
                            if info_wiki.get('imagen'):
                                st.image(info_wiki['imagen'], width=300)
                            
                            st.markdown(f"### {info_wiki['nombre']}")
                            st.markdown("### �� Biografía")
                            st.write(info_wiki['biografia'])
                        
                        else:
                            st.error("❌ No se encontró información")
                    
                    else:  # Pintor/Escritor General
                        info_wiki = ArtistInfo.buscar_en_wikipedia(nombre)
                        
                        if info_wiki:
                            st.success(f"✅ Información encontrada: {info_wiki['nombre']}")
                            
                            if info_wiki.get('imagen'):
                                st.image(info_wiki['imagen'], width=400)
                            
                            st.markdown(f"### {info_wiki['nombre']}")
                            st.markdown("### 📖 Biografía")
                            st.write(info_wiki['biografia'])
                            st.caption(f"Fuente: {info_wiki['fuente']}")
                        else:
                            st.error("❌ No se encontró información")
            else:
                st.warning("⚠️ Por favor ingresa el nombre del artista")
    
    # Footer
    st.markdown("---")
    st.caption("🎨 Arty - Tu Asistente de Arte IA | Powered by Google Gemini, TMDb, Met Museum, Rijksmuseum & Wikipedia")


if __name__ == "__main__":
    main()
