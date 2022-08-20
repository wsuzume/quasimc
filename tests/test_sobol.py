import numpy as np

from quasimc.sobol import i4_bit_hi1, i4_bit_lo0, i4_sobol

def test_i4_bit_hi1():

    # *****************************************************************************80
    #
    ## test_i4_bit_hi1() tests i4_bit_hi1().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    test_num = 10

    print("")
    print("test_i4_bit_hi1")
    print("  i4_bit_hi1 returns the location of the high 1 bit.")
    print("")
    print("       I  i4_bit_hi1(I)")
    print("")

    for test in range(0, test_num):
        i = np.random.randint(0, 101)
        j = i4_bit_hi1(i)
        print("  %8d  %8d" % (i, j))
    #
    #  Terminate.
    #
    print("")
    print("test_i4_bit_hi1")
    print("  Normal end of execution.")
    return

def test_i4_bit_lo0():

    # *****************************************************************************80
    #
    ## test_i4_bit_lo0() tests i4_bit_lo0().
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    test_num = 10

    print("")
    print("test_i4_bit_lo0")
    print("  i4_bit_lo0 returns the location of the low 0 bit.")
    print("")
    print("       I  i4_bit_lo0(I)")
    print("")

    for test in range(0, test_num):
        i = np.random.randint(0, 101)
        j = i4_bit_lo0(i)
        print("  %8d  %8d" % (i, j))
    #
    #  Terminate.
    #
    print("")
    print("test_i4_bit_lo0")
    print("  Normal end of execution.")
    return

def prime_ge(n):

    #*****************************************************************************80
    #
    ## prime_ge() returns the smallest prime greater than or equal to N.
    #
    #  Example:
    #
    #      N    prime_ge
    #
    #    -10     2
    #      1     2
    #      2     2
    #      3     3
    #      4     5
    #      5     5
    #      6     7
    #      7     7
    #      8    11
    #      9    11
    #     10    11
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #
    #  Input:
    #
    #    integer N, the number to be bounded.
    #
    #  Output:
    #
    #    integer P, the smallest prime number that is greater
    #    than or equal to N. 
    #
    p = max(np.ceil(n), 2)
    while (not is_prime(p)):
        p = p + 1

    return p

def is_prime(n):

    #*****************************************************************************80
    #
    ## is_prime() returns True if N is a prime number, False otherwise
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Corrado Chisari
    #
    #  Input:
    #
    #    integer N, the number to be checked.
    #
    #  Output:
    #
    #    boolean value, True or False
    #
    if ( n != int ( n ) or n < 1 ):
        return False
  
    p = 2
    while ( p < n ):
        if ( n % p == 0 ):
            return False
        p = p + 1

    return True

def test_sobol01():

    # *****************************************************************************80
    #
    ## test_sobol01() tests bitwise_xor().
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #
    print("")
    print("test_sobol01")
    print("  BITWISE_XOR returns the bitwise exclusive OR of two integers.")
    print("")
    print("     I     J     BITXOR(I,J)")
    print("")

    for test in range(0, 10):

        i = np.random.randint(0, 101)
        j = np.random.randint(0, 101)
        k = np.bitwise_xor(i, j)

        print("  %6d  %6d  %6d" % (i, j, k))

    return

def test_sobol02():

    # *****************************************************************************80
    #
    ## test_sobol02() tests i4_bit_hi1().
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #
    import numpy as np

    print("")
    print("test_sobol02")
    print("  i4_bit_hi1 returns the location of the high 1 bit.")
    print("")
    print("     I     i4_bit_hi1(I)")
    print("")

    for test in range(0, 10):
        i = np.random.randint(0, 101)
        j = i4_bit_hi1(i)
        print("%6d %6d" % (i, j))

    return


def test_sobol03():

    # *****************************************************************************80
    #
    ## test_sobol03() tests i4_bit_lo0().
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #
    import numpy as np

    print("")
    print("test_sobol03")
    print("  i4_bit_lo0 returns the location of the low 0 bit.")
    print("")
    print("     I     i4_bit_lo0(I)")
    print("")

    for test in range(0, 10):
        i = np.random.randint(0, 101)
        j = i4_bit_lo0(i)
        print("%6d %6d" % (i, j))

    return


def test_sobol04():

    # *****************************************************************************80
    #
    ## test_sobol04() tests i4_sobol().
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #
    print("")
    print("test_sobol04")
    print("  i4_sobol returns the next element")
    print("  of a Sobol sequence.")
    print("")
    print("In this test, we call i4_sobol repeatedly.")
    print("")

    dim_max = 4

    for dim_num in range(2, dim_max + 1):

        seed = 0
        qs = prime_ge(dim_num)

        print("\n  Using dimension DIM_NUM =   %d" % dim_num)
        print("\n  Seed  Seed   i4_sobol")
        print("  In    Out\n")

        for i in range(0, 111):
            [r, seed_out] = i4_sobol(dim_num, seed)
            if i <= 11 or 95 <= i:
                out = "%6d %6d  " % (seed, seed_out)
                for j in range(0, dim_num):
                    out += "%10f  " % r[j]
                print(out)
            elif i == 12:
                print("......................")
            seed = seed_out

    return


def test_sobol05():

    # *****************************************************************************80
    #
    ## test_sobol05() tests i4_sobol().
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    22 February 2011
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #
    print("")
    print("test_sobol05")
    print("  i4_sobol computes the next element of a Sobol sequence.")
    print("")
    print("  In this test, we demonstrate how the SEED can be")
    print("  manipulated to skip ahead in the sequence, or")
    print("  to come back to any part of the sequence.")
    print("")

    dim_num = 3

    print("")
    print("  Using dimension DIM_NUM =   %d\n" % dim_num)

    seed = 0

    print("")
    print("  Seed  Seed   i4_sobol")
    print("  In    Out")
    print("")

    for i in range(0, 10 + 1):
        [r, seed_out] = i4_sobol(dim_num, seed)
        out = "%6d %6d  " % (seed, seed_out)
        for j in range(1, dim_num + 1):
            out += "%10f  " % r[j - 1]
        print(out)
        seed = seed_out

    print("")
    print("  Jump ahead by increasing SEED:")
    print("")

    seed = 100

    print("")
    print("  Seed  Seed   i4_sobol")
    print("  In    Out")
    print("")

    for i in range(1, 6):
        [r, seed_out] = i4_sobol(dim_num, seed)
        out = "%6d %6d  " % (seed, seed_out)
        for j in range(1, dim_num + 1):
            out += "%10f  " % r[j - 1]
        print(out)
        seed = seed_out
    print("")
    print("  Jump back by decreasing SEED:")
    print("")

    seed = 3

    print("")
    print("  Seed  Seed   i4_sobol")
    print("  In    Out")
    print("")

    for i in range(0, 11):
        [r, seed_out] = i4_sobol(dim_num, seed)
        out = "%6d %6d  " % (seed, seed_out)
        for j in range(1, dim_num + 1):
            out += "%10f  " % r[j - 1]
        print(out)
        seed = seed_out

    print("")
    print("  Jump back by decreasing SEED:")
    print("")

    seed = 98

    print("")
    print("  Seed  Seed   i4_sobol")
    print("  In    Out")
    print("")

    for i in range(1, 6):
        [r, seed_out] = i4_sobol(dim_num, seed)
        out = "%6d %6d  " % (seed, seed_out)
        for j in range(1, dim_num + 1):
            out += "%10f  " % r[j - 1]
        print(out)
        seed = seed_out

    return


def test_sobol(argv=None):

    # *****************************************************************************80
    #
    ## test_sobol() tests sobol().
    #
    #  Licensing:
    #
    #    This code is distributed under the MIT license.
    #
    #  Modified:
    #
    #    25 October 2016
    #
    #  Author:
    #
    #    Original MATLAB version by John Burkardt.
    #    Python version by Corrado Chisari
    #

    print("")
    print("test_sobol")
    print("  Test sobol().")

    test_sobol01()
    test_sobol02()
    test_sobol03()
    test_sobol04()
    test_sobol05()
    #
    #  Terminate.
    #
    print("")
    print("test_sobol")
    print("  Normal end of execution.")
    
def timestamp():

    # *****************************************************************************80
    #
    ## timestamp() prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return


if __name__ == "__main__":
    timestamp()
    test_sobol()
    timestamp()
