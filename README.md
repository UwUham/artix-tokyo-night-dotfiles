# artix-tokyo-night-dotfiles
dotfiles (again)

so uh
idk what to write really

install dependencies:
Arch/Arch-based (with yay):

`$ yay -S - < ./dependencies`

Note: Ironically Artix's official repo and the AUR combined do not have the packages to satisfy this full list: You will need to either temporarily enable Arch's repo or download the PKGBUILDs for the missing applications.

Other distributions (or Arch without yay):
figure it out lol idk

apply the :rice: (working directory is the root of this repo (eg ~/artix-tokyo-night-dotfiles/))
```
$ cp -r ~/.config ~/.config-backup
$ cp -r * ~
$ nitrogen .
# reboot
```

# Notes
You will need to edit .config/polybar-forecast/config.toml to use your API key and city. You can find more information about this [here](https://openweathermap.org).
Alternatively, you can disable the module by removing it from `[bar/left]`/`modules-center` in .config/polybar/config.ini

# Wallpaper
<img src=wallpaper.jpg></img>

# Screenshot
<img src=screenshot.png></img>
