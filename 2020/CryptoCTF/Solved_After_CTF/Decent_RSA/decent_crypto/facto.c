#include <stdlib.h>
#include <stdio.h>
#include <gmp.h>

void fermat_factor(mpz_t p, mpz_t q, mpz_t N);

int main()
{
    mpz_t N;
    mpz_t p, q;

    mpz_init(N);
    mpz_init(p);
    mpz_init(q);

    gmp_printf("[+] Working...");

    // change N here
    char *n = "31973912565930840183966476557514486967105734963490863850242883813184363077890247373353346311197244652164393947531225033913089540524508960337859521594971267299801046318823852855678220562983993746120365799161402319433119943409550637861054248792884967164024537194083317326043002215575735008275047537805378975239548031416843476640326890142850615245392184058602194672466707234505010060517043706542794833490218200030153606086208410372554126103395033388764862282497594446045727336858065181330686078548554317618028148145081341511574658757428258020937703703371498976906228288914164074403171127516885244682134581893201619939353";
    mpz_set_str(N, n, 10);
    fermat_factor(p, q, N);

    gmp_printf("[+] p = %Zd\n", p);
    gmp_printf("[+] q = %Zd\n", q);

    mpz_clear(p);
    mpz_clear(q);
    mpz_clear(N);

    return 0;
}

void fermat_factor(mpz_t p, mpz_t q, mpz_t N)
{
    mpz_t a, b;

    mpz_init(a);
    mpz_init(b);

    mpz_sub_ui(a, N, 1);
    mpz_sqrt(a, a);
    mpz_add_ui(a, a, 1);

    while (1)
    {
        mpz_mul(b, a, a);
        mpz_sub(b, b, N);

        if (mpz_perfect_square_p(b))
            break;

        mpz_add_ui(a, a, 1);
    }

    mpz_sqrt(p, b);
    mpz_sqrt(q, b);
    mpz_add(p, a, p);
    mpz_sub(q, a, q);

    mpz_clear(a);
    mpz_clear(b);
}
