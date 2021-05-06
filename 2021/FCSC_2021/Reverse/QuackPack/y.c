#include <stdio.h>
#include <stdlib.h>

int check_pwd(char *input) {
    int n = 0;
    char *pcVar1;
    if (*input == '0') {
        n = 9;
    }
    else {
        if (*input == '1') {
            n = 0xffffffcb;
        }
        else {
            if (*input == '2') {
                n = 0xf;
            }
            else {
                if (*input == '3') {
                    n = 0xffffffd5;
                }
                else {
                    if (*input == '4') {
                        n = 0xffffffa3;
                    }
                    else {
                        if (*input == '5') {
                            n = 1;
                        }
                        else {
                            if (*input == '6') {
                                n = 0x39;
                            }
                            else {
                                if (*input == '7') {
                                    n = 0x32;
                                }
                                else {
                                    if (*input == '8') {
                                        n = 0x1d;
                                    }
                                    else {
                                        if (*input == '9') {
                                            n = 0xffffffaf;
                                        }
                                        else {
                                            if (*input == 'a') {
                                                n = 0x3b;
                                            }
                                            else {
                                                if (*input == 'b') {
                                                    n = 0x3d;
                                                }
                                                else {
                                                    if (*input == 'c') {
                                                        n = 0xb;
                                                    }
                                                    else {
                                                        if (*input == 'd') {
                                                            n = 0x17;
                                                        }
                                                        else {
                                                            if (*input == 'e') {
                                                                n = 0xc;
                                                            }
                                                            else {
                                                                if (*input == 'f') {
                                                                    n = 0x41;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 1;
    if (*pcVar1 == '0') {
        n = n - 0x3e;
    }
    else {
        if (*pcVar1 == '1') {
            n = n - 0x4c;
        }
        else {
            if (*pcVar1 == '2') {
                n = n ^ 0x28;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 0x46;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 0x52;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n - 0x10;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n ^ 0x45;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n + 0x17;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 0x1f;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n - 0x36;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n + 0x33;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0x49;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 99;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n + 0x3c;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n + 0x52;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n ^ 0x48;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 2;
    if (*pcVar1 == '0') {
        n = n + 0x61;
    }
    else {
        if (*pcVar1 == '1') {
            n = n + 0x16;
        }
        else {
            if (*pcVar1 == '2') {
                n = n ^ 10;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n + 0x2a;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 0x3d;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n - 0x2e;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n ^ 0x3b;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x23;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 0x28;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n ^ 0x40;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x3c;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n + 0xe;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 0x16;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x4a;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n + 0x17;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n - 0x34;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 3;
    if (*pcVar1 == '0') {
        n = n + 0xe;
    }
    else {
        if (*pcVar1 == '1') {
            n = n ^ 0x52;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0x48;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n + 0xd;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 0x59;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n ^ 0x43;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n - 0x4c;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x52;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 0x4b;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n - 0x4d;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x2e;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n ^ 0x46;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n - 0x4a;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x17;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n ^ 0x50;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n ^ 0x23;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 4;
    if (*pcVar1 == '0') {
        n = n + 0x4a;
    }
    else {
        if (*pcVar1 == '1') {
            n = n + 0x1e;
        }
        else {
            if (*pcVar1 == '2') {
                n = n - 0xb;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n + 0x23;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 99;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n + 0x12;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n ^ 0x35;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n - 0x14;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n - 0x2e;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n - 0xe;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n + 0x5a;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n ^ 5;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n - 0x17;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n + 0x3c;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0xf;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n - 0x48;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 5;
    if (*pcVar1 == '0') {
        n = n - 8;
    }
    else {
        if (*pcVar1 == '1') {
            n = n + 0x37;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0xf;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 0x17;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 0x3d;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n + 0x1d;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n + 0x2e;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x15;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 0x5e;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n ^ 0x62;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x38;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n + 0x32;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n ^ 8;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n - 3;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0x40;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n - 0x42;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 6;
    if (*pcVar1 == '0') {
        n = n ^ 0x40;
    }
    else {
        if (*pcVar1 == '1') {
            n = n ^ 0x5b;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0x43;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 0x18;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n - 0x37;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n - 8;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n - 0x46;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n + 0x62;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 0x58;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n + 0x36;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n - 0x21;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0x2b;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 0x18;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x3d;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0x5a;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n - 0x1b;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 7;
    if (*pcVar1 == '0') {
        n = n + 0xd;
    }
    else {
        if (*pcVar1 == '1') {
            n = n - 0x16;
        }
        else {
            if (*pcVar1 == '2') {
                n = n ^ 0x25;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n - 0x3a;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n ^ 0x2b;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n + 0xf;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n ^ 0x31;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n + 5;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n ^ 0xc;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n ^ 0x45;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x41;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0x12;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n ^ 0x24;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n - 0x4d;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n ^ 0x39;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n ^ 6;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 8;
    if (*pcVar1 == '0') {
        n = n + 0x49;
    }
    else {
        if (*pcVar1 == '1') {
            n = n ^ 0x2b;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0x39;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 7;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n - 0x5f;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n ^ 0x1b;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n + 0x50;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x2c;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 1;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n ^ 0x2d;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n - 0x36;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0x5f;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 0x28;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x39;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n + 0x2a;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n - 0x5f;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 9;
    if (*pcVar1 == '0') {
        n = n ^ 8;
    }
    else {
        if (*pcVar1 == '1') {
            n = n + 0x44;
        }
        else {
            if (*pcVar1 == '2') {
                n = n ^ 0x60;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 0x41;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n - 0x4f;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n ^ 3;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n + 0x43;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n - 0x30;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n + 0xf;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n - 0x2f;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x18;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n + 0x48;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n ^ 0x49;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n + 0x2a;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0x12;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n - 0x22;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 10;
    if (*pcVar1 == '0') {
        n = n ^ 0x55;
    }
    else {
        if (*pcVar1 == '1') {
            n = n ^ 0x30;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0x4b;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n - 0x52;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n - 0x1b;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n + 0x3b;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n - 3;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 99;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n ^ 0x57;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n - 0x3c;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x5f;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n ^ 0x55;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 3;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x2d;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n + 8;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n + 0x46;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 0xb;
    if (*pcVar1 == '0') {
        n = n + 0x2c;
    }
    else {
        if (*pcVar1 == '1') {
            n = n - 0x1e;
        }
        else {
            if (*pcVar1 == '2') {
                n = n - 0x39;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n + 0x5f;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n - 0x56;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n - 0x3b;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n + 0x10;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x1f;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n ^ 0x30;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n + 0x4b;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n + 0x35;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0xb;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n - 8;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x60;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n + 4;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n ^ 0x18;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 0xc;
    if (*pcVar1 == '0') {
        n = n - 0x27;
    }
    else {
        if (*pcVar1 == '1') {
            n = n + 0x60;
        }
        else {
            if (*pcVar1 == '2') {
                n = n ^ 0xd;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 0x43;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 0x18;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n - 0x39;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n - 0x56;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x34;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n - 0x5a;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n + 0x40;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n - 0x3e;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n + 0x30;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 0x2d;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n + 0x11;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n ^ 0x1f;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n ^ 0x45;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 0xd;
    if (*pcVar1 == '0') {
        n = n + 0x18;
    }
    else {
        if (*pcVar1 == '1') {
            n = n - 0x12;
        }
        else {
            if (*pcVar1 == '2') {
                n = n - 0x11;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n ^ 0x26;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n - 0xe;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n ^ 0x3d;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n - 0x5d;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 8;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n ^ 0x20;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n ^ 0x33;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n ^ 0x13;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0x36;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n - 6;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0xf;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0xe;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n + 0x20;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 0xe;
    if (*pcVar1 == '0') {
        n = n ^ 0x1f;
    }
    else {
        if (*pcVar1 == '1') {
            n = n + 0x19;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0x35;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n + 8;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n ^ 0xb;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n + 0x32;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n + 0x31;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n + 0x62;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n - 0x31;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n + 0x60;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n + 0x3d;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 0x36;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n + 0x62;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 1;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0x25;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n + 0x57;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    pcVar1 = input + 0xf;
    if (*pcVar1 == '0') {
        n = n - 0x23;
    }
    else {
        if (*pcVar1 == '1') {
            n = n ^ 0x11;
        }
        else {
            if (*pcVar1 == '2') {
                n = n + 0xc;
            }
            else {
                if (*pcVar1 == '3') {
                    n = n - 0xd;
                }
                else {
                    if (*pcVar1 == '4') {
                        n = n + 0x1a;
                    }
                    else {
                        if (*pcVar1 == '5') {
                            n = n + 0x5f;
                        }
                        else {
                            if (*pcVar1 == '6') {
                                n = n - 0x50;
                            }
                            else {
                                if (*pcVar1 == '7') {
                                    n = n ^ 0x5e;
                                }
                                else {
                                    if (*pcVar1 == '8') {
                                        n = n ^ 7;
                                    }
                                    else {
                                        if (*pcVar1 == '9') {
                                            n = n ^ 10;
                                        }
                                        else {
                                            if (*pcVar1 == 'a') {
                                                n = n + 0x11;
                                            }
                                            else {
                                                if (*pcVar1 == 'b') {
                                                    n = n - 99;
                                                }
                                                else {
                                                    if (*pcVar1 == 'c') {
                                                        n = n ^ 0x18;
                                                    }
                                                    else {
                                                        if (*pcVar1 == 'd') {
                                                            n = n ^ 0x3d;
                                                        }
                                                        else {
                                                            if (*pcVar1 == 'e') {
                                                                n = n - 0x53;
                                                            }
                                                            else {
                                                                if (*pcVar1 == 'f') {
                                                                    n = n + 0x44;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return n;
}

int main(int argc, char **argv)
{
    //char *pwd = "fc5ca1130bf5000";
    char *pwd = argv[1];
    int res = check_pwd(pwd);
    printf("pwd = %s\n", pwd);
    printf("res = 0x%x\n", res);
    if (res == 0x2b) {
        printf("success\n");
        return 0;
    }
    printf("fail\n");
    return 0;
}

// bu quackpack+0x95a1
// bu quackpack+0x959f
// bu quackpack+0x25000
// we want n == 0x2b
