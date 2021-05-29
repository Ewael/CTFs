#!/usr/bin/env python3

'''
ptrace(PTRACE_CONT, 15724, NULL, SIGRT_25) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGTTOU) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGQUIT) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGRT_29) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGCONT) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGPROF) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGRT_19) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGRT_31) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGSYS) = 0
ptrace(PTRACE_CONT, 15724, NULL, SIGTERM) = 0
ptrace(PTRACE_CONT, 15724, NULL, 0)     = 0
'''

signals = [25, 22, 3, 29, 18, 27, 19, 31, 31, 15]
f = ''.join(chr(a + 0x20) for a in L)
print(f)
