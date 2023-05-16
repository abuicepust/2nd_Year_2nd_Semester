x=-6:6;
n=[1:7,6:-1:1];
[n1,x1]= shift(n,x,5);
[n2,x2]= shift(n,x,-4);
%[n3,x3]= add(n1,n2,2*x1,(-3)*x2);
stem(n2,x2);
title("The desired sequence");
xlabel("n--->");
ylabel("Amplitude");

function[p,q] = shift(n,x,val)
p=n+val;
q=x;
end


