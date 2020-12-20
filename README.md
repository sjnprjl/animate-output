# animate-output



> **Note**: **PIL** is required. So please install **PIL** module first.



## DESCRIPTION

> simple python program that output *ascii* art with animation.



## USAGE

```bash
animate_output.py <[-i] [--image]> [Location] || <[-a] [--ascii]> [Location]


```

```bash
## example
./animate_output.py --speed 0.01 --image google.jpg  ## image is included
## or
./animate_output.py --speed 0.01 --ascii google.txt  ## ascii art is included
## or just
./animate_output.py --speed 0.01 --clipboard ## content of clipboard will be used

```

## OPTIONS

```bash
  -h, --help            show this help message and exit
  -i IMAGE [IMAGE ...], --image IMAGE [IMAGE ...]
                        Location of image
  -a ASCII [ASCII ...], --ascii ASCII [ASCII ...]
                        Location of text file containing ascii art
  -c, --clipboard       Copy from clipboard
  -w [WIDTH], --width [WIDTH]
                        Width of ascii art
  -s [SPEED], --speed [SPEED]
  
  

```



## INSTALLATION

### ``Clone this repository``

```bash
git clone https://github.com/ilvghst/animate-output.git

```

### ``Change directory``

``` bash
cd animate-output

```

### ``Install dependencies ``

```bash
pip install -r requirements.txt

```

### ``Make it executable (unix user) && RUN IT!``

```bash
chmod +x animate_output.py 
./animate_output.py [ --speed ] 0.01 < [ --ascii ] [ --image ] > [ source ] < [ --clipboard ] >

```

>  *voilà*, you are good to go! 

## Thank you! 
