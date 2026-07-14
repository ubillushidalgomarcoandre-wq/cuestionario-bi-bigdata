import streamlit as st

st.set_page_config(
    page_title="Cuestionario · BI & Big Data",
    page_icon="🧊",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Datos: 20 preguntas Unidad 3 + 20 preguntas Unidad 4
# ---------------------------------------------------------------------------
UNIDAD_3 = [
    {"q": "¿Qué es un cubo OLAP?",
     "opts": ["Una tabla plana de dos dimensiones",
              "Una estructura de datos multidimensional que permite analizar información desde múltiples perspectivas",
              "Un tipo de archivo de texto plano",
              "Un servidor físico de almacenamiento"], "correct": 1},
    {"q": "En un modelo multidimensional, una dimensión representa:",
     "opts": ["Un valor numérico a calcular, como las ventas totales",
              "Una perspectiva de análisis, como Tiempo, Producto o Región",
              "El servidor donde se aloja la base de datos",
              "Un algoritmo de minería de datos"], "correct": 1},
    {"q": "¿Cuál de los siguientes es un ejemplo correcto de jerarquía dentro de una dimensión?",
     "opts": ["Ventas → Costos → Utilidad",
              "Año → Trimestre → Mes → Día",
              "Cliente → Producto → Proveedor",
              "Servidor → Red → Internet"], "correct": 1},
    {"q": "¿Cuáles son características principales de un tablero de control (dashboard) en BI?",
     "opts": ["Almacenar datos sin procesar",
              "Presentar indicadores clave (KPIs) de forma visual para apoyar la toma de decisiones",
              "Reemplazar completamente las bases de datos transaccionales",
              "Ejecutar procesos de ingesta de datos"], "correct": 1},
    {"q": "Un KPI (Key Performance Indicator) se define como:",
     "opts": ["Un tipo de base de datos NoSQL",
              "Un indicador cuantificable que mide el desempeño de un objetivo o proceso clave del negocio",
              "Un lenguaje de programación para BI",
              "Un componente físico de almacenamiento"], "correct": 1},
    {"q": "En la gestión de proyectos de BI, ¿qué diferencia principal existe entre las metodologías ágiles y las tradicionales?",
     "opts": ["Las ágiles no permiten trabajar con datos",
              "Las tradicionales siguen un flujo secuencial y planificado, mientras que las ágiles trabajan con iteraciones cortas y entregas incrementales",
              "Las tradicionales solo se usan en Big Data",
              "No existen diferencias relevantes entre ambas"], "correct": 1},
    {"q": "¿Cuál de las siguientes es una herramienta tecnológica de apoyo a soluciones BI mencionada en la unidad?",
     "opts": ["Qlik Sense", "WordPress", "Photoshop", "AutoCAD"], "correct": 0},
    {"q": "¿Cuál de los siguientes es un modelo de minería de datos?",
     "opts": ["Clustering (agrupamiento)", "Firewall", "Data Lineage", "Dashboard"], "correct": 0},
    {"q": "¿Cuál de las siguientes se considera un factor crítico de éxito en la implementación de soluciones BI?",
     "opts": ["El compromiso de la alta dirección y una gestión adecuada del cambio organizacional",
              "Usar exclusivamente hojas de cálculo de Excel",
              "Evitar la capacitación de los usuarios finales",
              "Prescindir de un plan de proyecto"], "correct": 0},
    {"q": "¿Cuál es la principal diferencia entre las arquitecturas ROLAP y MOLAP?",
     "opts": ["ROLAP almacena los datos en bases de datos relacionales, mientras que MOLAP los almacena en estructuras multidimensionales propias",
              "MOLAP no permite realizar consultas analíticas",
              "ROLAP solo funciona con datos no estructurados",
              "No existe ninguna diferencia entre ambas"], "correct": 0},
    {"q": "¿Qué estrategia de almacenamiento multidimensional se utiliza para optimizar el rendimiento de las consultas analíticas en un cubo OLAP?",
     "opts": ["Indexación exclusiva en tablas planas",
              "Pre-agregación y particionamiento de datos según las dimensiones más consultadas",
              "Almacenamiento únicamente en memoria RAM sin persistencia",
              "Uso exclusivo de archivos de texto sin estructura"], "correct": 1},
    {"q": "¿Qué es un atributo dentro de una dimensión de un cubo OLAP?",
     "opts": ["Una medida numérica calculada, como el total de ventas",
              "Una característica descriptiva de un miembro de la dimensión, como el nombre de un producto o su categoría",
              "Un servidor de almacenamiento distribuido",
              "Un algoritmo de clasificación"], "correct": 1},
    {"q": "En Power BI, ¿qué elemento permite representar visualmente un KPI dentro de un dashboard?",
     "opts": ["Una consulta SQL sin formato",
              "Una visualización tipo tarjeta o indicador (KPI visual) que muestra el valor actual frente a una meta",
              "Un archivo CSV sin procesar",
              "Un script de PowerShell"], "correct": 1},
    {"q": "¿Qué aspecto se debe evaluar al analizar la usabilidad de un tablero de control?",
     "opts": ["La cantidad de servidores utilizados",
              "La facilidad con la que el usuario interpreta la información y toma decisiones a partir de ella",
              "El lenguaje de programación usado internamente",
              "El tamaño del archivo de la base de datos"], "correct": 1},
    {"q": "¿Cuál de las siguientes es una fase típica en la gestión de un proyecto de BI bajo un enfoque tradicional (en cascada)?",
     "opts": ["Sprint diario",
              "Planificación, análisis, diseño, implementación y control secuencial",
              "Retrospectiva semanal",
              "Kanban continuo sin fases definidas"], "correct": 1},
    {"q": "¿Qué ventaja ofrece un enfoque ágil frente a uno tradicional en un proyecto de BI?",
     "opts": ["Mayor rigidez en los requerimientos iniciales",
              "Mayor capacidad de adaptación a cambios y entregas incrementales de valor",
              "Eliminación total de la planificación",
              "Ausencia de retroalimentación del cliente"], "correct": 1},
    {"q": "¿Cuál de las siguientes herramientas se utiliza principalmente para la visualización de datos en soluciones BI?",
     "opts": ["Tableau", "Apache Kafka", "HDFS", "MySQL Workbench (exclusivamente administración)"], "correct": 0},
    {"q": "En minería de datos, ¿qué tipo de modelo se utiliza para predecir un valor numérico continuo, como el precio de una vivienda?",
     "opts": ["Clustering", "Regresión", "Reglas de asociación", "Clasificación binaria exclusivamente"], "correct": 1},
    {"q": "¿Qué técnica de minería de datos se utiliza para descubrir relaciones del tipo \"quienes compran el producto A también compran el producto B\"?",
     "opts": ["Reglas de asociación", "Regresión lineal", "Clustering jerárquico", "Análisis de series de tiempo"], "correct": 0},
    {"q": "¿Cuál de las siguientes es una buena práctica reconocida para garantizar la sostenibilidad de una iniciativa BI en una organización?",
     "opts": ["Concentrar todo el conocimiento en una sola persona sin documentación",
              "Establecer procesos de gobierno de datos y capacitación continua a los usuarios",
              "Evitar la actualización de los tableros de control",
              "No definir indicadores de éxito del proyecto"], "correct": 1},
]

UNIDAD_4 = [
    {"q": "Big Data se define principalmente como:",
     "opts": ["Un software de ofimática",
              "Conjuntos de datos de gran volumen, velocidad y variedad que superan la capacidad de las herramientas tradicionales de procesamiento",
              "Un tipo de red social",
              "Una base de datos relacional pequeña"], "correct": 1},
    {"q": "¿Cómo genera valor Big Data para las empresas?",
     "opts": ["Únicamente reduciendo el número de empleados",
              "Optimizando procesos, mejorando la toma de decisiones e identificando oportunidades de negocio",
              "Eliminando la necesidad de almacenamiento",
              "Sustituyendo por completo a los sistemas transaccionales"], "correct": 1},
    {"q": "¿Cuál de las siguientes NO es una de las \"4 V's\" de Big Data?",
     "opts": ["Volumen", "Velocidad", "Virtualización", "Veracidad"], "correct": 2},
    {"q": "¿Cuál de los siguientes es un ejemplo real de aplicación de Big Data?",
     "opts": ["Un sistema de recomendaciones de productos basado en el comportamiento de millones de usuarios",
              "Una hoja de cálculo con 50 filas",
              "Un documento de texto simple",
              "Una agenda telefónica personal"], "correct": 0},
    {"q": "La plataforma de Big Data se describe como:",
     "opts": ["Un único servidor físico",
              "La arquitectura que integra los componentes, funciones y el flujo de datos dentro del ecosistema analítico",
              "Un programa de diseño gráfico",
              "Una hoja de cálculo en la nube"], "correct": 1},
    {"q": "¿Cuál de los siguientes es un aspecto clave de una plataforma de Big Data?",
     "opts": ["La tolerancia a fallos y la escalabilidad",
              "El color de la interfaz gráfica",
              "El tamaño de la pantalla del usuario",
              "El idioma del sistema operativo"], "correct": 0},
    {"q": "La gobernanza de datos (Data Governance) en Big Data busca principalmente:",
     "opts": ["Aumentar la velocidad del procesador",
              "Garantizar la seguridad, calidad, trazabilidad y cumplimiento normativo de los datos",
              "Diseñar la interfaz de los dashboards",
              "Reemplazar a los analistas de datos"], "correct": 1},
    {"q": "Las dos modalidades principales de ingesta de datos son:",
     "opts": ["Pública y privada",
              "Batch (por lotes) y streaming (tiempo real)",
              "Local y remota",
              "Manual y automática únicamente"], "correct": 1},
    {"q": "A diferencia de un Data Warehouse, un Data Lake almacena:",
     "opts": ["Solo datos estructurados y procesados",
              "Datos en su formato original —estructurados, semiestructurados y no estructurados— sin esquema predefinido",
              "Únicamente reportes financieros",
              "Solo imágenes"], "correct": 1},
    {"q": "La capa de visualización dentro de una arquitectura Big Data tiene como función:",
     "opts": ["Capturar los datos desde las fuentes originales",
              "Presentar los resultados del análisis mediante dashboards y reportes gráficos",
              "Cifrar la información sensible",
              "Almacenar los datos sin procesar"], "correct": 1},
    {"q": "¿Cuál de las siguientes describe mejor la característica de \"Volumen\" dentro de las 4 V's de Big Data?",
     "opts": ["La velocidad con la que se generan y procesan los datos",
              "La cantidad masiva de datos generados constantemente por diversas fuentes",
              "La diversidad de formatos y tipos de datos",
              "La confiabilidad y exactitud de los datos"], "correct": 1},
    {"q": "¿Cuál de las siguientes describe mejor la característica de \"Variedad\" dentro de las 4 V's de Big Data?",
     "opts": ["La cantidad de datos almacenados",
              "La diversidad de formatos de datos: estructurados, semiestructurados y no estructurados",
              "La velocidad de procesamiento en tiempo real",
              "La exactitud de los datos capturados"], "correct": 1},
    {"q": "¿Cuál de las siguientes describe mejor la característica de \"Veracidad\" dentro de las 4 V's de Big Data?",
     "opts": ["El volumen total de datos almacenados",
              "La confiabilidad, calidad y precisión de los datos utilizados para el análisis",
              "La cantidad de servidores en el clúster",
              "La velocidad de generación de los datos"], "correct": 1},
    {"q": "En el contexto de Big Data generando valor para las empresas, ¿cuál es un ejemplo de optimización de procesos?",
     "opts": ["Ignorar los datos históricos de producción",
              "Usar el análisis predictivo para anticipar fallas en maquinaria y programar mantenimiento preventivo",
              "Eliminar los sistemas de monitoreo",
              "Reducir la cantidad de datos recolectados"], "correct": 1},
    {"q": "¿Qué se entiende por escalabilidad dentro de una plataforma de Big Data?",
     "opts": ["La capacidad de aumentar o disminuir los recursos de cómputo y almacenamiento según la demanda",
              "La cantidad de usuarios que pueden iniciar sesión simultáneamente en un dashboard",
              "El número de licencias de software adquiridas",
              "La velocidad del procesador de un solo servidor"], "correct": 0},
    {"q": "¿Qué significa tolerancia a fallos en una plataforma de Big Data?",
     "opts": ["La capacidad del sistema de seguir operando correctamente aunque falle alguno de sus componentes",
              "La eliminación completa de errores en el código fuente",
              "La reducción del volumen de datos almacenados",
              "La capacidad de ignorar errores de los usuarios"], "correct": 0},
    {"q": "Dentro de los componentes técnicos de Big Data, ¿qué función cumple la capa de procesamiento?",
     "opts": ["Capturar los datos desde las fuentes originales",
              "Transformar, limpiar y analizar los datos para generar información útil",
              "Presentar los resultados en dashboards",
              "Almacenar los datos sin ningún tipo de transformación"], "correct": 1},
    {"q": "¿Cuál de las siguientes es una fuente de datos no estructurada comúnmente utilizada en Big Data?",
     "opts": ["Una tabla de una base de datos relacional",
              "Publicaciones de texto e imágenes en redes sociales",
              "Un archivo CSV con columnas fijas",
              "Una hoja de cálculo de Excel con celdas tabulares"], "correct": 1},
    {"q": "¿Qué relación existe entre la gobernanza de datos y la calidad de los datos en un entorno Big Data?",
     "opts": ["No existe ninguna relación entre ambas",
              "La gobernanza de datos establece las políticas y procesos que garantizan que los datos mantengan altos niveles de calidad",
              "La calidad de datos reemplaza por completo a la gobernanza de datos",
              "La gobernanza de datos solo aplica a los datos estructurados"], "correct": 1},
    {"q": "¿Por qué es importante la seguridad de la información dentro de la gobernanza de Big Data?",
     "opts": ["Porque no afecta el cumplimiento normativo",
              "Porque protege los datos sensibles frente a accesos no autorizados, pérdidas o filtraciones",
              "Porque reduce la velocidad de procesamiento",
              "Porque elimina la necesidad de respaldos de información"], "correct": 1},
]

LETTERS = ["a", "b", "c", "d"]

# ---------------------------------------------------------------------------
# Estilos: fuentes, tema oscuro, hero con cubo isométrico animado (CSS puro)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

    html, body, [class*="css"] { color: #EBEFF7; font-family: 'IBM Plex Sans', sans-serif; }
    .stApp {
        background:
            radial-gradient(1200px 500px at 15% -10%, #16213a 0%, transparent 60%),
            radial-gradient(900px 500px at 100% 0%, #1a1730 0%, transparent 55%),
            #0B0F19;
    }
    header[data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 800px; padding-top: 4.2rem !important; padding-bottom: 4rem; }

    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; letter-spacing: -0.01em; }
    .stApp h1 { font-size: 2.4rem !important; font-weight: 700 !important; }

    .eyebrow {
        font-family: 'IBM Plex Mono', monospace; font-size: 12.5px; letter-spacing: .14em;
        text-transform: uppercase; color: #E8B24C; display:block; margin-bottom: 6px;
    }
    .subtitle { color: #8C95AC; font-size: 15.5px; line-height: 1.6; max-width: 480px; }

    /* ---- hero cube (puro CSS, sin JS) ---- */
    .cube-wrap { width:150px; height:150px; position:relative; perspective:600px; margin: 0 auto; }
    .cube {
        position:absolute; inset:0; margin:auto; width:92px; height:92px;
        transform-style:preserve-3d; transform:rotateX(-28deg) rotateY(-38deg);
        animation:spin 22s linear infinite;
    }
    @keyframes spin { to { transform:rotateX(-28deg) rotateY(322deg); } }
    .face { position:absolute; width:92px; height:92px; border:1px solid #3a4a72;
        background:linear-gradient(135deg,#16203a,#101830); }
    .face span { position:absolute; inset:0; background-image:
        linear-gradient(#26324f 1px, transparent 1px),
        linear-gradient(90deg, #26324f 1px, transparent 1px);
        background-size:23px 23px; opacity:.6; }
    .f-front{ transform: translateZ(46px); }
    .f-back{ transform: rotateY(180deg) translateZ(46px); }
    .f-right{ transform: rotateY(90deg) translateZ(46px); background:linear-gradient(135deg,#1a2542,#12192e); }
    .f-left{ transform: rotateY(-90deg) translateZ(46px); background:linear-gradient(135deg,#1a2542,#12192e); }
    .f-top{ transform: rotateX(90deg) translateZ(46px); background:linear-gradient(135deg,#1c2c46,#131c33); }
    .f-bottom{ transform: rotateX(-90deg) translateZ(46px); }

    /* ---- metrics ---- */
    div[data-testid="stMetric"] {
        background: #121A2B; border: 1px solid #26314A; border-radius: 12px; padding: 12px 16px;
    }
    div[data-testid="stMetricLabel"] {
        font-family: 'IBM Plex Mono', monospace !important; font-size: 11.5px !important;
        color: #8C95AC !important; text-transform: uppercase; letter-spacing: .06em;
    }
    div[data-testid="stMetricValue"] { font-family: 'Space Grotesk', sans-serif !important; }

    /* ---- section divider ---- */
    .divider-row { display:flex; align-items:center; gap:14px; margin: 40px 0 18px 0; }
    .divider-badge {
        font-family: 'IBM Plex Mono', monospace; font-size: 13px; font-weight: 600;
        padding: 3px 10px; border-radius: 6px; color: #0B0F19;
    }
    .divider-badge.u3 { background: #4FD1C5; }
    .divider-badge.u4 { background: #E8B24C; }
    .divider-title { font-size: 20px; font-weight: 600; font-family: 'Space Grotesk', sans-serif; }
    .divider-line { flex:1; height:1px; background: linear-gradient(90deg, #26314A, transparent); }

    /* ---- question card ---- */
    .qcard {
        background: #121A2B; border: 1px solid #26314A; border-left: 3px solid #4FD1C5;
        border-radius: 14px; padding: 20px 22px 6px 22px; margin-bottom: 16px;
    }
    .qcard.u4 { border-left-color: #E8B24C; }
    .qmeta {
        font-family: 'IBM Plex Mono', monospace; font-size: 11.5px; color: #8C95AC;
        text-transform: uppercase; letter-spacing: .06em;
    }
    .qtext { font-size: 16px; font-weight: 500; margin: 8px 0 12px 0; line-height: 1.5; }
    .answer-good {
        color: #34D399; font-family: 'IBM Plex Mono', monospace; font-size: 13px;
        margin: 4px 0 14px 0; padding-top: 10px; border-top: 1px dashed #26314A;
    }

    /* ---- radio options styled as cards ---- */
    div[data-testid="stRadio"] > div[role="radiogroup"] { gap: 8px; }
    div[data-testid="stRadio"] label {
        background: #17203570; border: 1px solid #26314A; border-radius: 9px;
        padding: 9px 12px !important; margin-bottom: 0 !important; transition: .15s ease;
    }
    div[data-testid="stRadio"] label:hover { border-color: #3a4665; }
    div[data-testid="stRadio"] label p { font-size: 14px !important; }

    div[data-testid="stAlert"] { border-radius: 10px; font-family: 'IBM Plex Sans', sans-serif; }

    footer, #MainMenu { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

hero_col1, hero_col2 = st.columns([2.3, 1], gap="large")
with hero_col1:
    st.markdown('<span class="eyebrow">40 preguntas · opción múltiple</span>', unsafe_allow_html=True)
    st.markdown("# Cubos, gobernanza y Big Data")
    st.markdown(
        '<p class="subtitle">Repaso combinado de la <b>Unidad 3</b> (cubos de información y '
        'minería de datos) y la <b>Unidad 4</b> (tecnología Big Data), 20 preguntas por unidad.</p>',
        unsafe_allow_html=True,
    )
with hero_col2:
    st.markdown(
        """
        <div class="cube-wrap">
          <div class="cube">
            <div class="face f-front"><span></span></div>
            <div class="face f-back"><span></span></div>
            <div class="face f-right"><span></span></div>
            <div class="face f-left"><span></span></div>
            <div class="face f-top"><span></span></div>
            <div class="face f-bottom"><span></span></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

modo_lectura = st.toggle("Modo lectura (mostrar todas las respuestas)", value=False)

if "answers" not in st.session_state:
    st.session_state.answers = {}

respondidas = len(st.session_state.answers)
correctas = sum(1 for v in st.session_state.answers.values() if v["correct"])

col1, col2 = st.columns(2)
col1.metric("Revisadas", f"{respondidas}/40")
col2.metric("Correctas", f"{correctas}/{respondidas}" if respondidas else "0/0")


def render_divider(badge_class, badge_text, title):
    st.markdown(
        f'<div class="divider-row">'
        f'<span class="divider-badge {badge_class}">{badge_text}</span>'
        f'<span class="divider-title">{title}</span>'
        f'<span class="divider-line"></span>'
        f"</div>",
        unsafe_allow_html=True,
    )


def render_question(idx, item, unidad_class, unidad_label):
    key = f"{unidad_label}_{idx}"
    st.markdown(f'<div class="qcard {unidad_class}">', unsafe_allow_html=True)
    st.markdown(f'<span class="qmeta">Pregunta {idx:02d} · {unidad_label}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="qtext">{item["q"]}</div>', unsafe_allow_html=True)

    labels = [f"{LETTERS[i]}) {opt}" for i, opt in enumerate(item["opts"])]

    if modo_lectura:
        st.radio(
            "Opciones", labels, index=item["correct"], key=f"ro_{key}",
            disabled=True, label_visibility="collapsed",
        )
        st.markdown(
            f'<div class="answer-good">✓ Respuesta correcta: {labels[item["correct"]]}</div>',
            unsafe_allow_html=True,
        )
    else:
        already = key in st.session_state.answers
        choice = st.radio(
            "Opciones", labels, index=None, key=f"q_{key}",
            disabled=already, label_visibility="collapsed",
        )
        if choice is not None and not already:
            chosen_idx = labels.index(choice)
            st.session_state.answers[key] = {"correct": chosen_idx == item["correct"]}
            st.rerun()
        if already:
            if st.session_state.answers[key]["correct"]:
                st.success(f"✓ Correcto — {labels[item['correct']]}")
            else:
                st.error(f"✗ Incorrecto. Respuesta correcta: {labels[item['correct']]}")
        st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


render_divider("u3", "U3", "Cubos de información y minería de datos")
for i, item in enumerate(UNIDAD_3, start=1):
    render_question(i, item, "u3", "Unidad 3")

render_divider("u4", "U4", "Tecnología Big Data")
for i, item in enumerate(UNIDAD_4, start=1):
    render_question(i + 20, item, "u4", "Unidad 4")

st.markdown(
    '<p style="text-align:center; color:#8C95AC; font-family:\'IBM Plex Mono\',monospace; '
    'font-size:12px; margin-top:40px;">Universidad de Guayaquil · Material de repaso — Unidad 3 y Unidad 4</p>',
    unsafe_allow_html=True,
)
