# 🎨 Asistente de Arte con IA

Chatbot inteligente especializado en arte que ayuda con poesía, identificación de pinturas, recomendaciones de películas e información sobre artistas.

## 🌟 Características

### 1. ✍️ Asistente de Poesía
- Ayuda a redactar poesía en **10 estructuras diferentes**:
  - Soneto (14 versos endecasílabos)
  - Haiku (3 versos: 5-7-5 sílabas)
  - Décima (10 versos octosílabos)
  - Cuarteto, Lira, Terceto
  - Verso Libre, Redondilla, Octava Real, Silva
- **No escribe por ti**, te guía para que escribas tu propio poema
- Contador de sílabas integrado
- Sugerencias de rimas y métrica

### 2. 🖼️ Identificador de Pinturas
- Búsqueda en **múltiples museos del mundo**:
  - The Metropolitan Museum (Met Museum)
  - Rijksmuseum
  - Harvard Art Museums (opcional)
- Información completa: artista, año, dimensiones, técnica
- Imágenes de alta calidad

### 3. 🎬 Recomendaciones de Películas
- Búsqueda por **18 géneros** diferentes
- Búsqueda por temática específica
- Información de TMDb (The Movie Database)
- Sinopsis, valoraciones y posters

### 4. 👤 Información de Artistas
- **Directores de cine**: biografía, filmografía completa
- **Pintores y escritores**: biografías detalladas
- Imágenes y datos biográficos
- Fuentes: TMDb + Wikipedia

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd arty
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar API Keys
Copia el archivo `.env.example` a `.env`:
```bash
cp .env.example .env
```

Edita `.env` y agrega tus API keys:
```env
GEMINI_API_KEY=tu_clave_aqui
TMDB_API_KEY=tu_clave_aqui
TMDB_ACCESS_TOKEN=tu_token_aqui
HARVARD_API_KEY=tu_clave_aqui  # Opcional
```

## 🔑 Obtener API Keys

### Google Gemini AI (GRATIS)
1. Ve a: https://makersuite.google.com/app/apikey
2. Inicia sesión con tu cuenta Google
3. Crea una nueva API key
4. Copia y pega en `GEMINI_API_KEY`

### TMDb - The Movie Database (GRATIS)
1. Ve a: https://www.themoviedb.org/settings/api
2. Regístrate (gratis)
3. Solicita una API key
4. Copia la API Key en `TMDB_API_KEY`
5. Copia el Read Access Token en `TMDB_ACCESS_TOKEN`

### Harvard Art Museums (OPCIONAL)
1. Ve a: https://www.harvardartmuseums.org/collections/api
2. Registra tu aplicación
3. Copia la API key

## ▶️ Ejecutar la Aplicación

```bash
streamlit run streamlit_app.py
```

La aplicación se abrirá en tu navegador en: http://localhost:8501

## 📖 Uso

### Módulo de Poesía
1. Selecciona "✍️ Ayuda con Poesía" en el menú lateral
2. Escribe tu idea o sentimiento
3. Elige una estructura poética
4. Haz clic en "Ayudarme a redactar"
5. La IA te guiará con sugerencias (NO escribe el poema completo)

### Identificar Pinturas
1. Selecciona "🖼️ Identificar Pinturas"
2. Escribe el nombre de la pintura o artista
3. Explora los resultados de múltiples museos

### Recomendaciones de Películas
1. Selecciona "🎬 Recomendaciones de Películas"
2. Elige género o búsqueda por temática
3. Ajusta la cantidad de resultados
4. Explora recomendaciones personalizadas

### Información de Artistas
1. Selecciona "👤 Info de Artistas/Directores"
2. Elige el tipo de artista
3. Escribe el nombre
4. Obtén biografía completa y obras

## 🛠️ Tecnologías Utilizadas

- **Frontend**: Streamlit
- **IA Generativa**: Google Gemini AI
- **APIs de Datos**:
  - The Metropolitan Museum API
  - Rijksmuseum API
  - Harvard Art Museums API
  - TMDb (The Movie Database)
  - Wikipedia API
- **Python 3.8+**

## 📝 Estructura del Proyecto

```
arty/
├── streamlit_app.py      # Aplicación principal
├── requirements.txt      # Dependencias Python
├── .env                 # Variables de entorno (API keys)
├── .env.example         # Plantilla de configuración
├── README.md            # Documentación
└── data/                # Datos (opcional)
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 🙏 Créditos

- **APIs utilizadas**:
  - Google Gemini AI
  - The Metropolitan Museum
  - Rijksmuseum
  - Harvard Art Museums
  - TMDb (The Movie Database)
  - Wikipedia

## 🐛 Reportar Problemas

Si encuentras algún bug o tienes sugerencias, por favor abre un issue en GitHub.

## 📧 Contacto

Para preguntas o comentarios, contacta al desarrollador.

---

**¡Disfruta explorando el mundo del arte con IA! 🎨✨**
