clc;
close all;
k=1;
n=-2:2;
x=[-2,3,0,1,5];
subplot(2,1,1);
stem(n,x);
title('Given signal');
xlabel('n-->');
ylabel('x(n)');
[p,q]=user(k,n,x);
subplot(2,1,2);
stem(p,q);
title('Desired signal');
xlabel('p-->');
ylabel('q(p)');

function[r,s]=user(k,n,x)
r=n+k;
s=x;
end