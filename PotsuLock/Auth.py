import hashlib

def gerar_senha(nome_usuario):
    usuario_bytes = nome_usuario.encode('utf-8')
    hash_sha256 = hashlib.sha256(usuario_bytes).hexdigest()
    return hash_sha256[:16]