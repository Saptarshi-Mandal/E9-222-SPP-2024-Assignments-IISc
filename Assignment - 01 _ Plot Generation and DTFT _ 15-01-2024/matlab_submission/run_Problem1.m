clear
close all

%% Time specifications

T = [0.001, 0.01, 0.1, 1]; % Time Step Sizes

%% Problem 1 : Generate Plots

% 1) x_1(t) = Gaussian

figure(1);
plot_number = 1;
sgtitle('x_1(t)')
for time_step = T
    t = -5:time_step:5; 
    for sigma_sq = [0.1,1]
        subplot(4,2,plot_number)
        stem(t, exp((-t.^2)/(2*sigma_sq)))
        title(['T : ', num2str(time_step) ' and sigma_sq : ', num2str(sigma_sq)],'Interpreter','none')
        xlabel('Time (in seconds)')
        ylabel('Amplitude')
        plot_number= plot_number + 1;    
    end
end

% 2) x_2(t)

figure(2);
plot_number = 1;
sgtitle('x_2(t)')
for time_step = T
    t = -5:time_step:5; 
    subplot(4,1,plot_number)
    stem(t, exp(-abs(t)))
    title(['T : ', num2str(time_step)])
    xlabel('Time (in seconds)')
    ylabel('Amplitude')
    plot_number= plot_number + 1;
end

% 2) x_3(t)

figure(3);
plot_number = 1;
alpha = -0.02;
w_0 = 2*pi*200;
sgtitle('x_3(t)')
for time_step = T
    t = -5:time_step:5;
    subplot(4,1,plot_number)
    plot(t, exp(alpha*t).*cos(w_0.*t).*(t>0))
    title(['T : ', num2str(time_step)])
    xlabel('Time (in seconds)')
    ylabel('Amplitude')
    plot_number= plot_number + 1;
end
