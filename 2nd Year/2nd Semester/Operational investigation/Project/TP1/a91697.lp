/* Objective function */
// xij -> emparelhamento. = caso n�o seja escolhido. 1 Caso seja.
min: 3 x01 + 4.24 x02 + 6.32 x03 + 8.25 x04 + 5.66 x05 + 6 x06 + 10 x07 + 10 x09 + 10.20 x0_10 + 11.18 x0_11 + 12.81 x0_12 + 7.21 x0_13 + 14.42 x0_14
   + 3 x12 + 6.08 x13 + 8.06 x14 + 4.12 x15 + 3 x16 + 8.54 x17 + 7 x19 + 7.28 x1_10 + 8.60 x1_11 + 10.63 x1_12 + 5 x1_13 + 12.04 x1_14
   + 3.16 x23 + 5.10 x24 + 1.41 x25 + 4.24 x26 + 5.83 x27 + 7.62 x29 + 7.07 x2_10 + 7.28 x2_11 + 8.60 x2_12 + 3.16 x2_13 + 10.30 x2_14
   + 2 x34 + 2.83 x35 + 7.21 x36 + 4.47 x37 + 10 x39 + 8.94 x3_10 + 8.06 x3_11 + 8.25 x3_12 + 4.47 x3_13 + 10.20 x3_14
   + 4.47 x45 + 8.94 x46 + 4 x47 + 11.31 x49 + 10 x4_10 + 8.54 x4_11 + 8 x4_12 + 5.66 x4_13 + 10 x4_14
   + 4.47 x56 + 4.47 x57 + 7.21 x59 + 6.32 x5_10 + 6.08 x5_11 + 7.21 x5_12 + 2 x5_13 + 8.94 x5_14
   + 8 x67 +  4 x69 + 4.47 x6_10 + 6.40 x6_11 + 8.94 x6_12 + 4 x6_13 + 10 x6_14
   + 8.94 x79 + 7.21 x7_10 + 5 x7_11 + 4 x7_12 + 4 x7_13 + 6 x7_14
   + 2 x9_10 + 5 x9_11 + 8 x9_12 + 5.66 x9_13 + 8.25 x9_14
   + 3 x10_11 + 6 x10_12 + 4.47 x10_13 + 6.32 x10_14
   + 3 x11_12 + 4.12 x11_13 + 3.61 x11_14
   + 5.66 x12_13 + 2 x12_14
   + 7.21 x13_14 ;

/* Variable bounds */
/*Garantir que os emparelhamentos s�o v�lidos*/

Vertice0: x01 + x02 + x03 + x04 + x05 + x06 + x07 + x09 + x0_10 + x0_11 + x0_12 + x0_13 + x0_14 = 1 ;
Vertice1: x01 + x12 + x13 + x14 + x15 + x16 + x17 + x19 + x1_10 + x1_11 + x1_12 + x1_13 + x1_14 = 1 ;
Vertice2: x02 + x12 + x23 + x24 + x25 + x26 + x27 + x29 + x2_10 + x2_11 + x2_12 + x2_13 + x2_14 = 1 ;
Vertice3: x03 + x13 + x23 + x34 + x35 + x36 + x37 + x39 + x3_10 + x3_11 + x3_12 + x3_13 + x3_14 = 1 ;
Vertice4: x04 + x14 + x24 + x34 + x45 + x46 + x47 + x49 + x4_10 + x4_11 + x4_12 + x4_13 + x4_14 = 1 ;
Vertice5: x05 + x15 + x25 + x35 + x45 + x56 + x57 + x59 + x5_10 + x5_11 + x5_12 + x5_13 + x5_14 = 1 ;
Vertice6: x06 + x16 + x26 + x36 + x46 + x56 + x67 + x69 + x6_10 + x6_11 + x6_12 + x6_13 + x6_14 = 1 ;
Vertice7: x07 + x17 + x27 + x37 + x47 + x57 + x67 + x79 + x7_10 + x7_11 + x7_12 + x7_13 + x7_14 = 1 ;
Vertice9: x09 + x19 + x29 + x39 + x49 + x59 + x69 + x79 + x9_10 + x9_11 + x9_12 + x9_13 + x9_14 = 1 ;
Vertice10: x0_10 + x1_10 + x2_10 + x3_10 + x4_10 + x5_10 + x6_10 + x7_10 + x9_10 + x10_11 + x10_12 + x10_13 + x10_14 = 1 ;
Vertice11: x0_11 + x1_11 + x2_11 + x3_11 + x4_11 + x5_11 + x6_11 + x7_11 + x9_11 + x10_11 + x11_12 + x11_13 + x11_14 = 1 ;
Vertice12: x0_12 + x1_12 + x2_12 + x3_12 + x4_12 + x5_12 + x6_12 + x7_12 + x9_12 + x10_12 + x11_12 + x12_13 + x12_14 = 1 ;
Vertice13: x0_13 + x1_13 + x2_13 + x3_13 + x4_13 + x5_13 + x6_13 + x7_13 + x9_13 + x10_13 + x11_13 + x12_13 + x13_14 = 1 ;
Vertice14: x0_14 + x1_14 + x2_14 + x3_14 + x4_14 + x5_14 + x6_14 + x7_14 + x9_14 + x10_14 + x11_14 + x12_14 + x13_14 = 1 ;

bin x01, x02 , x03 , x04 , x05 , x06 , x07 , x09 , x0_10 , x0_11 , x0_12 , x0_13 , x0_14 ;
bin x12 , x13 , x14 , x15 , x16 , x17 , x19 , x1_10 , x1_11 , x1_12 , x1_13, x1_14 ;
bin x23 , x24 , x25 , x26 , x27 , x29 , x2_10 , x2_11 , x2_12 , x2_13, x2_14 ;
bin x34 , x35 , x36 , x37 , x39 , x3_10 , x3_11 , x3_12 , x3_13, x3_14 ;
bin x45 , x46 , x47 , x49 , x4_10 , x4_11 , x4_12 , x4_13, x4_14 ;
bin x56 , x57 , x59 , x5_10 , x5_11 , x5_12 , x5_13, x5_14 ;
bin x67 , x69 , x6_10 , x6_11 , x6_12 , x6_13, x6_14 ;
bin x79 , x7_10 , x7_11 , x7_12 , x7_13, x7_14 ;
bin x9_10 , x9_11 , x9_12 , x9_13, x9_14 ;
bin x10_11 , x10_12 , x10_13, x10_14 ;
bin x11_12 , x11_13, x11_14 ;
bin x12_13, x12_14 ;
bin x13_14 ;