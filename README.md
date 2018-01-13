# 距離感測

## 發想
題目發想來源是因為有些汽車都有距離偵測，當與別的車輛過近時會發出警告。我們決定在機車上面實作一個類似概念的偵測器，讓機車行時中，與左、右、後方車輛距離過近時會發出警告，以免在轉彎或煞車時造成後方車輛追撞，造成不必要的人財損失。

## 使用材料
| 材料名稱 | 數量 | 來源 |
| ------ | ------ | ------ | ------ |
| Raspberrt Pi 3 | 1 | 課堂提供 |
| HC-SR04 | 3 | 網拍購買 |
| 麵包版 | 1 | MoLi借用 |
| 燈泡 | 3 | Moli借用 |

## 成品
圖片~

## 程式
主要功能：不斷偵測感測器與其範圍內的東西過近(<50cm)時，使警告燈泡亮起。

(偵測並警報部分)
```python=
略...

while True:
	print("no.1 devices:cm=%f" % get_distance(GPIO_ECHO_1,GPIO_TRIGGER_1))
	print("no.2 devices:cm=%f" % get_distance(GPIO_ECHO_2,GPIO_TRIGGER_2))
	print("no.3 devices:cm=%f" % get_distance(GPIO_ECHO_3,GPIO_TRIGGER_3))
	danger = 50
	if get_distance(GPIO_ECHO_1,GPIO_TRIGGER_1) < danger:
		blink(4) # first
	if get_distance(GPIO_ECHO_2,GPIO_TRIGGER_2) < danger:
		blink(5) # second
	if get_distance(GPIO_ECHO_3,GPIO_TRIGGER_3) < danger:
		blink(6) # third
	time.sleep(0.005)

略...
```

## Reference Website
1. [Raspberry Pi 筆記(十五)：超音波測距離](http://atceiling.blogspot.tw/2014/03/raspberry-pi_18.html)
2. [SETTING WIFI UP VIA THE COMMAND LINE](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
3. [讓你的 Raspberry Pi 透過 GPIO 閃爍 LED 燈](https://coldnew.github.io/f7349436/)
4. [How to Exit GPIO programs cleanly, avoid warnings and protect your Pi](http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi)
5. [Week 14 (2017/12/20) 共筆 Raspberry Pi](https://hackmd.io/OwFgjATAHAZgrMAtANgEYBMDMjye1CEZRABhLDhNQggE5N1ag===?view)
6. [學習樹莓派--Raspberry Pi](https://sites.google.com/site/raspberypishare0918/home/lei-bi-gan-ce/chao-yin-bo-ce-ju)

## 簡報
https://docs.google.com/presentation/d/1NxVFpDTOssYJsdKBTjhcn7iXhTVzVvaKlWRpcO4yZtY/edit?usp=sharing
