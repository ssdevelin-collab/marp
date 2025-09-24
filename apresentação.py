name: Gerar Slide Continental

on:
  workflow_dispatch:
  push:
    paths:
      - "apresentacao.py"
      - ".github/workflows/gera-slide.yml"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install python-pptx matplotlib

      - name: Executar script para gerar o slide
        run: python apresentacao.py

      - name: Upload do slide gerado
        uses: actions/upload-artifact@v4
        with:
          name: slide_continental
          path: apresentacao_conti.pptx
