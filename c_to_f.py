#!/usr/bin/env python
# coding: utf-8

# 攝氏(C) 轉換為華氏(F)程式
# 讓使用者輸入 攝氏溫度
# 然後印出華氏溫度

c_temp = input('請輸入攝氏溫度: ')
c_temp = float(c_temp)
f_temp = c_temp * 9 / 5 + 32
print('華氏溫度為: ', f_temp)

