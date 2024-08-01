clear
close all
%% Time specifications

T = [0.001, 0.01, 0.1, 1]; % Time Step Sizes

%% Problem 2 : Generate DTFT


% 1) x_1(t)

figure(1);
plot_number = 1;
sgtitle('Magnitude and Phase Plots of X_1(\omega)')
for time_step = T
    t = -5:time_step:5; 
    for sigma_sq = [0.1,1]
        x_1 = exp((-t.^2)/(2*sigma_sq));
        [dtft_x_1,w_axis] = DTFT(x_1);
        
        subplot(4,4,plot_number)       
        plot(w_axis, abs(dtft_x_1))        
        title(['Magnitude Spectrum, T : ', num2str(time_step) ' and sigma : ', num2str(sigma_sq)])
        xlabel('Frequency (in rad/s)')
        ylabel('Magnitude')

        subplot(4,4,plot_number+1)
        plot(w_axis, angle(dtft_x_1))        
        title(['Phase Spectrum, T : ', num2str(time_step) ' and sigma : ', num2str(sigma_sq)])
        xlabel('Frequency (in rad/s)')
        ylabel('Phase (in rads)')

        plot_number= plot_number + 2;    
    end
end

% 2) x_2

figure(2);
plot_number = 1;
sgtitle('Magnitude and Phase plots of X_2(\omega)')
for time_step = T

    t = -5:time_step:5; 
    x_2 = exp(-abs(t));
    [dtft_x_2, w_axis] = DTFT(x_2);

    subplot(4,3,plot_number)
    stem(t, x_2)
    title(['x_2(t), T : ', num2str(time_step)])
    xlabel('Time (in seconds)')
    ylabel('Amplitude')

    subplot(4,3,plot_number+1)
    plot(w_axis,abs(dtft_x_2))
    title(['Magnitude Spectrum, T : ', num2str(time_step)])
    xlabel('Frequency (rad/s)')
    ylabel('Magnitude')

    subplot(4,3,plot_number+2)
    plot(w_axis,angle(dtft_x_2))
    title(['Phase Spectrum , T : ', num2str(time_step)])
    xlabel('Frequency (in rad/s)')
    ylabel('Phase')

    plot_number= plot_number + 3;

end

% 3) x_3(t)

figure(3);
plot_number = 1;
alpha = -0.02;
w_0 = 2*pi*200;
sgtitle('Magnitude and Phase plots of X_3(\omega)')
for time_step = T

    t = -5:time_step:5; 
    x_3 = exp(alpha*t).*cos(w_0.*t).*(t>0);
    [dtft_x_3, w_axis] = DTFT(x_3);
    
    subplot(4,3,plot_number)
    plot(t, x_3)
    title(['x_3(t), T : ', num2str(time_step)])
    xlabel('Time (in seconds)')
    ylabel('Amplitude')

    subplot(4,3,plot_number+1)
    plot(w_axis,abs(dtft_x_3))
    title(['Magnitude Spectrum, T : ', num2str(time_step)])
    xlabel('Frequency (in rad/s)')
    ylabel('Magnitude')

    subplot(4,3,plot_number+2)
    plot(w_axis,angle(dtft_x_3))
    title(['Phase Spectrum, T : ', num2str(time_step)])
    xlabel('Frequency (in rad/s)')
    ylabel('Phase')

    plot_number= plot_number + 3;
    
end