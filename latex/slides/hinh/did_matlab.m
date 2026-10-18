%% Minimalist figure for the DiD illustration
% Viết theo đúng bố cục figures.m của pmichaillat/matlab-figures (MIT).
% Chỉ khác ở chỗ cần để chạy được cả Octave: set(0,...) thay groot, bảng màu dạng số thay mã hex,
% fill thay xregion/area (màu nhạt tương đương FaceAlpha = 0.2).
% Dữ liệu là MINH HỌA (ngẫu nhiên có seed), không phải dữ liệu thật.

%% Clear workspace

close all
clear
clc

%% Set default properties for 4:3 figure

figureWidth = 8.5;
figureHeight = 6.375;
set(0, 'defaultFigureUnits', 'inches')
set(0, 'defaultFigurePosition', [1,1,figureWidth,figureHeight]);
set(0, 'defaultFigurePaperPosition', [0, 0, figureWidth,figureHeight]);
set(0, 'defaultFigurePaperSize', [figureWidth,figureHeight]);

%% Set default properties for axes

set(0, 'defaultAxesFontName', 'Helvetica')
set(0, 'defaultTextFontName', 'Helvetica')
set(0, 'defaultAxesFontSize', 24)
set(0, 'defaultTextFontSize', 24)
set(0, 'defaultAxesXColor', 'k')
set(0, 'defaultAxesYColor', 'k')
set(0, 'defaultAxesLineWidth', 1)
set(0, 'defaultAxesYGrid', 'on')
set(0, 'defaultAxesXGrid', 'off')
set(0, 'defaultAxesTickDir', 'out')
set(0, 'defaultAxesTickLength',[0.005, 0.005])
set(0, 'defaultAxesBox','off')

%% Predefine qualitative color palettes

% Dark colors
darkPalette = [27 158 119; 217 95 2; 117 112 179; 231 41 138; 102 166 30; 230 171 2; 166 118 29; 102 102 102]/255;
greenColor = darkPalette(1,:);
orangeColor = darkPalette(2,:);
purpleColor = darkPalette(3,:);

% Light colors (equivalent to FaceAlpha = 0.2 on white)
lightPurple = 0.8 + 0.2*purpleColor;
lightGray = 0.8 + 0.2*[0 0 0];

%% Create data

randn('seed', 3);
time = [2023:1/12:2029]';
pre = time < 2027;
post = ~pre;
n = numel(time);

common = filter(1, [1 -0.8], 0.035*randn(n,1));
data1 = 0.85 + common + 0.015*randn(n,1);    % mã chuyển sàn
data2 = 0.45 + common + 0.015*randn(n,1);    % mã HOSE đối sánh
data3 = data2 + mean(data1(pre) - data2(pre)); % nếu không chuyển sàn
data1(post) = data3(post) - 0.30 + 0.015*randn(sum(post),1);

% Create period
startPeriod = 2025.5;
endPeriod = 2027;

%% Predefine properties for x-axis

clear obj
obj.XLim = [2023, 2029];
obj.XTick = [2023:2:2029];
xAxis = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for y-axis

clear obj
obj.YLim = [0, 1.4];
obj.YTick = [0:0.2:1.4];
obj.YTickLabel = {};
yAxis = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for lines

clear obj
obj.Color = purpleColor;
obj.LineWidth = 3;
obj.LineStyle = '-';
purpleLine = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.Color = orangeColor;
obj.LineWidth = 3;
obj.LineStyle = '-';
orangeLine = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.Color = purpleColor;
obj.LineWidth = 3;
obj.LineStyle = ':';
purpleDotted = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for areas

clear obj
obj.FaceColor = lightGray;
obj.EdgeColor = 'none';
periodArea = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.FaceColor = lightPurple;
obj.EdgeColor = 'none';
purpleArea = [fieldnames(obj), struct2cell(obj)]';

%% Create a plot with a gray period area and a higher-lower area

% Open figure
iFigure = 1;
figure(iFigure)
clf
hold on

% Paint period area
fill([startPeriod endPeriod endPeriod startPeriod], [0 0 1.4 1.4], periodArea{:});

% Paint higher-lower area
fill([time(post); flipud(time(post))], [data3(post); flipud(data1(post))], purpleArea{:});

% Plot data
plot(time(post), data3(post), purpleDotted{:})
plot(time, data2, orangeLine{:})
plot(time, data1, purpleLine{:})

% Annotate (template annotates in Keynote; a few short labels here)
text(2023.1, 1.05, 'Mã chuyển sàn', 'Color', purpleColor)
text(2023.1, 0.22, 'Mã HOSE đối sánh', 'Color', orangeColor)
text(2027.1, 1.25, 'Nếu không chuyển sàn', 'Color', purpleColor)
text(2027.6, 0.80, 'Tác động', 'Color', purpleColor)

%Populate axes
set(gca, xAxis{:}, yAxis{:})
ylabel('Amihud (log)')

%Print figure
print('-dpdf', 'did.pdf')
