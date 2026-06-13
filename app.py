import streamlit as st

# =====================================================================
# CONFIGURACIÓN DE PÁGINA Y ESTILOS CSS GLOBALES
# =====================================================================
st.set_page_config(
    page_title="El Juego de los Valores",
    page_icon="🎴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados para inyectar en la aplicación
custom_css = """
<style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #4B5563;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# =====================================================================
# BASE DE DATOS DE LOS 52 VALORES (51 + SUPERVALOR)
# =====================================================================
valores_db = {
    # 🔵 VALORES DEL SER (Intrapersonales)
    "Autenticidad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "💎",
        "descripcion": "Vivir alineado a tu verdad interior, expresando con honestidad quién eres sin máscaras ni pretensiones.",
        "imagen": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=400&q=80"
    },
    "Valentía": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🦁",
        "descripcion": "La fuerza del corazón para actuar firmemente ante el miedo, la incertidumbre o el dolor físico y moral.",
        "imagen": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=400&q=80"
    },
    "Humildad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🌾",
        "descripcion": "Reconocer tus límites, errores y aprendizajes constantes sin necesidad de imponer superioridad sobre otros.",
        "imagen": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=400&q=80"
    },
    "Coherencia": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🎯",
        "descripcion": "La sintonía perfecta entre lo que piensas, sientes, dices y finalmente haces en tu vida cotidiana.",
        "imagen": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=400&q=80"
    },
    "Sinceridad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🗣️",
        "descripcion": "Expresarte con la verdad libre de fingimientos, construyendo puentes transparentes con tu entorno.",
        "imagen": "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&w=400&q=80"
    },
    "Paz interior": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🌊",
        "descripcion": "Un estado de serenidad profunda y calma mental que se mantiene firme ante las tormentas del exterior.",
        "imagen": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=400&q=80"
    },
    "Libertad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🕊️",
        "descripcion": "La facultad de elegir conscientemente tus propias acciones, asumiendo con madurez su responsabilidad.",
        "imagen": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80"
    },
    "Disciplina": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "⏳",
        "descripcion": "El compromiso diario de sostener hábitos y acciones orientados a tus objetivos, incluso cuando falta motivación.",
        "imagen": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=400&q=80"
    },
    "Responsabilidad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🧭",
        "descripcion": "La capacidad de responder hábilmente por tus decisiones y asumir plenamente las consecuencias de tus actos.",
        "imagen": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=400&q=80"
    },
    "Gratitud": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🙏",
        "descripcion": "Apreciar conscientemente las bendiciones, aprendizajes y bellezas cotidianas que recibes del mundo.",
        "imagen": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&w=400&q=80"
    },
    "Integridad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🛡️",
        "descripcion": "Hacer lo correcto basándote en principios firmes, incluso cuando nadie te está observando.",
        "imagen": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=400&q=80"
    },
    "Serenidad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🍃",
        "descripcion": "Mantener una actitud imperturbable, templada y apacible para procesar los eventos de la vida.",
        "imagen": "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?auto=format&fit=crop&w=400&q=80"
    },
    "Optimismo": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "☀️",
        "descripcion": "Enfoque constructivo que busca oportunidades en los desafíos y confía en el porvenir positivo.",
        "imagen": "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?auto=format&fit=crop&w=400&q=80"
    },
    "Confianza en uno mismo": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "✨",
        "descripcion": "La creencia profunda en tus capacidades, intuición y valor para navegar las circunstancias del camino.",
        "imagen": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=400&q=80"
    },
    "Sabiduría": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🦉",
        "descripcion": "Integración del conocimiento y la experiencia de vida para tomar decisiones prudentes y justas.",
        "imagen": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=400&q=80"
    },
    "Creatividad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🎨",
        "descripcion": "El impulso de dar vida a nuevas ideas, soluciones alternativas y expresiones únicas de tu ser.",
        "imagen": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=400&q=80"
    },
    "Curiosidad": {
        "categoria": "SER (Intrapersonales)", "color": "#2563EB", "emoji": "🔍",
        "descripcion": "La apertura constante para descubrir, hacer preguntas y explorar activamente la riqueza del mundo.",
        "imagen": "https://images.unsplash.com/photo-1489710437720-ebb67ec84dd2?auto=format&fit=crop&w=400&q=80"
    },

    # 🟢 VALORES DE RELACIÓN (Interpersonales)
    "Empatía": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🤝",
        "descripcion": "Comprender y resonar con el mundo emocional de los demás desde un lugar de respeto mutuo.",
        "imagen": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=400&q=80"
    },
    "Amabilidad": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🌸",
        "descripcion": "Tratar a los demás y a ti mismo con dulzura, cortesía y genuino afecto.",
        "imagen": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=400&q=80"
    },
    "Compasión": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "❤️",
        "descripcion": "El deseo sincero de aliviar el sufrimiento de los otros y acompañarles en sus momentos de dificultad.",
        "imagen": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=400&q=80"
    },
    "Generosidad": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🎁",
        "descripcion": "Compartir tu tiempo, recursos y amor de manera altruista y desinteresada.",
        "imagen": "https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?auto=format&fit=crop&w=400&q=80"
    },
    "Escucha": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "👂",
        "descripcion": "Prestar atención plena con presencia total, intentando comprender antes de responder.",
        "imagen": "https://images.unsplash.com/photo-1484981138541-3d074aa97716?auto=format&fit=crop&w=400&q=80"
    },
    "Respeto": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "✊",
        "descripcion": "Reconocer y valorar la dignidad inherentemente sagrada de todas las personas y sus límites.",
        "imagen": "https://images.unsplash.com/photo-1521791136368-1a46827d03f0?auto=format&fit=crop&w=400&q=80"
    },
    "Aceptación": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "👐",
        "descripcion": "Dar la bienvenida a la realidad de las cosas y personas tal y como son, sin juzgar ni resistirse.",
        "imagen": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=400&q=80"
    },
    "Colaboración": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🐝",
        "descripcion": "Sumar talentos, fuerzas y corazones con otros para lograr objetivos compartidos de manera armónica.",
        "imagen": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=400&q=80"
    },
    "Lealtad": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🤝",
        "descripcion": "Fidelidad y apoyo incondicional a tus compromisos, principios y vínculos afectivos en el tiempo.",
        "imagen": "https://images.unsplash.com/photo-1516880711640-ef7db81be3e1?auto=format&fit=crop&w=400&q=80"
    },
    "Honestidad relacional": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "👁️",
        "descripcion": "Ser transparente sobre tus sentimientos, límites e intenciones en tus relaciones humanas.",
        "imagen": "https://images.unsplash.com/photo-1501386761578-eac5c94b800a?auto=format&fit=crop&w=400&q=80"
    },
    "Ternura": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🧸",
        "descripcion": "Expresión sutil de afecto y cuidado que abraza la vulnerabilidad del otro con calidez.",
        "imagen": "https://images.unsplash.com/photo-1471286174890-9c112ffca5b4?auto=format&fit=crop&w=400&q=80"
    },
    "Cuidado mutuo": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🏡",
        "descripcion": "La corresponsabilidad de velar por el bienestar integral de quienes nos rodean en comunidad.",
        "imagen": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=400&q=80"
    },
    "Compañerismo": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "⛺",
        "descripcion": "Caminar al lado del otro compartiendo alegrías, retos y ofreciendo respaldo genuino en la ruta.",
        "imagen": "https://images.unsplash.com/photo-1539635278303-d4002c07eae3?auto=format&fit=crop&w=400&q=80"
    },
    "Igualdad": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "⚖️",
        "descripcion": "Garantizar el mismo trato, valor, oportunidades y dignidad para todos, sin discriminación alguna.",
        "imagen": "https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?auto=format&fit=crop&w=400&q=80"
    },
    "Justicia": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🏛️",
        "descripcion": "Dar a cada quien lo que le corresponde según el derecho y la equidad, velando por la rectitud.",
        "imagen": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=400&q=80"
    },
    "Solidaridad": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "🌍",
        "descripcion": "La adhesión y apoyo desinteresado a causas difíciles ajenas, especialmente en crisis comunitarias.",
        "imagen": "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=400&q=80"
    },
    "Amor": {
        "categoria": "RELACIÓN (Interpersonales)", "color": "#10B981", "emoji": "💖",
        "descripcion": "La fuerza suprema de unión, apreciación y cuidado que busca la plenitud y felicidad del ser.",
        "imagen": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&w=400&q=80"
    },

    # 🟠 VALORES DE CONTRIBUCIÓN (Acción en el mundo)
    "Servicio": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🤲",
        "descripcion": "La disposición constante de ayudar y agregar valor a la vida de otros de forma activa.",
        "imagen": "https://images.unsplash.com/photo-1559027615-cd4487df1365?auto=format&fit=crop&w=400&q=80"
    },
    "Excelencia": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "⭐",
        "descripcion": "El compromiso con la mejora continua y la entrega de la mejor versión posible en lo que realizas.",
        "imagen": "https://images.unsplash.com/photo-1510074377623-8cf13fb86c08?auto=format&fit=crop&w=400&q=80"
    },
    "Perseverancia": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🏔️",
        "descripcion": "La constancia firme para continuar avanzando a pesar de las caídas o demoras en los resultados.",
        "imagen": "https://images.unsplash.com/photo-1519817650390-64a93db51149?auto=format&fit=crop&w=400&q=80"
    },
    "Eficacia": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🎯",
        "descripcion": "La capacidad de lograr los efectos y resultados deseados optimizando el uso de tus recursos.",
        "imagen": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=400&q=80"
    },
    "Aprendizaje": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "📚",
        "descripcion": "La apertura de integrar nuevos conocimientos, desaprender y nutrir tu intelecto continuamente.",
        "imagen": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=400&q=80"
    },
    "Innovación": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "💡",
        "descripcion": "Desafiar lo establecido para proponer soluciones ingeniosas, disruptivas y de alto valor.",
        "imagen": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=400&q=80"
    },
    "Liderazgo": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "📢",
        "descripcion": "Inspirar, guiar y empoderar a un group humano hacia la conquista de una visión colectiva y noble.",
        "imagen": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80"
    },
    "Aventura": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🧭",
        "descripcion": "El deseo de salir de la zona de confort para explorar nuevos caminos, ideas y experiencias vibrantes.",
        "imagen": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=400&q=80"
    },
    "Orden": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "📋",
        "descripcion": "Organización armónica del espacio mental y físico que facilita la claridad y la fluidez.",
        "imagen": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=400&q=80"
    },
    "Claridad": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "💎",
        "descripcion": "Tener la mente despejada y transparente sobre lo que es real, prioritario y de valor.",
        "imagen": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=400&q=80"
    },
    "Propósito": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🧭",
        "descripcion": "Vivir alineado con un sentido profundo del porqué existes y qué legado deseas dejar.",
        "imagen": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80"
    },
    "Compromiso": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "💍",
        "descripcion": "El pacto irrompible de sostener tu palabra e intenciones ante proyectos, personas y principios.",
        "imagen": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=400&q=80"
    },
    "Autonomía": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🚲",
        "descripcion": "Gobernarte por tus propias leyes, manteniendo independencia intelectual y toma de decisiones libres.",
        "imagen": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=400&q=80"
    },
    "Sostenibilidad": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🌱",
        "descripcion": "Actuar hoy preservando los recursos del planeta y el bienestar sistémico para las futuras generaciones.",
        "imagen": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=400&q=80"
    },
    "Equidad": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "⚖️",
        "descripcion": "Diseñar e implementar soluciones que atiendan las necesidades específicas de cada quien, equilibrando la balanza.",
        "imagen": "https://images.unsplash.com/photo-1489533119213-66a5cd877091?auto=format&fit=crop&w=400&q=80"
    },
    "Responsabilidad social": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🏢",
        "descripcion": "Reconocer y mitigar activamente el impacto de tus acciones sobre el tejido de la comunidad global.",
        "imagen": "https://images.unsplash.com/photo-1469571486040-0b3b11419913?auto=format&fit=crop&w=400&q=80"
    },
    "Contribución": {
        "categoria": "CONTRIBUCIÓN (Acción en el mundo)", "color": "#D97706", "emoji": "🧱",
        "descripcion": "Poner activamente tu grano de arena para co-crear un mundo más justo, saludable y armónico.",
        "imagen": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=400&q=80"
    }
}

super_valor_confianza = {
    "nombre": "CONFIANZA", "categoria": "SUPERVALOR", "color": "#8B5CF6", "emoji": "⭐",
    "descripcion": "Es el valor base que permite que todos los demás valores se expresen plenamente. No compite con los otros valores, sino que los sostiene, amplifica y reorganiza.",
    "imagen": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=400&q=80"
}

# =====================================================================
# INICIALIZACIÓN DE VARIABLES DE SESIÓN (STATE MACHINE)
# =====================================================================
if "fase" not in st.session_state:
    st.session_state.fase = 0
if "seleccionados_12" not in st.session_state:
    st.session_state.seleccionados_12 = []
if "seleccionados_5" not in st.session_state:
    st.session_state.seleccionados_5 = []
if "jerarquia" not in st.session_state:
    st.session_state.jerarquia = {1: None, 2: None, 3: None, 4: None, 5: None}
if "respuestas_reflexion" not in st.session_state:
    st.session_state.respuestas_reflexion = {"por_que": "", "cuando_vivo": "", "cuando_no": "", "confianza_impacto": ""}
if "variante_elegida" not in st.session_state:
    st.session_state.variante_elegida = "Juego Clásico"

# =====================================================================
# FUNCIONES AUXILIARES DE RENDERIZACIÓN
# =====================================================================
def html_card(nombre, emoji, categoria, color, descripcion, imagen_url, selected=False):
    borde_ancho = "4px" if selected else "1px"
    color_borde = color if selected else "#E5E7EB"
    sombra = "0 10px 15px -3px rgba(0, 0, 0, 0.1)" if selected else "0 4px 6px -1px rgba(0,0,0,0.05)"
    opacidad_bg = f"background-color: {color}10;" if selected else "background-color: #F8FAFC;"
    
    return f"""
    <div style="
        border: {borde_ancho} solid {color_borde};
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 12px;
        text-align: center;
        box-shadow: {sombra};
        height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        {opacidad_bg}
    ">
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 1.5rem;">{emoji}</span>
                <span style="font-size: 0.75rem; font-weight: bold; color: {color}; text-transform: uppercase; background-color: {color}15; padding: 2px 8px; border-radius: 9999px;">
                    {categoria}
                </span>
            </div>
            <h4 style="margin: 10px 0 5px 0; color: #1F2937; font-family: system-ui, sans-serif; font-weight: 700;">{nombre}</h4>
            <div style="width: 100%; height: 130px; border-radius: 8px; overflow: hidden; margin: 8px 0;">
                <img src="{imagen_url}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <p style="font-size: 0.85rem; color: #4B5563; line-height: 1.4; text-align: left; margin-top: 10px;">
                {descripcion}
            </p>
        </div>
    </div>
    """

# =====================================================================
# SIDEBAR / CONTROLES DE NAVEGACIÓN
# =====================================================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🎴 Menú del Juego</h2>", unsafe_allow_html=True)
    fases_nombres = ["Inicio", "1. Exploración", "2. Priorización", "3. Jerarquía", "4. Reflexión", "5. Integración"]
    st.progress(st.session_state.fase / 5.0)
    st.markdown(f"**Paso actual:** {fases_nombres[st.session_state.fase]}")
    st.markdown("---")
    
    st.session_state.variante_elegida = st.selectbox(
        "Variante Activa de Juego:",
        ["Juego Clásico", "El espejo del conflicto", "Valores aspiracionales", "Termómetro de valores", "Línea de vida"]
    )
    
    if st.button("🔄 Reiniciar Juego"):
        st.session_state.fase = 0
        st.session_state.seleccionados_12 = []
        st.session_state.seleccionados_5 = []
        st.session_state.jerarquia = {1: None, 2: None, 3: None, 4: None, 5: None}
        st.session_state.respuestas_reflexion = {"por_que": "", "cuando_vivo": "", "cuando_no": "", "confianza_impacto": ""}
        st.rerun()

# =====================================================================
# RUTA / PANTALLAS DE LAS FASES DEL JUEGO
# =====================================================================

# FASE 0: INICIO
if st.session_state.fase == 0:
    st.markdown("<h1 class='main-title'>✨ El Juego de los Valores</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Un viaje interactivo de priorización, autoexploración y toma de conciencia.</p>", unsafe_allow_html=True)
    
    col_izq, col_der = st.columns([1, 1])
    with col_izq:
        st.subheader("🎮 Bienvenidos a la Baraja de la Conciencia")
        st.write("Los valores no son simples conceptos; son los pilares desde donde tomamos decisiones.")
        if st.button("🚀 Comenzar dinámica", type="primary", use_container_width=True):
            st.session_state.fase = 1
            st.rerun()
    with col_der:
        st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=600&q=80")

# FASE 1: EXPLORACIÓN (Elegir 12)
elif st.session_state.fase == 1:
    st.markdown("<h1 class='main-title'>🔍 Fase 1: Exploración</h1>", unsafe_allow_html=True)
    cuenta = len(st.session_state.seleccionados_12)
    
    col_cont_1, col_cont_2 = st.columns([3, 1])
    with col_cont_1:
        st.info(f"💡 **Cartas seleccionadas:** {cuenta} de **12 requeridas**.")
    with col_cont_2:
        if cuenta == 12:
            if st.button("Siguiente fase ➔", type="primary", use_container_width=True):
                st.session_state.fase = 2
                st.rerun()
        else:
            st.button("Siguiente fase ➔", disabled=True, use_container_width=True)

    filtro = st.radio("Filtrar por:", ["Todos", "SER", "RELACIÓN", "CONTRIBUCIÓN"], horizontal=True)
    
    cols = st.columns(3)
    idx = 0
    for nombre, datos in valores_db.items():
        if filtro != "Todos" and filtro not in datos["categoria"]:
            continue
            
        with cols[idx % 3]:
            is_selected = nombre in st.session_state.seleccionados_12
            # Aquí inyectamos el HTML de manera correcta usando la bandera unsafe_allow_html
            st.markdown(html_card(nombre, datos["emoji"], datos["categoria"], datos["color"], datos["descripcion"], datos["imagen"], is_selected), unsafe_allow_html=True)
            
            check = st.checkbox("Seleccionar", key=f"chk_{nombre}", value=is_selected)
            if check and nombre not in st.session_state.seleccionados_12:
                if len(st.session_state.seleccionados_12) < 12:
                    st.session_state.seleccionados_12.append(nombre)
                    st.rerun()
            elif not check and nombre in st.session_state.seleccionados_12:
                st.session_state.seleccionados_12.remove(nombre)
                st.rerun()
        idx += 1

# FASE 2: PRIORIZACIÓN (Elegir 5 de las 12)
elif st.session_state.fase == 2:
    st.markdown("<h1 class='main-title'>🔽 Fase 2: Priorización</h1>", unsafe_allow_html=True)
    cuenta = len(st.session_state.seleccionados_5)
    
    col_cont_1, col_cont_2 = st.columns([3, 1])
    with col_cont_1:
        st.info(f"💡 **Cartas seleccionadas:** {cuenta} de **5 requeridas**.")
    with col_cont_2:
        if cuenta == 5:
            if st.button("Siguiente fase ➔", type="primary", use_container_width=True):
                st.session_state.fase = 3
                st.rerun()
        else:
            st.button("Siguiente fase ➔", disabled=True, use_container_width=True)

    cols = st.columns(3)
    for idx, nombre in enumerate(st.session_state.seleccionados_12):
        datos = valores_db[nombre]
        with cols[idx % 3]:
            is_selected = nombre in st.session_state.seleccionados_5
            st.markdown(html_card(nombre, datos["emoji"], datos["categoria"], datos["color"], datos["descripcion"], datos["imagen"], is_selected), unsafe_allow_html=True)
            
            check = st.checkbox("Conservar", key=f"keep_{nombre}", value=is_selected)
            if check and nombre not in st.session_state.seleccionados_5:
                if len(st.session_state.seleccionados_5) < 5:
                    st.session_state.seleccionados_5.append(nombre)
                    st.rerun()
            elif not check and nombre in st.session_state.seleccionados_5:
                st.session_state.seleccionados_5.remove(nombre)
                st.rerun()

# FASE 3: JERARQUIZACIÓN
elif st.session_state.fase == 3:
    st.markdown("<h1 class='main-title'>🏆 Fase 3: Jerarquización</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Asigna las posiciones:")
        for pos in range(1, 6):
            # Determinamos el índice por defecto si ya existía una selección previa
            opciones = ["-- Elegir --"] + st.session_state.seleccionados_5
            valor_actual = st.session_state.jerarquia.get(pos)
            def_idx = opciones.index(valor_actual) if valor_actual in opciones else 0
            
            sel = st.selectbox(f"Posición #{pos}", opciones, index=def_idx, key=f"pos_{pos}")
            if sel != "-- Elegir --":
                st.session_state.jerarquia[pos] = sel
            else:
                st.session_state.jerarquia[pos] = None

    with col2:
        st.subheader("Tu Orden actual:")
        valores_asignados = []
        for pos in range(1, 6):
            val = st.session_state.jerarquia.get(pos)
            valores_asignados.append(val)
            st.write(f"**#{pos}:** {val if val else '⏳ Pendiente...'}")
        
        st.markdown("---")
        
        # Validamos que se hayan completado las 5 posiciones sin dejar nulos y sin repetir valores
        valores_validos = [v for v in valores_asignados if v is not None]
        todos_asignados = len(valores_validos) == 5 and len(set(valores_validos)) == 5
        
        if todos_asignados:
            if st.button("Siguiente fase: Reflexión ➔", type="primary", use_container_width=True):
                st.session_state.fase = 4
                st.rerun()
        else:
            if len(set(valores_validos)) != len(valores_validos):
                st.warning("⚠️ Hay valores repetidos en la jerarquía. Elige un valor único para cada posición.")
            else:
                st.info("💡 Por favor, asigna un valor a las 5 posiciones para poder continuar.")

# FASE 4: REFLEXIÓN
elif st.session_state.fase == 4:
    st.markdown("<h1 class='main-title'>🧠 Fase 4: Reflexión</h1>", unsafe_allow_html=True)
    st.session_state.respuestas_reflexion["por_que"] = st.text_area("¿Por qué estos valores?")
    st.session_state.respuestas_reflexion["cuando_vivo"] = st.text_area("¿Cuándo los vives?")
    st.session_state.respuestas_reflexion["cuando_no"] = st.text_area("¿Cuándo no?")
    
    if st.button("Integrar con la Confianza ➔", type="primary"):
        st.session_state.fase = 5
        st.rerun()

# FASE 5: INTEGRACIÓN Y CIERRE
elif st.session_state.fase == 5:
    st.markdown("<h1 class='main-title'>⭐ Fase 5: Integración</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(html_card(super_valor_confianza["nombre"], super_valor_confianza["emoji"], super_valor_confianza["categoria"], super_valor_confianza["color"], super_valor_confianza["descripcion"], super_valor_confianza["imagen"], True), unsafe_allow_html=True)
    with c2:
        st.session_state.respuestas_reflexion["confianza_impacto"] = st.text_area("¿Cómo cambiaría tu vida si vivieras estos valores con plena confianza?")
        
        # Generar bitácora en texto plano
        reporte = f"Tu Top 5:\n1. {st.session_state.jerarquia[1]}\n2. {st.session_state.jerarquia[2]}\n3. {st.session_state.jerarquia[3]}\n4. {st.session_state.jerarquia[4]}\n5. {st.session_state.jerarquia[5]}\n"
        
        st.download_button("📥 Descargar Bitácora", data=reporte, file_name="bitacora.txt")
