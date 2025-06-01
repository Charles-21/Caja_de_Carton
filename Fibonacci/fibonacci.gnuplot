set title "Fibonacci"
set xlabel "n-esimo termino"
set ylabel "valor de Fibonacci"
set grid
set style data linespoints

plot "fibonacci.txt" using 1:2 title "Fibonacci" lt rgb "blue" 

pause -1 "Presiona enter para salir, hdlv"
