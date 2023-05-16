clc;
close all;
N=input('Enter the length of the sequence ');
xn=input('Enter the sequence: ');
n=0:N-1;
k=0:N-1;
wN=exp((-1i*2*pi)/N);
nk=n'*k;
wNnk=wN.^nk;
xk=xn*wNnk;
disp('k-->>');
disp(xk);
mag=abs(xk);
subplot(2,1,1);
stem(k,mag);
grid on;
title('Magnitude of the Fourier Transform');
xlabel('k-->>');
ylabel('Magnitude(x(k))');
phase=angle(xk);
subplot(2,1,2);
stem(k,phase);
grid on;
title('Phase of the Fourier Transform');
xlabel('k-->');
ylabel('Phase(x(k))');