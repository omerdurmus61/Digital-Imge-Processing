clc;clear;

img = imread("1.png");
gray = rgb2gray(img);

gray_negative = 255 - gray;
original_negative = 255 - img;

subplot(2,2,1); imshow(img); title("Original");
subplot(2,2,2); imshow(original_negative); title("Negative")
subplot(2,2,3); imshow(gray); title("Gray");
subplot(2,2,4); imshow(gray_negative); title("Negative")