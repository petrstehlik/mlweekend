set terminal svg enhanced font "arial,13" size 25000,7000
set output 'res_20k.svg'
set style textbox transparent margins  1.0,  1.0 border
set xtics -10000 ,100
set xlabel "x"
set ylabel "y"
set grid ytics, xtics
set key bottom left
f(x) = 1.00000000*x**4 + -4.99999801*x**2 + 4.97825167*x**1 + -5.09104155
plot f(x) t "Approximated Function", 'data_20k.dat' t "Measured Points" smooth cspline
