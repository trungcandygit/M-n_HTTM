%% Hình minh họa khác biệt kép, theo thiết lập figures.m của pmichaillat/matlab-figures
% Chạy được cả MATLAB lẫn Octave (không dùng xregion, area, độ trong suốt, mã màu hex).
% Chuỗi là MINH HỌA (ngẫu nhiên có seed), không phải dữ liệu.

close all
clear
clc

%% Thiết lập mặc định của template (4:3, Helvetica 24, lưới ngang, vạch ra ngoài)
figureWidth = 8.5;
figureHeight = 6.375;
set(0, 'defaultFigureUnits', 'inches')
set(0, 'defaultFigurePosition', [1,1,figureWidth,figureHeight]);
set(0, 'defaultFigurePaperPosition', [0, 0, figureWidth,figureHeight]);
set(0, 'defaultFigurePaperSize', [figureWidth,figureHeight]);
set(0, 'defaultAxesFontName', 'Helvetica')
set(0, 'defaultTextFontName', 'Helvetica')
set(0, 'defaultAxesFontSize', 24)
set(0, 'defaultTextFontSize', 24)
set(0, 'defaultAxesLineWidth', 1)
set(0, 'defaultAxesYGrid', 'on')
set(0, 'defaultAxesXGrid', 'off')
set(0, 'defaultAxesTickDir', 'out')
set(0, 'defaultAxesTickLength', [0.005, 0.005])
set(0, 'defaultAxesBox', 'off')

%% Màu của template (Dark2) và màu nhạt tương đương độ mờ 0,2
purpleColor = [117 112 179]/255;
orangeColor = [217 95 2]/255;
lightPurple = 0.8*[1 1 1] + 0.2*purpleColor;
lightGray = [0.8 0.8 0.8];

%% Dữ liệu minh họa theo tháng, 2023-2028
randn('seed', 3);
time = (2023:1/12:2029)';
pre = time < 2027;
post = ~pre;
n = numel(time);
common = filter(1, [1 -0.8], 0.035*randn(n,1));      % cú sốc chung của thị trường
control = 0.45 + common + 0.015*randn(n,1);           % mã HOSE đối sánh
treated = 0.85 + common + 0.015*randn(n,1);           % mã chuyển sàn
gap = mean(treated(pre) - control(pre));
counterfactual = control + gap;                       % nếu không chuyển sàn: song song với đối chứng
treated(post) = counterfactual(post) - 0.30 + 0.015*randn(sum(post),1);

%% Vẽ
figure(1)
clf
hold on

% Dải xám: giai đoạn chuyển tiếp 7/2025-12/2026, loại khỏi kiểm định chính
fill([2025.5 2027 2027 2025.5], [0 0 1.4 1.4], lightGray, 'EdgeColor', 'none');

% Vùng tác động giữa đường "nếu không chuyển sàn" và đường thực tế
tp = time(post);
fill([tp; flipud(tp)], [counterfactual(post); flipud(treated(post))], lightPurple, 'EdgeColor', 'none');

plot(tp, counterfactual(post), ':', 'Color', purpleColor, 'LineWidth', 3)
plot(time, control, '-', 'Color', orangeColor, 'LineWidth', 3)
plot(time, treated, '-', 'Color', purpleColor, 'LineWidth', 3)

% Ít chữ: ba nhãn ngắn đặt cạnh đường
text(2023.1, 1.05, 'Mã chuyển sàn', 'Color', purpleColor)
text(2023.1, 0.22, 'Mã HOSE đối sánh', 'Color', orangeColor)
text(2027.1, 1.25, 'Nếu không chuyển sàn', 'Color', purpleColor, 'FontSize', 20)
text(2027.6, 0.80, 'Tác động', 'Color', purpleColor, 'FontSize', 20)

xlim([2023 2029]); set(gca, 'XTick', 2023:2:2029)
ylim([0 1.4]); set(gca, 'YTick', 0:0.2:1.4, 'YTickLabel', {})
ylabel('Amihud (log)')

print('-dpdf', 'did_matlab.pdf')
