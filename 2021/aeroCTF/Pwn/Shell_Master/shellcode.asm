section .text
    global _start

_start:
    pop ebx
    pop ebx
    pop ebx ; path as arg
    xor ecx, ecx ; O_RDONLY
    push 0x5 ; open syscall
    pop eax
    int 0x80

    push eax
    pop ebx ; fd
    push 0x3 ; read syscall
    pop eax
    push esp
    pop ecx
    push 0xff ; buf size
    pop edx
    int 0x80

    push 0x4 ; write syscall
    pop eax
    push 0x1 ; stdout
    pop ebx
    int 0x80

    push 0x1 ; exit syscall
    pop eax
    push 0x0 ; arg
    pop ebx
    int 0x80
