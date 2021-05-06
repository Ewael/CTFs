#define _GNU_SOURCE 
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char const *argv[]) {
    setresgid(getegid(), getegid(), getegid());
    system("head -c5 flag.txt");
    return 0;
}
