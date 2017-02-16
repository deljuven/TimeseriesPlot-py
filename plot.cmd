gnuplot << EOF
set terminal png
set offset 0.1,0.1,0.5,0.5
set output "D:\\Projects\\local\\out.png"
plot "D:\\Projects\\local\\count.out" using 1:2 with linespoints linecolor 3 linewidth 1 pointtype 5 pointsize 1, using 1:2:(int(\$1) % 5 == 0 ? sprintf("%.3f", \$2) : "")
quit
EOF