.PHONY: build install

install:
	rsync -avr --update ./build/02-colors.conf ~/.config/sway/config.d/.
	rsync -avr --update ./build/colors.css ~/.config/waybar/.
	rsync -avr --update ./build/colors.rasi ~/.config/rofi/.
	rsync -avr --update ./build/mako ~/.config/mako/config