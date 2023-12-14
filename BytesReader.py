import argparse

def ler_primeiros_bytes(arquivo, num_bytes):
    with open(arquivo, 'rb') as f:
        dados = f.read(num_bytes)
    return dados

def main():
    parser = argparse.ArgumentParser(description='Ler os primeiros bytes de um arquivo.')
    parser.add_argument('arquivo', help='Caminho para o arquivo a ser lido.')
    parser.add_argument('num_bytes', type=int, help='Número de bytes a serem lidos.')

    args = parser.parse_args()

    arquivo = args.arquivo
    num_bytes = args.num_bytes

    try:
        primeiros_bytes = ler_primeiros_bytes(arquivo, num_bytes)
        print(f'Primeiros {num_bytes} bytes do arquivo "{arquivo}": {primeiros_bytes}')
    except Exception as e:
        print(f'Erro ao ler os bytes do arquivo: {e}')

if __name__ == "__main__":
    main()