import tkinter as tk
from tkinter import ttk, Entry, Canvas, filedialog
from PIL import Image, ImageTk
import qrcode

def generar_qr(direccion_web, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(direccion_web)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

def generar_qr_desde_entrada():
    direccion_web = entrada_direccion.get()
    if direccion_web:
        nombre_archivo = "qr_personalizado.png"
        generar_qr(direccion_web, nombre_archivo)
        mostrar_vista_preliminar(nombre_archivo)
        resultado.config(text=f"Se ha generado el código QR en el archivo: {nombre_archivo}")
    else:
        resultado.config(text="Por favor, ingrese una dirección web.")

def mostrar_vista_preliminar(nombre_archivo):
    img = Image.open(nombre_archivo)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk

def descargar_qr(nombre_archivo):
    destino = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png")])
    if destino:
        img = Image.open(nombre_archivo)
        img.save(destino)
        resultado.config(text=f"El código QR ha sido descargado en: {destino}")
    else:
        resultado.config(text="Descarga cancelada.")

# Función para abrir enlace en el navegador
def abrir_enlace(enlace):
    import webbrowser
    webbrowser.open(enlace)

# ventana principal
ventana = tk.Tk()
ventana.title("ULTRAHOST -Generador de Código QR- By IBZAN")
ventana.iconbitmap("C:\\Users\\zero\\Documents\\correos\\logo.ico")  # Reemplaza con la ruta de tu icono

# Tema
style = ttk.Style()
style.theme_use("clam")  # Puedes probar con otros temas como "winnative", "xpnative", "vista", etc.

# Etiqueta y entrada para la dirección web
etiqueta = ttk.Label(ventana, text="Ingrese la dirección web:")
etiqueta.pack(pady=10)

entrada_direccion = Entry(ventana, width=40)
entrada_direccion.pack(pady=10)

# Botón para generar el código QR y mostrar la vista preliminar
boton_generar_qr = ttk.Button(ventana, text="Generar QR", command=generar_qr_desde_entrada, style="TButton")
boton_generar_qr.pack(pady=10)

# Vista preliminar del código QR
canvas = Canvas(ventana, width=200, height=200)
canvas.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado = ttk.Label(ventana, text="")
resultado.pack(pady=10)

# Botón para descargar el código QR
boton_descargar_qr = ttk.Button(ventana, text="Descargar QR", command=lambda: descargar_qr("qr_personalizado.png"), style="TButton")
boton_descargar_qr.pack(pady=10)

# Línea divisoria
linea_divisoria = tk.Frame(ventana, height=1, width=400, bg="gray")
linea_divisoria.pack(fill="x", pady=10)

# Texto
texto_descripcion = "Diseño de aplicaciones - páginas y aplicativos web - servicio de hosting y dominio."
etiqueta_descripcion = ttk.Label(ventana, text=texto_descripcion, justify="center", wraplength=400)
etiqueta_descripcion.pack(pady=10)

# Botones PUBLICIDAD
boton_whatsapp = ttk.Button(ventana, text="WhatsApp", command=lambda: abrir_enlace("https://wa.me/447418353168"), style="TButton")
boton_whatsapp.pack(pady=10)

boton_web = ttk.Button(ventana, text="WEB", command=lambda: abrir_enlace("https://ultrahost.uk"), style="TButton")
boton_web.pack(pady=10)

# Estilo para botones
style.configure("TButton", padding=10, font=("Arial", 10), width=100)
style.map("TButton",
          foreground=[("active", "green"), ("disabled", "gray")],
          background=[("active", "!disabled", "white"), ("disabled", "white")])

# Iniciar el bucle de eventos
ventana.mainloop()
