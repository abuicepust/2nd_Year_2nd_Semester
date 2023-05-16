clc;
close all;
fm=0.4;
fc=20;
Vm=1;
Vc=1;
fs=160;
t=0:1/fs:10;
m=Vm*cos(2*pi*fm*t);
c=Vc*cos(2*pi*fc*t);
y=ammod(m,fc,fs);
subplot(5,1,1);
plot(t,m);
title('Message Signal');
xlabel('Time');
ylabel('Amplitude');
subplot(5,1,2);
plot(t,c);
title('Carrier Signal');
xlabel('Time');
ylabel('Amplitude');
subplot(5,1,3);
plot(t,y);
title('Modulated Signal');
xlabel('Time');
ylabel('Amplitude');
Vd(1)=0;
for i=2:length(y)
    if y(i)>Vd(i-1)
        Vd(i)=y(i);
    else 
        Vd(i)=Vd(i-1)-0.023*Vd(i-1);
    end
end
       
h=fir1(100,0.0125,'low');
foutputc=filter(h,1,Vd);
subplot(5,1,4);
plot(t,Vd);
title('Envelop Detector output of Modulating Signal');
xlabel('Time');
ylabel('Amplitude');
subplot(5,1,5);
plot(t,foutputc);
title('Demodulated Signal');
xlabel('Time');
ylabel('Amplitude');
