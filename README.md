# midcli

Commandline to image generate from Midjorney on Hugface

## How to use

### Demo

![thumb_midcli2](https://github.com/user-attachments/assets/98596318-6cea-45b8-951a-b5ec749c1d75)

### Installation

```sh
pip install git+https://github.com/brunodavi/midcli
```

### Usage

```sh
NAME
    midcli

SYNOPSIS
    midcli PROMPT <flags>

POSITIONAL ARGUMENTS
    PROMPT
        Type: str

FLAGS
    -s, --style=STYLE
        Default: 'Anime'
    -f, --filename=FILENAME
        Default: 'image'
    -i, --image_dir=IMAGE_DIR
        Default: '.'

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS

EXAMPLE
    midcli 'Generate running person' --style 'Photo' --filename 'person_running' --image_dir '~/Images'

    # Generate 2 images in:
    # images/person_running1.png
    # images/person_running2.png
```
