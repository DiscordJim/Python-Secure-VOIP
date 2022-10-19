def integer_to_bytes(integer: int) -> bytes:
    return integer.to_bytes(2, byteorder='big')


def create_packet(opcode: bytes, message: str) -> bytes:
    return opcode + integer_to_bytes(len(message)) + message.encode()
