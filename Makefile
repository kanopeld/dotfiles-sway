.PHONY: configs_deploy, configs_collect

configs_deploy:
	rm -rf ~/.config/alacritty
	rsync -avr --update ./configs/alacritty ~/.config/

	rm -rf ~/.config/sway
	rsync -avr --update ./configs/sway --exclude=env/ ~/.config/

	rm -rf ~/.config/waybar
	rsync -avr --update ./configs/waybar ~/.config/

	mkdir -p ~/.config/environment.d
	rm -f ~/.config/environment.d/sway.conf
	rsync -avr --update ./configs/sway/env/wayland.conf ~/.config/environment.d/sway.conf

	rm -rf ~/.config/rofi
	rsync -avr --update ./configs/rofi ~/.config/

	rm -rf ~/.config/mako
	rsync -avr --update ./configs/mako ~/.config/

configs_collect:
	rm -rf ./config/*

	rsync -avr --update ~/.config/alacritty ./configs/
	rsync -avr --update ~/.config/sway ./configs/
	rsync -avr --update ~/.config/waybar ./configs/
	rsync -avr --update ~/.config/environment.d/sway.conf ./configs/sway/env/wayland.conf
	rsync -avr --update ~/.config/rofi ./configs/
	rsync -avr --update ~/.config/mako ./configs/

