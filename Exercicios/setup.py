from cx_Freeze import setup, Executable

setup(
    name="Corte",
    version="1.0",
    description="Programa de Corte",
    executables=[
        Executable("Corte.py", icon="corte1.ico")
    ]
)
