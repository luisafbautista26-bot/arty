# 🎨 Arty - Instrucciones para Compartir

## Para Compartir la Aplicación con Tus Amigos

### ✅ Seguridad de las API Keys

**¡Buenas noticias!** Tus API keys están completamente seguras y ocultas:

- ✅ Las keys están en el archivo `.env` (NO se comparte)
- ✅ Las keys **NO aparecen** en la interfaz de usuario
- ✅ Tus amigos usarán TUS keys automáticamente
- ✅ No necesitan configurar nada

### 🌐 Opciones para Compartir

#### **Opción 1: Desplegar en Streamlit Cloud (RECOMENDADO)**

1. **Sube tu código a GitHub:**
   ```bash
   git add .
   git commit -m "Agregar Arty - Asistente de Arte IA"
   git push origin main
   ```

2. **Ve a Streamlit Cloud:**
   - Visita: https://share.streamlit.io/
   - Inicia sesión con GitHub
   - Click en "New app"
   - Selecciona tu repositorio: `luisafbautista26-bot/arty`
   - Main file: `streamlit_app.py`

3. **Configura los Secrets (API Keys):**
   - En Streamlit Cloud, ve a "Settings" → "Secrets"
   - Copia y pega el contenido de tu archivo `.env`:
   ```toml
   GEMINI_API_KEY = "AIzaSyD82ggLUiBRJwk5PVsA5oE6_cKhQy8g5p8"
   TMDB_API_KEY = "0202a08e8685a9918ea5bd9426d7d054"
   TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMjAyYTA4ZTg2ODVhOTkxOGVhNWJkOTQyNmQ3ZDA1NCIsIm5iZiI6MTc2NDY4MjcxOS44OTEsInN1YiI6IjY5MmVlYmRmMTE2NWJmOGM2NDI2ZjM5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JR1jMTlXyNJP8MqTbP8eUXoNEsl9Ce8woZiMZKQc2GU"
   HARVARD_API_KEY = ""
   ```

4. **Comparte el enlace:**
   - Streamlit te dará una URL como: `https://arty-xxx.streamlit.app/`
   - ¡Comparte ese link con tus amigos!

#### **Opción 2: Compartir Codespaces/Puerto Local**

Si estás en GitHub Codespaces (como ahora):

1. **Hacer público el puerto:**
   - Ve a la pestaña "PORTS" en VS Code
   - Click derecho en el puerto 8501
   - Selecciona "Port Visibility" → "Public"

2. **Compartir la URL:**
   - Copia la URL del puerto 8501
   - Se verá como: `https://xxx-8501.app.github.dev/`
   - Comparte ese link con tus amigos

**⚠️ IMPORTANTE:** Con esta opción:
- El link funciona mientras tu Codespace esté activo
- Si cierras Codespaces, el link dejará de funcionar
- Cada vez que reinicies, la URL puede cambiar

#### **Opción 3: Desplegar en Otras Plataformas**

- **Hugging Face Spaces** (gratis)
- **Render** (gratis con límites)
- **Railway** (gratis con límites)
- **Google Cloud Run**
- **AWS/Azure**

### 🔐 ¿Qué Pueden Ver Tus Amigos?

✅ **SÍ pueden:**
- Usar todas las funcionalidades de Arty
- Generar poesía con Gemini AI
- Buscar pinturas y películas
- Ver información de artistas

❌ **NO pueden:**
- Ver tus API keys
- Modificar la configuración
- Acceder al código fuente (a menos que compartas el repo)

### 📊 Límites de las APIs Gratuitas

Con tus API keys actuales:

**Google Gemini:**
- 60 requests por minuto
- 1500 requests por día
- Gratis indefinidamente

**TMDb:**
- Sin límite de requests publicado
- Uso razonable esperado

**Met Museum / Rijksmuseum:**
- Sin límites (APIs abiertas)

### 🚀 Pasos Rápidos para Compartir

1. **Añade archivo `.gitignore` para proteger tus keys:**
   ```bash
   echo ".env" >> .gitignore
   ```

2. **Sube a GitHub:**
   ```bash
   git add .
   git commit -m "Arty listo para compartir"
   git push
   ```

3. **Despliega en Streamlit Cloud** (ver Opción 1 arriba)

4. **Comparte el link** con tus amigos 🎉

### 💡 Recomendaciones

- ✅ **USA Streamlit Cloud** - Es gratis, fácil y profesional
- ✅ **Agrega `.env` al `.gitignore`** - Protege tus keys
- ✅ **Monitorea el uso** - Revisa tus cuotas de API ocasionalmente
- ⚠️ **NO compartas** el archivo `.env` directamente

### 📞 Soporte

Si tus amigos tienen problemas:
1. Verifica que Streamlit Cloud esté activo
2. Revisa que los secrets estén configurados correctamente
3. Mira los logs en Streamlit Cloud para diagnosticar errores

---

¡Disfruta compartiendo Arty con tus amigos! 🎨✨
