clc;
close all;
n=-1:2;
x=[3,-1,0,-4];
subplot(2,1,1);
stem(n,x);
title('Main Signal');
xlabel('n-->');
ylabel('x(n)');
p=(-1)*n;
subplot(2,1,2);
stem(p,x);
title('Folded Signal');
xlabel('n-->');
ylabel('x(p)');

