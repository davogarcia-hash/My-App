import streamlit as st
import pandas as pd
import numpy as np

# IMPORTA TUS LIBRERÍAS
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

# -------------------------------
# CONFIGURACIÓN INICIAL
# -------------------------------
st.set_page_config(page_title="Proyecto Streamlit", layout="wide")

menu = st.sidebar.selectbox(
    "Menú",
    ["Home", "Caja", "Compra de productos", "Créditos", "Productos para venta"]
)

# LOGO EN SIDEBAR
st.sidebar.image("AGROICA.png", width=250)

# -------------------------------
# HOME
# -------------------------------
if menu == "Home":

    st.markdown("""
    <style>
    .banner {
        background: linear-gradient(90deg, #306998, #FFD43B);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtext {
        text-align: center;
        font-size: 18px;
        color: #444;
        margin-bottom: 20px;
    }
    </style>

    <div class="banner">
        🐍 Proyecto en Streamlit
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subtext">Python Fundamentals</div>', unsafe_allow_html=True)

    st.success("✅ Bienvenido a la aplicación interactiva")

    st.image("logo.png", width=150)

    st.write("**Nombre:** David Tipismana Garcia")
    st.write("**Año:** 2026")

    st.markdown("""
    ### 📌 Descripción
    Esta aplicación integra conceptos de Python como:
    - Estructuras de datos
    - Funciones
    - NumPy
    - DataFrames
    - Programación orientada a objetos

    ### 🚀 Tecnologías utilizadas
    - Python
    - Streamlit
    - NumPy
    - Pandas
    """)

# -------------------------------
# CAJA (ANTES EJERCICIO 1)
# -------------------------------
elif menu == "Caja":
    st.title("Flujo de Caja")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0)

    if st.button("Agregar movimiento"):
        st.session_state.movimientos.append({
            "concepto": concepto,
            "tipo": tipo,
            "valor": valor
        })
        st.success("✅ Movimiento agregado correctamente")

    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df)

        ingresos = df[df["tipo"] == "Ingreso"]["valor"].sum()
        gastos = df[df["tipo"] == "Gasto"]["valor"].sum()
        saldo = ingresos - gastos

        col1, col2, col3 = st.columns(3)
        col1.metric("Ingresos", ingresos)
        col2.metric("Gastos", gastos)
        col3.metric("Saldo", saldo)

        if saldo >= 0:
            st.success("💰 Flujo de caja a favor")
        else:
            st.error("⚠️ Flujo de caja en contra")

# -------------------------------
# COMPRA DE PRODUCTOS (ANTES EJERCICIO 2)
# -------------------------------
elif menu == "Compra de productos":
    st.title("Registro de Productos")

    productos = ["Abamex", "Abafín 1.8 EC", "Abasac Ultra", "Absolute 60 SC", "Acarstin L 600",
    "Affirm", "Aliette", "Ally XP", "Almighty", "Alphamax 10 CE", "Amistar Top", 
    "Antracol", "Arrivo", "Azote", "Bacillus Mi Perú", "Bacthur", "Banvel", 
    "Batavia 150 OD", "BC 1000", "Bellis", "Belt", "Bifentex", "Boveril", 
    "Broder", "Cantus", "Casumin", "Cerillo", "Cipermeta", "Clincher", 
    "Clortosip L 500", "Confidor", "Crecisac", "Cytex 400", "Daconil", 
    "Decis", "Desfan 100", "Dimetoxion", "Dipel", "DK-Gib", "DK-Zate", 
    "Dormex", "Driver", "Engeo", "Exalt", "Facet", "Fitaminas", "Folicur", 
    "Force 20 CS", "Furia", "Gesaprim", "Gib-Bex", "Gib-Liq", "Giber Plus", 
    "Goal 2 EC", "Gorrión 2X", "Gramoxone", "Haley", "Hussar", "Incipio", 
    "Karmex", "Kocide", "Kryptón", "Lannate 90", "Larvin 375 F", "Lorsban", 
    "Luna Tranquility", "Luxazim 500", "Mata Gusano 2.5", "Merivon", "Metafos 600", 
    "Microthiol Special", "Misil 600 SL", "Mospilan", "Movento", "N-Large Premier", 
    "Nativo", "Nemaless", "Nemata SC", "Nominee", "Oberon", "Orius", "Orvego", 
    "Palladium", "Panzer", "Polyram DF", "Pounce", "Precursor", "Probac BS", 
    "Proclaim", "Promalina", "Pyrinex", "Ridomil Gold", "Rival", "Root-One", 
    "Sanmite", "Score", "Serenade", "Sevin 80 PM", "Silanki", "Solt-Gib 4 SL", 
    "Switch", "Talonil 500", "Talstar", "Thodogibe", "Tordon", "Tracer", 
    "Trichonativa", "Trichosil 50 WP", "Triathlon BA", "Vulcano-DP", "Vydate L"]
    productos = sorted(productos)

    if "productos_registrados" not in st.session_state:
        st.session_state.productos_registrados = []

    nombre = st.selectbox("Nombre del producto", productos)
    categoria = st.selectbox("Categoría", ["Insecticida","Fungicida","Herbicida","Bioinsumo"])
    precio = st.number_input("Precio", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=0)
    unidad = st.selectbox("Unidad", ["Lt","Kg","Sacos","Cilindros","Tn"])

    if st.button("Agregar producto"):
        total = precio * cantidad

        st.session_state.productos_registrados.append([
            nombre, categoria, precio, cantidad, unidad, total
        ])

        st.success(f"✅ Producto {nombre} agregado")

    if st.session_state.productos_registrados:
        arr = np.array(st.session_state.productos_registrados)

        df = pd.DataFrame(arr, columns=[
            "Producto","Categoría","Precio","Cantidad","Unidad","Total"
        ])

        st.dataframe(df)

# -------------------------------
# CRÉDITOS (ANTES EJERCICIO 3)
# -------------------------------
elif menu == "Créditos":
    st.title("Cálculo de Préstamos")

    if "historial" not in st.session_state:
        st.session_state.historial = []

    p = st.number_input("Monto del préstamo", value=12000.0)
    t = st.number_input("Tasa anual (%)", value=5.0)
    meses = st.slider("Meses", 1, 60)

    if st.button("Calcular"):
        resultado = lf.calcular_cuota_prestamo_frances(p, t, meses)

        st.session_state.historial.append({
            "monto": p,
            "tasa": t,
            "meses": meses,
            "cuota": resultado["cuota_mensual"]
        })

        st.success("✅ Cálculo realizado")

    if st.session_state.historial:
        df = pd.DataFrame(st.session_state.historial)
        st.dataframe(df)

# -------------------------------
# PRODUCTOS PARA VENTA (ANTES EJERCICIO 4)
# -------------------------------
elif menu == "Productos para venta":
    st.title("CRUD de Productos")

    if "crud_productos" not in st.session_state:
        st.session_state.crud_productos = []

    nombre = st.text_input("Nombre")
    precio = st.number_input("Precio", min_value=0.0)
    stock = st.number_input("Stock", min_value=0)

    if st.button("Agregar"):
        st.session_state.crud_productos.append({
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        })
        st.success("✅ Producto agregado")

    if st.session_state.crud_productos:
        df = pd.DataFrame(st.session_state.crud_productos)
        st.dataframe(df)

        index_eliminar = st.number_input("Índice a eliminar", min_value=0, step=1)
        if st.button("Eliminar"):
            if index_eliminar < len(st.session_state.crud_productos):
                st.session_state.crud_productos.pop(index_eliminar)
                st.success("🗑️ Producto eliminado")

        index_actualizar = st.number_input("Índice a actualizar", min_value=0, step=1)

        nuevo_nombre = st.text_input("Nuevo nombre")
        nuevo_precio = st.number_input("Nuevo precio", min_value=0.0)
        nuevo_stock = st.number_input("Nuevo stock", min_value=0)

        if st.button("Actualizar"):
            if index_actualizar < len(st.session_state.crud_productos):
                st.session_state.crud_productos[index_actualizar] = {
                    "nombre": nuevo_nombre,
                    "precio": nuevo_precio,
                    "stock": nuevo_stock
                }
                st.success("🔄 Producto actualizado")