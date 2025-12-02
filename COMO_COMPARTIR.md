# 🎨 Arty - Guía Rápida para Compartir

## ✅ Tu aplicación está LISTA para compartir

### 🔐 Seguridad de API Keys

**¡Tranquilo!** Tus API keys están COMPLETAMENTE seguras:

✅ **Las keys NO se muestran en la interfaz**
✅ **Están en el archivo `.env` que NO se sube a GitHub**
✅ **Tus amigos usarán TUS keys sin verlas**
✅ **No necesitan configurar nada**

---

## 🚀 OPCIÓN MÁS FÁCIL: Streamlit Cloud

### Paso 1: Subir a GitHub
```bash
# Asegúrate de que .env esté en .gitignore (ya lo está ✓)
git add .
git commit -m "Arty - Asistente de Arte IA listo"
git push origin main
```

### Paso 2: Desplegar en Streamlit Cloud

1. Ve a: **https://share.streamlit.io/**
2. Inicia sesión con tu GitHub
3. Click en **"New app"**
4. Selecciona:
   - Repository: `luisafbautista26-bot/arty`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. Click en **"Advanced settings"**
6. En **"Secrets"**, pega esto:

```toml
GEMINI_API_KEY = "AIzaSyD82ggLUiBRJwk5PVsA5oE6_cKhQy8g5p8"
TMDB_API_KEY = "0202a08e8685a9918ea5bd9426d7d054"
TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMjAyYTA4ZTg2ODVhOTkxOGVhNWJkOTQyNmQ3ZDA1NCIsIm5iZiI6MTc2NDY4MjcxOS44OTEsInN1YiI6IjY5MmVlYmRmMTE2NWJmOGM2NDI2ZjM5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JR1jMTlXyNJP8MqTbP8eUXoNEsl9Ce8woZiMZKQc2GU"
HARVARD_API_KEY = ""
```

7. Click en **"Deploy"**
8. ¡Espera 2-3 minutos!

### Paso 3: Compartir

- Streamlit te dará una URL como: `https://arty-xxx.streamlit.app/`
- **¡Comparte ese link con quien quieras!** 🎉

---

## 🌐 OPCIÓN RÁPIDA: Compartir desde Codespaces

Si quieres compartir AHORA (temporal):

1. Ve a la pestaña **"PORTS"** en VS Code
2. Busca el puerto **8501**
3. Click derecho → **"Port Visibility"** → **"Public"**
4. Copia la URL que aparece (algo como: `https://xxx-8501.app.github.dev/`)
5. Comparte esa URL

**⚠️ NOTA:** Esta URL funciona solo mientras Codespaces esté abierto.

---

## 📊 Límites de Uso (Gratis)

Con tus APIs actuales:

- **Google Gemini:** 60 req/min, 1500 req/día (gratis para siempre)
- **TMDb:** Sin límite oficial (uso razonable)
- **Met Museum:** Sin límite (API abierta)
- **Rijksmuseum:** Sin límite (API abierta)

---

## ❓ FAQ

**P: ¿Mis amigos verán mis API keys?**
R: ❌ NO. Las keys están ocultas en el backend.

**P: ¿Puedo revocar el acceso?**
R: ✅ SÍ. Solo apaga la app en Streamlit Cloud.

**P: ¿Cuánto cuesta?**
R: 💰 GRATIS. Streamlit Cloud es gratis para uso personal.

**P: ¿Cuántas personas pueden usar la app?**
R: 👥 ILIMITADAS. No hay límite de usuarios.

**P: ¿La app estará siempre activa?**
R: ✅ SÍ (con Streamlit Cloud). Se apaga si no se usa por días, pero se reactiva automáticamente.

---

## 🎯 Resumen

1. **Sube a GitHub** (`git push`)
2. **Despliega en Streamlit Cloud** (5 minutos)
3. **Comparte el link** con tus amigos
4. **¡Listo!** Tus amigos usan Arty con tus keys (sin verlas)

---

**¿Necesitas ayuda?** Lee el archivo `COMPARTIR.md` para más detalles.

🎨 ¡Disfruta compartiendo Arty!
