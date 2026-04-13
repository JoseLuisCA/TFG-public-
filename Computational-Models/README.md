# Computational Models

## Requisitos

- Python 3.11+ (recomendado 3.12 o 3.13)
- pip
- Graphviz del sistema (para visualizacion de automatas)

### Instalar Graphviz

- Windows: instala desde https://graphviz.org/download/ y marca la opcion de agregar a PATH.
- Linux (Debian/Ubuntu): `sudo apt install graphviz`
- macOS (Homebrew): `brew install graphviz`

## Ejecucion rapida (primera vez)

### Windows (PowerShell)

```powershell
cd Computational-Models
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python GUI/main.py
```

### Linux/macOS (bash/zsh)

```bash
cd Computational-Models
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python GUI/main.py
```

## Ejecuciones siguientes

- Windows:

```powershell
cd Computational-Models
.\.venv\Scripts\Activate.ps1
python GUI/main.py
```

- Linux/macOS:

```bash
cd Computational-Models
source .venv/bin/activate
python GUI/main.py
```

## Notas

- Si Graphviz no esta en PATH, las funciones que usan `graphviz` pueden fallar aunque el paquete de Python este instalado.
- No subas `.venv/` al repositorio; cada PC debe crear su propio entorno virtual.
