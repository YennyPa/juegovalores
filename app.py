import streamlit as st
import random

# Configuración de la página para un diseño ancho y moderno
st.set_page_config(
    page_title="El Juego de los Valores",
    page_icon="🎴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para simular cartas reales e interactivas
st.markdown("""
<style>
    /* Estilos generales */
    .main {
        background-color: #0f172a;
    }
    
    /* Contenedor de la carta */
    .value-card {
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        height: 420px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        color: #ffffff;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s, box-shadow 0.2s;
        border: 2px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .value-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    /* Colores según categoría de carta */
    .card-ser {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); /* Azul */
        border-left: 6px solid #3b82f6;
    }
    .card-relacion {
        background: linear-gradient(135deg, #064e3b 0%, #0f172a 100%); /* Verde */
        border-left: 6px solid #10b981;
    }
    .card-contribucion {
        background: linear-gradient(135deg, #7c2d12 0%, #0f172a 100%); /* Naranja */
        border-left: 6px solid #f97316;
    }
    .card-confianza {
        background: linear-gradient(135deg, #581c87 0%, #0f172a 100%); /* Púrpura / Dorado */
        border: 3px solid #eab308;
    }
    
    /* Imagen de la carta */
    .card-image {
        width: 100%;
        height: 140px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 12px;
        opacity: 0.85;
    }
    
    /* Detalles de texto */
    .card-category {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #94a3b8;
        font-weight: 700;
        margin-bottom: 4px;
    }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 8px;
        color: #f8fafc;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .card-desc {
        font-size: 0.85rem;
        line-height: 1.4;
        color: #cbd5e1;
        overflow-y: auto;
        flex-grow: 1;
    }
    
    /* Insignia de selección */
    .selected-badge {
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: #ef4444;
        color: white;
        border-radius: 9999px;
        padding: 4px 10px;
        font-size: 0.7rem;
        font-weight: bold;
    }
    
    /* Títulos e instrucciones */
    .section-title {
        color: #f1f5f9;
        border-left: 4px solid #10b981;
        padding-left: 12px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS DE LOS 52 VALORES ---
# Cada valor cuenta con categoría, emoji, descripción reflexiva y una imagen conceptual de Unsplash
VALORES = {
    # 1. VALORES DEL SER (Intrapersonales) - Azul
    "Autenticidad": {
        "categoria": "SER",
        "icono": "👤",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Vivir y expresarse en total coherencia con tu verdad interior, sin usar máscaras para complacer las expectativas ajenas."
    },
    "Valentía": {
        "categoria": "SER",
        "icono": "🦁",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La fuerza del corazón para actuar a pesar del miedo, enfrentando la incertidumbre con determinación y templanza."
    },
    "Humildad": {
        "categoria": "SER",
        "icono": "🌱",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Reconocer con sencillez tus talentos y límites, manteniendo la mente siempre abierta para aprender de los demás."
    },
    "Coherencia": {
        "categoria": "SER",
        "icono": "⚖️",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La alineación armónica entre lo que piensas, lo que sientes, lo que dices y, fundamentalmente, lo que haces."
    },
    "Sinceridad": {
        "categoria": "SER",
        "icono": "💎",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Expresar la verdad con transparencia y sin dobleces, construyendo puentes libres de simulación o engaño."
    },
    "Paz interior": {
        "categoria": "SER",
        "icono": "🕊️",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1518241353330-0f7941c2d9b5?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Un estado de serenidad y quietud mental que permanece estable incluso en medio de las tormentas externas."
    },
    "Libertad": {
        "categoria": "SER",
        "icono": "🦅",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La capacidad de elegir conscientemente tu propio camino y asumir con total responsabilidad sus consecuencias."
    },
    "Disciplina": {
        "categoria": "SER",
        "icono": "🎯",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=300",
        "descripcion": "El compromiso diario con tus metas a largo plazo, haciendo lo necesario con constancia por encima de la motivación pasajera."
    },
    "Responsabilidad": {
        "categoria": "SER",
        "icono": "🗝️",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Responder conscientemente por tus actos, decisiones y sus efectos en ti mismo y en quienes te rodean."
    },
    "Gratitud": {
        "categoria": "SER",
        "icono": "🙏",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Apreciar activamente la abundancia del presente y reconocer el valor de cada experiencia y persona en tu vida."
    },
    "Integridad": {
        "categoria": "SER",
        "icono": "🛡️",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1473186578172-c141e6798cf4?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Hacer lo correcto basándote en principios éticos profundos, incluso cuando nadie te está observando."
    },
    "Serenidad": {
        "categoria": "SER",
        "icono": "🌊",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La quietud y calma que te permiten observar la realidad sin reaccionar de manera impulsiva o apresurada."
    },
    "Optimismo": {
        "categoria": "SER",
        "icono": "☀️",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Enfocar tu mirada en las soluciones y oportunidades del futuro, manteniendo una actitud positiva y constructiva."
    },
    "Confianza en uno mismo": {
        "categoria": "SER",
        "icono": "🕯️",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La seguridad interna de que posees los recursos necesarios para afrontar las dificultades y aprender de tus errores."
    },
    "Sabiduría": {
        "categoria": "SER",
        "icono": "🦉",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Integrar el conocimiento de las experiencias vividas para tomar decisiones sensatas y comprender profundamente la vida."
    },
    "Creatividad": {
        "categoria": "SER",
        "icono": "🎨",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La capacidad de conectar ideas de forma original para crear soluciones, belleza o nuevas perspectivas en el mundo."
    },
    "Curiosidad": {
        "categoria": "SER",
        "icono": "🔍",
        "color_class": "card-ser",
        "imagen": "https://images.unsplash.com/photo-1501504905252-473c47e087f8?auto=format&fit=crop&q=80&w=300",
        "descripcion": "El deseo constante y el asombro por explorar, comprender y aprender sobre el universo y el alma humana."
    },

    # 2. VALORES DE RELACIÓN (Interpersonales) - Verde
    "Empatía": {
        "categoria": "RELACIÓN",
        "icono": "🫂",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Sintonizar con el universo emocional del otro, comprendiendo su perspectiva sin emitir juicios."
    },
    "Amabilidad": {
        "categoria": "RELACIÓN",
        "icono": "🌸",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Tratar a los demás con calidez, cortesía y consideración genuina, haciendo más grato el andar compartido."
    },
    "Compasión": {
        "categoria": "RELACIÓN",
        "icono": "❤️‍🩹",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1469571486040-7a9b1373d702?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Percibir el sufrimiento ajeno acompañado del deseo profundo y la acción consciente para aliviarlo."
    },
    "Generosidad": {
        "categoria": "RELACIÓN",
        "icono": "🤲",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Compartir tus recursos, tiempo, atención y afecto con los demás de manera desinteresada y abundante."
    },
    "Escucha": {
        "categoria": "RELACIÓN",
        "icono": "👂",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Prestar atención plena y silenciosa al otro, buscando comprender antes de preparar una respuesta."
    },
    "Respeto": {
        "categoria": "RELACIÓN",
        "icono": "🤝",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1491438590914-bc09fcaaf77a?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Reconocer el valor intrínseco de cada persona, honrando sus diferencias, límites y dignidad."
    },
    "Aceptación": {
        "categoria": "RELACIÓN",
        "icono": "🍃",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Abrazar a las personas y circunstancias tal como son en el presente, renunciando a la necesidad de controlarlas."
    },
    "Colaboración": {
        "categoria": "RELACIÓN",
        "icono": "🐝",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Sumar talentos, voluntades y esfuerzos compartidos para alcanzar un bien u objetivo común."
    },
    "Lealtad": {
        "categoria": "RELACIÓN",
        "icono": "🐕",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Mantener firmes tus compromisos y apoyo hacia las personas y causas en las que crees, a lo largo del tiempo."
    },
    "Honestidad relacional": {
        "categoria": "RELACIÓN",
        "icono": "💬",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Comunicar tus límites, necesidades y sentimientos de manera asertiva, sincera y transparente."
    },
    "Ternura": {
        "categoria": "RELACIÓN",
        "icono": "🧸",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1515488042361-404e9250afef?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La expresión suave, afectuosa y protectora del cariño que suaviza las interacciones y cobija al otro."
    },
    "Cuidado mutuo": {
        "categoria": "RELACIÓN",
        "icono": "🏡",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1464863979621-258859e62245?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Proteger y nutrir recíprocamente el bienestar físico y emocional dentro de un vínculo o comunidad."
    },
    "Compañerismo": {
        "categoria": "RELACIÓN",
        "icono": "🏕️",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1501555088652-021faa106b9b?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Caminar al lado del otro brindando apoyo, complicidad y solidaridad constante en los proyectos compartidos."
    },
    "Igualdad": {
        "categoria": "RELACIÓN",
        "icono": "⚖️",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1489533119213-66a5cd877091?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Reconocer que todos los seres humanos poseen la misma dignidad y derechos, sin importar su condición."
    },
    "Justicia": {
        "categoria": "RELACIÓN",
        "icono": "🏛️",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Obrar y juzgar teniendo como guía la verdad y dando a cada quien lo que le corresponde por equidad."
    },
    "Solidaridad": {
        "categoria": "RELACIÓN",
        "icono": "🧣",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1544027993-37dbfe43562a?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Adherirse y prestar ayuda desinteresada a las causas o problemas de los demás, especialmente en la dificultad."
    },
    "Amor": {
        "categoria": "RELACIÓN",
        "icono": "❤️",
        "color_class": "card-relacion",
        "imagen": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La fuerza universal que nos une, cuida y expande, buscando siempre el florecimiento pleno de la vida."
    },

    # 3. VALORES DE CONTRIBUCIÓN (Acción en el mundo) - Naranja
    "Servicio": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🍵",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1469571486040-7a9b1373d702?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Disponer con alegría y de forma proactiva tus dones al cuidado, ayuda o facilitación de la vida de otros."
    },
    "Excelencia": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "💎",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=300",
        "descripcion": "El hábito de dar lo mejor de ti en cada tarea, buscando superarte a ti mismo con pasión y rigurosidad."
    },
    "Perseverancia": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🧗",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Mantener el esfuerzo constante a pesar de los obstáculos, la fatiga o las demoras en ver resultados."
    },
    "Eficacia": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "⚡",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La capacidad de lograr los efectos u objetivos deseados optimizando el uso de energía y recursos."
    },
    "Aprendizaje": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "📚",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La actitud constante de asimilar conocimientos y transformar las experiencias en sabiduría práctica."
    },
    "Innovación": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "💡",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Pensar fuera de la caja para introducir cambios novedosos que aporten un valor real al entorno."
    },
    "Liderazgo": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "📢",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Inspirar, guiar y facilitar el camino para que un grupo de personas despliegue su máximo potencial hacia un fin común."
    },
    "Aventura": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "⛺",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1501555088652-021faa106b9b?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Atreverse a explorar lo desconocido, asumiendo riesgos con emoción por el mero aprendizaje de descubrir."
    },
    "Orden": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🗂️",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Organizar tu mente, tus espacios y tus procesos para generar armonía, fluidez y claridad mental."
    },
    "Claridad": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "👓",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Definir tus intenciones con nitidez y comunicar tus metas de forma transparente, eliminando ruidos y dudas."
    },
    "Propósito": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🎯",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Tener una dirección clara e intencional en tus acciones, conectándolas con un sentido de trascendencia."
    },
    "Compromiso": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "💍",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1473186578172-c141e6798cf4?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Sostener tu palabra y tus decisiones a largo plazo, asumiendo el esfuerzo necesario por fidelidad al acuerdo."
    },
    "Autonomía": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🧭",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&q=80&w=300",
        "descripcion": "La libertad y capacidad de gobernarte a ti mismo basándote en tu propio criterio, libre de dependencias externas."
    },
    "Sostenibilidad": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🌍",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Satisfacer las necesidades presentes sin comprometer los recursos de las futuras generaciones, respetando la biosfera."
    },
    "Equidad": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "⚖️",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Dar a cada persona lo que necesita según sus condiciones particulares, reconociendo la diversidad humana."
    },
    "Responsabilidad social": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🏙️",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=300",
        "descripcion": "El compromiso consciente de aportar positivamente a la sociedad y mitigar el impacto negativo de nuestras acciones."
    },
    "Contribución": {
        "categoria": "CONTRIBUCIÓN",
        "icono": "🌳",
        "color_class": "card-contribucion",
        "imagen": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&q=80&w=300",
        "descripcion": "Ir más allá del beneficio propio para dejar un legado positivo y constructivo en el ecosistema social y ambiental."
    }
}

# Carta especial adicional
CONFIANZA_INFO = {
    "categoria": "SUPERVALOR",
    "icono": "⭐",
    "color_class": "card-confianza",
    "imagen": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80&w=300",
    "descripcion": "El cimiento que sostiene toda la baraja. La Confianza no compite con tus otros valores; es la fuerza que los sostiene, amplifica y reorganiza, eliminando el miedo para permitir su expresión plena."
}

# --- CONTROL DEL ESTADO DE LA APLICACIÓN (SESSION STATE) ---
if "step" not in st.session_state:
    st.session_state.step = "bienvenida"
if "seleccionadas_12" not in st.session_state:
    st.session_state.seleccionadas_12 = []
if "seleccionadas_5" not in st.session_state:
    st.session_state.seleccionadas_5 = []
if "ordenadas_5" not in st.session_state:
    st.session_state.ordenadas_5 = []
if "reflexion_respuestas" not in st.session_state:
    st.session_state.reflexion_respuestas = {
        "p1": "", "p2": "", "p3": "", "confianza_p1": "", "confianza_p2": "", "confianza_p3": ""
    }

# Función para renderizar la carta visualmente usando HTML y CSS
def render_value_card(name, info, selected=False, rank=None):
    badge_html = ""
    if rank:
        badge_html = f'<div class="selected-badge">Top {rank}</div>'
    elif selected:
        badge_html = '<div class="selected-badge">Seleccionada</div>'
        
    st.markdown(f"""
    <div class="value-card {info['color_class']}">
        {badge_html}
        <div>
            <span class="card-category">{info['categoria']}</span>
            <div class="card-title">{info['icono']} {name}</div>
        </div>
        <img src="{info['imagen']}" class="card-image" alt="{name}" />
        <div class="card-desc">{info['descripcion']}</div>
    </div>
    """, unsafe_allow_html=True)


# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🎴 Menú del Juego")
    
    # Progreso visual de los pasos
    st.write("### Tu Progreso")
    pasos = {
        "bienvenida": "🏠 Inicio & Instrucciones",
        "fase1": "🔍 1. Exploración (Elegir 12)",
        "fase2": "🎯 2. Priorización (Elegir 5)",
        "fase3": "📶 3. Jerarquización (Top 5)",
        "fase4": "🧠 4. Reflexión",
        "fase5": "⭐ 5. Supervalor Confianza",
        "final": "🏆 Tu Mapa de Valores"
    }
    
    for key, text in pasos.items():
        if st.session_state.step == key:
            st.info(f"👉 **{text}**")
        else:
            st.write(f"⚪ {text}")
            
    st.markdown("---")
    
    # Botón para resetear todo el juego
    if st.button("🔄 Reiniciar Juego Completo", use_container_width=True):
        st.session_state.step = "bienvenida"
        st.session_state.seleccionadas_12 = []
        st.session_state.seleccionadas_5 = []
        st.session_state.ordenadas_5 = []
        st.session_state.reflexion_respuestas = {
            "p1": "", "p2": "", "p3": "", "confianza_p1": "", "confianza_p2": "", "confianza_p3": ""
        }
        st.rerun()


# --- FLUJO DE DIAPOSITIVAS / PANTALLAS ---

# PANTALLA 1: BIENVENIDA E INSTRUCCIONES
if st.session_state.step == "bienvenida":
    st.title("✨ El Juego de los Valores")
    st.subheader("Un framework interactivo de autoconocimiento, priorización y decisiones conscientes.")
    
    st.markdown("""
    Este juego no busca darte respuestas correctas, sino encender un espejo de **autoconciencia** sobre tus prioridades vitales.
    A través de un proceso de decantación, pasarás de 51 naipes fundamentales a tus **5 valores innegociables**.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        ### 🎮 Cómo jugar (Modo Clásico):
        1. **Fase 1: Exploración (12 cartas)**: Examina las 51 cartas del Ser, Relación y Contribución. Elige las 12 que más vibren contigo hoy.
        2. **Fase 2: Priorización (5 cartas)**: Reduce drásticamente tu selección a únicamente 5 valores esenciales.
        3. **Fase 3: Jerarquización**: Ordena esas 5 cartas de mayor a menor prioridad en tu vida.
        4. **Fase 4: Reflexión**: Responde un breve cuestionario para anclar tus descubrimientos.
        5. **Fase 5: Supervalor**: Integra la carta especial **CONFIANZA** para transformar tu mirada.
        """)
        
        if st.button("🚀 Comenzar a Jugar", type="primary", use_container_width=True):
            st.session_state.step = "fase1"
            st.rerun()
            
    with col2:
        st.write("### Las 3 Familias de Valores")
        st.markdown("""
        * **🔵 Valores del SER (Intrapersonales)**: Definen tu conexión interior, tu regulación personal, sabiduría y carácter íntimo.
        * **🟢 Valores de RELACIÓN (Interpersonales)**: Rigen el cómo interactúas, empatizas, cuidas y te comunicas con los otros.
        * **🟠 Valores de CONTRIBUCIÓN (Acción en el mundo)**: Indican tu huella, tu energía productiva, tu excelencia y tu propósito activo.
        
        **⭐ CARTA 52 (CONFIANZA):** El supervalor base que sostiene toda tu estructura existencial.
        """)
        
        # Mostrar variantes
        with st.expander("🔄 Variantes de Juego (Haz clic para ver)"):
            st.markdown("""
            * **🪞 El espejo del conflicto**: Elige los valores que defiendes tú, y luego ponte en los zapatos del otro en un conflicto y adivina los suyos.
            * **🌱 Valores aspiracionales**: Selecciona valores que YA tienes frente a valores que quieres DESARROLLAR para ver la brecha de crecimiento.
            * **🌡️ Termómetro de valores**: Califícate del 1 al 10 en cuánto vives hoy cada valor seleccionado para diagnosticar incoherencias.
            """)


# PANTALLA 2: FASE 1 (EXPLORACIÓN - ELEGIR 12)
elif st.session_state.step == "fase1":
    st.title("🔍 Fase 1: Exploración")
    st.subheader("Elige exactamente 12 valores que te definan o resuenen con tu momento de vida actual.")
    
    cant_seleccionada = len(st.session_state.seleccionadas_12)
    st.progress(min(cant_seleccionada / 12, 1.0))
    st.write(f"### Cartas elegidas: `{cant_seleccionada} de 12`")
    
    # Validar avance
    if cant_seleccionada == 12:
        st.success("🎉 ¡Excelente! Tienes las 12 cartas ideales. Presiona el botón para ir a la Fase de Priorización.")
        if st.button("🎯 Continuar a Priorización (Elegir 5)", type="primary"):
            st.session_state.step = "fase2"
            st.rerun()
    elif cant_seleccionada > 12:
        st.error(f"Has seleccionado {cant_seleccionada} cartas. Por favor desmarca algunas hasta tener exactamente 12.")
    else:
        st.warning("Selecciona tus 12 cartas para poder avanzar.")

    st.markdown("---")
    
    # Filtro por categoría para facilitar la exploración
    categoria_filtro = st.radio(
        "Filtrar baraja por categoría:", 
        ["Mostrar Todos", "🔵 SER (Intrapersonales)", "🟢 RELACIÓN (Interpersonales)", "🟠 CONTRIBUCIÓN (Acción en el mundo)"],
        horizontal=True
    )
    
    # Grid de cartas
    cols = st.columns(4)
    col_idx = 0
    
    for name, info in VALORES.items():
        # Filtro de lógica
        if categoria_filtro == "🔵 SER (Intrapersonales)" and info["categoria"] != "SER":
            continue
        if categoria_filtro == "🟢 RELACIÓN (Interpersonales)" and info["categoria"] != "RELACIÓN":
            continue
        if categoria_filtro == "🟠 CONTRIBUCIÓN (Acción en el mundo)" and info["categoria"] != "CONTRIBUCIÓN":
            continue
            
        with cols[col_idx % 4]:
            is_selected = name in st.session_state.seleccionadas_12
            render_value_card(name, info, selected=is_selected)
            
            # Checkbox interactivo debajo de la carta
            select_box = st.checkbox(
                f"Seleccionar {name}", 
                value=is_selected, 
                key=f"f1_select_{name}",
                label_visibility="collapsed"
            )
            
            # Guardar en estado
            if select_box and name not in st.session_state.seleccionadas_12:
                st.session_state.seleccionadas_12.append(name)
                st.rerun()
            elif not select_box and name in st.session_state.seleccionadas_12:
                st.session_state.seleccionadas_12.remove(name)
                st.rerun()
                
        col_idx += 1


# PANTALLA 3: FASE 2 (PRIORIZACIÓN - ELEGIR 5 DE LAS 12)
elif st.session_state.step == "fase2":
    st.title("🎯 Fase 2: Priorización")
    st.subheader("Filtro Drástico. De tus 12 cartas elegidas, quédate solo con las 5 innegociables.")
    
    cant_seleccionada = len(st.session_state.seleccionadas_5)
    st.progress(min(cant_seleccionada / 5, 1.0))
    st.write(f"### Esenciales elegidos: `{cant_seleccionada} de 5`")
    
    if cant_seleccionada == 5:
        st.success("✨ ¡Perfecto! Has destilado tu esencia. Es hora de ordenarlas por jerarquía.")
        if st.button("📶 Continuar a Jerarquización", type="primary"):
            st.session_state.step = "fase3"
            # Inicializamos la jerarquía con el orden de selección inicial para evitar errores
            st.session_state.ordenadas_5 = list(st.session_state.seleccionadas_5)
            st.rerun()
    elif cant_seleccionada > 5:
        st.error(f"Has seleccionado {cant_seleccionada} cartas. Elige únicamente 5.")
    
    if st.button("⬅️ Volver a la Exploración (12 cartas)"):
        st.session_state.step = "fase1"
        st.rerun()
        
    st.markdown("---")
    
    # Mostramos únicamente las 12 que el usuario seleccionó previamente
    cols = st.columns(4)
    for idx, name in enumerate(st.session_state.seleccionadas_12):
        info = VALORES[name]
        with cols[idx % 4]:
            is_selected = name in st.session_state.seleccionadas_5
            render_value_card(name, info, selected=is_selected)
            
            select_box = st.checkbox(
                f"Priorizar {name}", 
                value=is_selected, 
                key=f"f2_select_{name}",
                label_visibility="collapsed"
            )
            
            if select_box and name not in st.session_state.seleccionadas_5:
                st.session_state.seleccionadas_5.append(name)
                st.rerun()
            elif not select_box and name in st.session_state.seleccionadas_5:
                st.session_state.seleccionadas_5.remove(name)
                st.rerun()


# PANTALLA 4: FASE 3 (JERARQUIZACIÓN - ORDENAR DEL 1 AL 5)
elif st.session_state.step == "fase3":
    st.title("📶 Fase 3: Jerarquización")
    st.subheader("Ordena tus 5 valores fundamentales. El puesto 1 representa tu faro absoluto.")
    
    st.markdown("""
    Selecciona la posición de cada carta usando los selectores a continuación. 
    **Asegúrate de no repetir posiciones** para que la jerarquía sea clara (del 1 al 5).
    """)
    
    # Creamos un sistema interactivo de reordenamiento
    nuevo_orden = [None] * 5
    posiciones_ocupadas = []
    
    col_cartas = st.columns(5)
    for idx, name in enumerate(st.session_state.seleccionadas_5):
        info = VALORES[name]
        with col_cartas[idx]:
            render_value_card(name, info)
            # Selector de prioridad
            opcion_rango = st.selectbox(
                f"Prioridad para {name}",
                options=[1, 2, 3, 4, 5],
                index=min(idx, 4),
                key=f"rank_select_{name}"
            )
            nuevo_orden[opcion_rango - 1] = name
            posiciones_ocupadas.append(opcion_rango)
            
    st.markdown("---")
    
    # Validar que no haya duplicados
    tiene_duplicados = len(set(posiciones_ocupadas)) != 5
    
    if tiene_duplicados:
        st.error("⚠️ Dos o más valores tienen asignado el mismo rango. Ajusta las opciones para que cada valor tenga un número del 1 al 5 único.")
    else:
        st.session_state.ordenadas_5 = nuevo_orden
        st.write("### Tu Jerarquía Actual:")
        ranking_texto = " ➔ ".join([f"**{i+1}. {name}**" for i, name in enumerate(nuevo_orden)])
        st.success(ranking_texto)
        
        col_nav = st.columns(2)
        with col_nav[0]:
            if st.button("⬅️ Ajustar Selección de 5"):
                st.session_state.step = "fase2"
                st.rerun()
        with col_nav[1]:
            if st.button("🧠 Ir a la Fase de Reflexión", type="primary", use_container_width=True):
                st.session_state.step = "fase4"
                st.rerun()


# PANTALLA 5: FASE 4 (REFLEXIÓN)
elif st.session_state.step == "fase4":
    st.title("🧠 Fase 4: Reflexión Intuitiva")
    st.subheader("Tómate un minuto para conectar la teoría con tu vida práctica.")
    
    # Mostrar el top 5 para tenerlo de referencia visual
    cols = st.columns(5)
    for idx, name in enumerate(st.session_state.ordenadas_5):
        with cols[idx]:
            render_value_card(name, VALORES[name], rank=idx+1)
            
    st.markdown("---")
    
    # Preguntas de autoindagación
    st.write("### Cuaderno de Indagación")
    
    st.session_state.reflexion_respuestas["p1"] = st.text_area(
        "1. ¿Por qué consideras que estos 5 valores son tus pilares fundamentales hoy?",
        value=st.session_state.reflexion_respuestas["p1"]
    )
    st.session_state.reflexion_respuestas["p2"] = st.text_area(
        "2. Identifica un momento específico de la última semana donde hayas vivido con total plenitud tu Valor #1.",
        value=st.session_state.reflexion_respuestas["p2"]
    )
    st.session_state.reflexion_respuestas["p3"] = st.text_area(
        "3. ¿En qué áreas de tu vida sientes que no estás honrando estos valores actualmente y qué lo está impidiendo?",
        value=st.session_state.reflexion_respuestas["p3"]
    )
    
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("⬅️ Volver a Jerarquizar"):
            st.session_state.step = "fase3"
            st.rerun()
    with col_nav[1]:
        if st.button("⭐ Revelar la Carta de la Confianza", type="primary", use_container_width=True):
            st.session_state.step = "fase5"
            st.rerun()


# PANTALLA 6: FASE 5 (INTEGRACIÓN CON LA CONFIANZA)
elif st.session_state.step == "fase5":
    st.title("⭐ Fase 5: Integración con la Confianza")
    st.subheader("La introducción de la Carta 52")
    
    col_carta, col_texto = st.columns([1, 2])
    with col_carta:
        render_value_card("CONFIANZA", CONFIANZA_INFO)
    with col_texto:
        st.markdown("""
        ### El Supervalor Raíz
        La **Confianza** no es solo un valor más de la baraja. Es el suelo, el oxígeno y el catalizador. Sin confianza, los valores del Ser se vuelven miedos disfrazados; los de Relación, apegos y los de Contribución, meras exigencias.
        
        #### Reflexiona con la Confianza:
        """)
        
        st.session_state.reflexion_respuestas["confianza_p1"] = st.text_area(
            "A. ¿Cómo cambiaría la expresión de tus 5 valores si los vivieras desde una confianza absoluta y libre de miedo?",
            value=st.session_state.reflexion_respuestas["confianza_p1"]
        )
        st.session_state.reflexion_respuestas["confianza_p2"] = st.text_area(
            "B. ¿Cuál de tus 5 valores seleccionados requiere hoy de mayor dosis de confianza para brillar?",
            value=st.session_state.reflexion_respuestas["confianza_p2"]
        )
        st.session_state.reflexion_respuestas["confianza_p3"] = st.text_area(
            "C. Si confías plenamente en el proceso de la vida, ¿reorganizarías la prioridad de tu top 5?",
            value=st.session_state.reflexion_respuestas["confianza_p3"]
        )
        
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("⬅️ Volver al Cuaderno de Reflexión"):
            st.session_state.step = "fase4"
            st.rerun()
    with col_nav[1]:
        if st.button("🏆 Generar Mi Mapa de Valores", type="primary", use_container_width=True):
            st.session_state.step = "final"
            st.rerun()


# PANTALLA 7: TABLERO FINAL DE RESULTADOS
elif st.session_state.step == "final":
    st.balloons()
    st.title("🏆 Tu Mapa de Valores Personales")
    st.subheader("Este es el reflejo de tu brújula de vida actual. Guárdalo, imprímelo o reflexiona en él.")
    
    # 1. Mostrar el Top 5 en columnas con un diseño destacado
    st.markdown("### 🎴 Tu Jerarquía de Vida Innegociable")
    cols = st.columns(5)
    for idx, name in enumerate(st.session_state.ordenadas_5):
        with cols[idx]:
            render_value_card(name, VALORES[name], rank=idx+1)
            
    st.markdown("---")
    
    # 2. Resumen de respuestas reflexivas en formato de vitrina
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.markdown("### 📝 Tus Reflexiones del Alma")
        st.markdown(f"**¿Por qué estos 5 valores?**\n*{st.session_state.reflexion_respuestas['p1']}*")
        st.markdown(f"**Ejemplo práctico vivido:**\n*{st.session_state.reflexion_respuestas['p2']}*")
        st.markdown(f"**Áreas a mejorar y bloqueos:**\n*{st.session_state.reflexion_respuestas['p3']}*")
        
    with col_der:
        st.markdown("### ⭐ La Luz de la Confianza")
        st.markdown(f"**Vivir con confianza absoluta:**\n*{st.session_state.reflexion_respuestas['confianza_p1']}*")
        st.markdown(f"**Valor que requiere más confianza:**\n*{st.session_state.reflexion_respuestas['confianza_p2']}*")
        st.markdown(f"**Cambio en el orden por confianza:**\n*{st.session_state.reflexion_respuestas['confianza_p3']}*")

    st.markdown("---")
    
    # 3. Herramienta de descarga en formato Texto Plano (.txt) para bitácora personal
    informe_txt = f"""==================================================
                 MI MAPA DE VALORES
==================================================
Fecha de Reflexión: 2026

JERARQUÍA COMPLETA (Top 5):
1. {st.session_state.ordenadas_5[0]}
2. {st.session_state.ordenadas_5[1]}
3. {st.session_state.ordenadas_5[2]}
4. {st.session_state.ordenadas_5[3]}
5. {st.session_state.ordenadas_5[4]}

--------------------------------------------------
CUADERNO DE INDAGACIÓN:
--------------------------------------------------
1. ¿Por qué estos pilares?
{st.session_state.reflexion_respuestas['p1']}

2. Momento de plenitud semanal:
{st.session_state.reflexion_respuestas['p2']}

3. Áreas no alineadas y obstáculos:
{st.session_state.reflexion_respuestas['p3']}

--------------------------------------------------
INTEGRACIÓN CON LA CONFIANZA:
--------------------------------------------------
A. Expresión libre de miedo:
{st.session_state.reflexion_respuestas['confianza_p1']}

B. Valor que requiere más confianza:
{st.session_state.reflexion_respuestas['confianza_p2']}

C. Ajuste de jerarquía por confianza:
{st.session_state.reflexion_respuestas['confianza_p3']}

==================================================
"Este juego no busca respuestas correctas, sino conciencia."
==================================================
"""
    
    st.download_button(
        label="📥 Descargar Mi Bitácora de Valores (TXT)",
        data=informe_txt,
        file_name="Mi_Mapa_de_Valores.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    if st.button("🔄 Jugar de Nuevo"):
        st.session_state.step = "bienvenida"
        st.session_state.seleccionadas_12 = []
        st.session_state.seleccionadas_5 = []
        st.session_state.ordenadas_5 = []
        st.session_state.reflexion_respuestas = {
            "p1": "", "p2": "", "p3": "", "confianza_p1": "", "confianza_p2": "", "confianza_p3": ""
        }
        st.rerun()
