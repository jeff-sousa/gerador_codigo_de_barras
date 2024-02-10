from barcode import Code128 #importando a codificação 128
from barcode.writer import ImageWriter #para escrever a imagem



class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'{tag}'  # caminho de criação da imagem
        tag.save(path_from_tag)
        return path_from_tag
