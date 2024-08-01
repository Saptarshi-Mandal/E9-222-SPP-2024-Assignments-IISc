function [dft, w] = DTFT(x)

N = length(x);
w_resolution = 0.001;
w = -pi:w_resolution: pi - w_resolution;

n = -floorDiv(N,2):1:floorDiv(N,2);


dft = zeros(1,length(w));

for k = 1:1:length(w)
        dft(k) = sum( x.* exp(-1i * w(k) * n));
end

end