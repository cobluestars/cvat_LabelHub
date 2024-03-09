from cx_Freeze import setup, Executable

setup(
    name="cvat_LabelHub",
    version="1.0.0",
    description="Labeling Tool",
    executables=[Executable("cvat_LabelHub.py")]
)